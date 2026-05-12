from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterator

from light_ai_classifier import AIConfig, LocalAIClassifier
from furry_rules import detect_furry_rules, refine_with_furry_rules
from manual_corrections import find_manual_correction, load_corrections
from rating_rules import (
    RATING_CATEGORIES,
    SUPPORTED_EXTENSIONS,
    VisualSignals,
    combine_decisions,
    detect_character,
    filename_context,
    keyword_rating,
    LINGERIE_KEYWORDS,
    safe_name,
    SFW_KEYWORDS,
    visual_rating,
)
from reporting import ReportWriter, utc_now


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_SOURCE_DIR = REPO_ROOT / "AI/PIX"
DEFAULT_OUTPUT_ROOT = REPO_ROOT / "AI/Perchance/IMG"
DEFAULT_CHARACTER = "Nyra_Vale"
DEFAULT_LOG_DIR = REPO_ROOT / "AI/ImageTools/Logs"
DEFAULT_CONFIG_PATH = REPO_ROOT / "AI/ImageTools/Configs/default_config.json"
DEFAULT_AI_MODEL = REPO_ROOT / "AI/ImageTools/Models/ONNX/model.onnx"
DEFAULT_AI_LABELS = REPO_ROOT / "AI/ImageTools/Models/ONNX/labels.json"
DEFAULT_CORRECTIONS = REPO_ROOT / "AI/ImageTools/Training/corrections.json"


@dataclass(frozen=True)
class ImageMeta:
    path: Path
    size_bytes: int
    modified_at: str
    sha256: str
    width: int | None
    height: int | None


@dataclass(frozen=True)
class OrganizeResult:
    source: str
    target: str
    original_name: str
    clean_name: str
    character: str
    category: str
    confidence: float
    used_ai: bool
    matched_rules: list[str]
    reason: str
    duplicate_status: str
    dry_run: bool


def is_supported_image(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS


def iter_images(source_dir: Path, recursive: bool = True) -> Iterator[Path]:
    if not source_dir.exists():
        raise SystemExit(f"Source folder does not exist: {source_dir}")
    if not source_dir.is_dir():
        raise SystemExit(f"Source path is not a folder: {source_dir}")

    iterator = source_dir.rglob("*") if recursive else source_dir.iterdir()
    for path in iterator:
        if is_supported_image(path):
            yield path


def hash_file(path: Path, chunk_size: int = 1024 * 256) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def analyze_with_pillow(path: Path, max_side: int = 96) -> VisualSignals:
    try:
        from PIL import Image
    except Exception:
        return VisualSignals(
            pillow_available=False,
            error=(
                "Pillow is missing. Install it with: python -m pip install -e AI/ImageTools "
                "or python -m pip install -r AI/ImageTools/Requirements/image.txt"
            ),
        )

    try:
        with Image.open(path) as image:
            width, height = image.size
            image.thumbnail((max_side, max_side))
            rgb = image.convert("RGB")
            pixel_source = rgb.get_flattened_data() if hasattr(rgb, "get_flattened_data") else rgb.getdata()
            pixels = list(pixel_source)
    except Exception as error:
        return VisualSignals(pillow_available=True, error=f"Pillow could not read image: {error}")

    if not pixels:
        return VisualSignals(width=width, height=height, pillow_available=True, error="Image had no pixels")

    skin_like = 0
    bright = 0
    neon = 0
    total = len(pixels)

    # Cheap color heuristics only. This is not a nudity detector; it just helps
    # decide when a rating should be reviewed instead of trusting filenames.
    for red, green, blue in pixels:
        max_channel = max(red, green, blue)
        min_channel = min(red, green, blue)
        if red > 95 and green > 40 and blue > 20 and red > green and red > blue and max_channel - min_channel > 15:
            skin_like += 1
        if max_channel > 210:
            bright += 1
        if (red > 180 and blue > 150 and green < 130) or (green > 170 and blue > 150 and red < 130):
            neon += 1

    return VisualSignals(
        width=width,
        height=height,
        skin_like_ratio=skin_like / total,
        bright_ratio=bright / total,
        neon_ratio=neon / total,
        pillow_available=True,
    )


def image_meta(path: Path, signals: VisualSignals) -> ImageMeta:
    stat = path.stat()
    return ImageMeta(
        path=path,
        size_bytes=stat.st_size,
        modified_at=datetime.fromtimestamp(stat.st_mtime).replace(microsecond=0).isoformat(),
        sha256=hash_file(path),
        width=signals.width,
        height=signals.height,
    )


def clean_stem(path: Path) -> str:
    stem = re.sub(r"\s*\(\d+\)$", "", path.stem)
    stem = re.sub(r"[_\-\s]+", "_", stem).strip("_")
    stem = re.sub(r"[^A-Za-z0-9_]+", "", stem)
    return stem or "image"


def clean_filename(path: Path, character: str, category: str, sha256: str, rename: bool = True) -> str:
    if not rename:
        return path.name
    return f"{safe_name(character)}_{safe_name(category)}_{clean_stem(path)}_{sha256[:8]}{path.suffix.lower()}"


def unique_target_path(target_dir: Path, filename: str) -> Path:
    candidate = target_dir / filename
    if not candidate.exists():
        return candidate

    stem = candidate.stem
    suffix = candidate.suffix
    counter = 1
    while True:
        next_candidate = target_dir / f"{stem}_{counter:02d}{suffix}"
        if not next_candidate.exists():
            return next_candidate
        counter += 1


def scan_report_entry(meta: ImageMeta, signals: VisualSignals) -> dict[str, object]:
    return {
        "path": str(meta.path),
        "filename": meta.path.name,
        "extension": meta.path.suffix.lower(),
        "size_bytes": meta.size_bytes,
        "modified_at": meta.modified_at,
        "width": meta.width,
        "height": meta.height,
        "sha256": meta.sha256,
        "visual_signals": {
            "pillow_available": signals.pillow_available,
            "skin_like_ratio": signals.skin_like_ratio,
            "bright_ratio": signals.bright_ratio,
            "neon_ratio": signals.neon_ratio,
            "error": signals.error,
        },
    }


def ai_log_metadata(ai_decision: object | None) -> dict[str, object]:
    """Return stable AI debug fields for every decision log entry."""

    empty = {
        "ai_raw_outputs": None,
        "ai_probabilities": None,
        "ai_selected_index": None,
        "ai_selected_label": None,
        "ai_label_mapping": None,
        "ai_model_input_shape": None,
        "ai_model_output_shape": None,
        "ai_preprocessing_mode": None,
    }
    metadata = getattr(ai_decision, "metadata", None)
    if not isinstance(metadata, dict):
        return empty

    return {
        "ai_raw_outputs": metadata.get("ai_raw_outputs"),
        "ai_probabilities": metadata.get("ai_probabilities"),
        "ai_selected_index": metadata.get("ai_selected_index"),
        "ai_selected_label": metadata.get("ai_selected_label"),
        "ai_label_mapping": metadata.get("ai_label_mapping"),
        "ai_model_input_shape": metadata.get("ai_model_input_shape"),
        "ai_model_output_shape": metadata.get("ai_model_output_shape"),
        "ai_preprocessing_mode": metadata.get("ai_preprocessing_mode"),
        "ai_original_selected_index": metadata.get("ai_original_selected_index"),
        "ai_actual_output_shape": metadata.get("ai_actual_output_shape"),
        "ai_flip_binary_labels": metadata.get("ai_flip_binary_labels"),
        "ai_flip_binary_labels_requested": metadata.get("ai_flip_binary_labels_requested"),
        "ai_labels_may_be_reversed": metadata.get("ai_labels_may_be_reversed"),
        "ai_label_count_matches_output": metadata.get("ai_label_count_matches_output"),
        "ai_label_count_warning": metadata.get("ai_label_count_warning"),
    }


def is_suspicious_sfw_ai_result(
    path: Path,
    signals: VisualSignals,
    skin_threshold: float,
    bright_threshold: float,
) -> bool:
    """Detect cases where a high-confidence SFW AI result should be reviewed.

    This is deliberately conservative. It does not decide NSFW by itself; it
    only prevents an AI SFW result from overriding visual uncertainty when the
    filename does not provide clothing/safe context.
    """

    tokens = filename_context(path)
    clothing_or_safe_keywords = SFW_KEYWORDS | LINGERIE_KEYWORDS
    if tokens & clothing_or_safe_keywords:
        return False

    skin = signals.skin_like_ratio or 0.0
    bright = signals.bright_ratio or 0.0
    return skin >= skin_threshold or bright >= bright_threshold


def is_strong_filename_rule(decision: object) -> bool:
    """Return true when filename/folder keywords should outrank weak signals."""

    category = getattr(decision, "category", None)
    confidence = float(getattr(decision, "confidence", 0.0))
    reason = str(getattr(decision, "reason", ""))
    return (
        category in {"SFW", "Suggestive", "Lingerie", "Partial_Nude", "Nude", "Explicit"}
        and confidence >= 0.72
        and reason.startswith("filename_or_folder_matched_")
    )


def resolve_config_path(value: str | Path | None) -> Path | None:
    """Resolve user-friendly config paths from the repository root.

    Beginners often run this script from the repo root, so relative config
    paths are treated as repo-relative instead of depending on the shell's
    current directory.
    """

    if value is None:
        return None
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def resolve_repo_path(value: str | Path | None) -> Path | None:
    """Resolve config paths while keeping absolute paths unchanged."""

    if value in (None, ""):
        return None
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def load_config(config_path: Path | None) -> dict[str, object]:
    """Load optional JSON config without making it required.

    The command line remains fully usable without a config file. When a config
    is supplied, those values become defaults and normal CLI flags can still
    override them.
    """

    if config_path is None:
        return {}
    if not config_path.exists():
        raise SystemExit(f"Config file does not exist: {config_path}")
    try:
        payload = json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise SystemExit(f"Config file is not valid JSON: {config_path} ({error})") from error
    if not isinstance(payload, dict):
        raise SystemExit(f"Config file must contain a JSON object: {config_path}")
    return payload


def config_bool(config: dict[str, object], key: str, default: bool) -> bool:
    value = config.get(key, default)
    return bool(value)


def organize_images(
    source_dir: Path,
    output_root: Path,
    character: str = DEFAULT_CHARACTER,
    recursive: bool = True,
    dry_run: bool = False,
    copy_only: bool = True,
    confidence_threshold: float = 0.70,
    review_uncertain: bool = True,
    use_ai: bool = False,
    ai_model: Path | None = None,
    ai_labels: Path | None = None,
    ai_model_load_mode: str = "source",
    ai_flip_binary_labels: bool = False,
    ai_debug_outputs: bool = False,
    force_review_on_suspicious_sfw: bool = True,
    suspicious_skin_ratio_threshold: float = 0.16,
    suspicious_bright_ratio_threshold: float = 0.45,
    corrections_path: Path | None = DEFAULT_CORRECTIONS,
    log_dir: Path = DEFAULT_LOG_DIR,
    rename: bool = True,
    known_characters: list[str] | None = None,
    debug: bool = False,
) -> tuple[list[OrganizeResult], dict[str, Path]]:
    if not copy_only:
        raise SystemExit("This tool is copy-only. Moving or deleting originals is intentionally unsupported.")

    reports = ReportWriter(log_dir)
    ai_classifier = LocalAIClassifier(
        enabled=use_ai,
        config=AIConfig(
            model_path=ai_model,
            labels_path=ai_labels,
            flip_binary_labels=ai_flip_binary_labels,
            debug_outputs=ai_debug_outputs,
            load_mode=ai_model_load_mode,
        ),
    )
    first_hash_path: dict[str, Path] = {}
    results: list[OrganizeResult] = []
    warned_pillow = False
    corrections = load_corrections(corrections_path)

    if use_ai and debug:
        print(f"DEBUG ai: {ai_classifier.reason}")
        print(f"DEBUG ai_model_path: {ai_classifier.model_path}")
        print(f"DEBUG ai_model_exists: {ai_classifier.model_exists}")

    for path in iter_images(source_dir, recursive=recursive):
        signals = analyze_with_pillow(path)
        if not signals.pillow_available and not warned_pillow:
            print(signals.error or "Pillow is missing. Install it with: python -m pip install Pillow")
            warned_pillow = True
        meta = image_meta(path, signals)
        reports.add_scan(scan_report_entry(meta, signals))

        duplicate_of = first_hash_path.get(meta.sha256)
        duplicate_status = "unique" if duplicate_of is None else f"duplicate_of:{duplicate_of}"
        if duplicate_of is None:
            first_hash_path[meta.sha256] = path

        detected_character, character_rules = detect_character(path, character, known_characters)
        keyword_decision = keyword_rating(path)
        visual_decision = visual_rating(signals)
        ai_decision = ai_classifier.classify(path, signals) if use_ai else None
        furry_rules = detect_furry_rules(path, signals)
        final_layer_used = "general_onnx_model" if ai_decision is not None else "filename_visual_rules"
        if is_strong_filename_rule(keyword_decision):
            decision = keyword_decision
            final_layer_used = "strong_filename_folder_rules"
        else:
            decision = combine_decisions(
                keyword=keyword_decision,
                visual=visual_decision,
                ai_decision=ai_decision,
                confidence_threshold=confidence_threshold,
                review_uncertain=review_uncertain,
            )
        suspicious_sfw_override_applied = False
        if (
            force_review_on_suspicious_sfw
            and ai_decision is not None
            and ai_decision.category == "SFW"
            and decision.category == "SFW"
            and is_suspicious_sfw_ai_result(
                path=path,
                signals=signals,
                skin_threshold=suspicious_skin_ratio_threshold,
                bright_threshold=suspicious_bright_ratio_threshold,
            )
        ):
            suspicious_sfw_override_applied = True
            decision = type(decision)(
                "Review_Needed",
                min(decision.confidence, ai_decision.confidence),
                decision.matched_rules + [
                    "suspicious_sfw_ai_result",
                    f"suspicious_skin_threshold:{suspicious_skin_ratio_threshold:.3f}",
                    f"suspicious_bright_threshold:{suspicious_bright_ratio_threshold:.3f}",
                ],
                "suspicious_sfw_ai_result",
                decision.metadata,
            )
            final_layer_used = "review_needed_fallback"
        refined_decision = refine_with_furry_rules(decision, furry_rules)
        if refined_decision != decision:
            decision = refined_decision
            final_layer_used = "furry_anthro_rule_refinement"
        if decision.category == "Review_Needed":
            final_layer_used = "review_needed_fallback"
        automated_decision = decision
        manual_correction = find_manual_correction(corrections, meta.sha256, path.name)
        manual_correction_applied = manual_correction is not None
        manual_correct_label = manual_correction.correct_label if manual_correction else None
        manual_correction_reason = manual_correction.reason if manual_correction else None
        manual_previous_label = None
        manual_correction_notes = None
        manual_correction_created_at = None
        if manual_correction is not None:
            manual_previous_label = manual_correction.entry.get("previous_label") or automated_decision.category
            manual_correction_notes = manual_correction.entry.get("notes")
            manual_correction_created_at = manual_correction.entry.get("created_at")
            decision = type(decision)(
                manual_correction.correct_label,
                1.0,
                decision.matched_rules
                + [
                    f"manual_correction:{manual_correction.reason}",
                    f"manual_correction_overrode:{automated_decision.category}",
                ],
                f"manual_correction:{manual_correction.reason}",
                decision.metadata,
            )
            final_layer_used = "manual_correction_sha256" if manual_correction.reason == "sha256_match" else "manual_correction_filename"

        target_dir = output_root / safe_name(detected_character) / safe_name(decision.category)
        target_name = clean_filename(path, detected_character, decision.category, meta.sha256, rename=rename)
        target_path = unique_target_path(target_dir, target_name)
        ai_was_used = bool(ai_decision is not None and ai_classifier.available)
        if target_path.name != target_name:
            duplicate_status = f"{duplicate_status};target_filename_adjusted"

        if not dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target_path)

        if duplicate_of is not None:
            reports.add_duplicate(
                {
                    "original_path": str(path),
                    "duplicate_of": str(duplicate_of),
                    "sha256": meta.sha256,
                    "output_path": str(target_path),
                }
            )

        matched_rules = character_rules + decision.matched_rules
        log_entry = {
            "original_path": str(path),
            "output_path": str(target_path),
            "filename": path.name,
            "detected_character": detected_character,
            "rating_category": decision.category,
            "confidence": decision.confidence,
            "used_ai": ai_was_used,
            "matched_rules": matched_rules,
            "reason": decision.reason,
            "timestamp": utc_now(),
            "duplicate_status": duplicate_status,
            "dry_run": dry_run,
            "ai_status": ai_classifier.reason if use_ai else "AI mode disabled",
            "suspicious_sfw_override_applied": suspicious_sfw_override_applied,
            "manual_correction_applied": manual_correction_applied,
            "manual_correct_label": manual_correct_label,
            "manual_correction_reason": manual_correction_reason,
            "manual_previous_label": manual_previous_label,
            "manual_correction_notes": manual_correction_notes,
            "manual_correction_created_at": manual_correction_created_at,
            "automated_rating_category": automated_decision.category,
            "automated_confidence": automated_decision.confidence,
            "automated_reason": automated_decision.reason,
            "raw_model_label": getattr(ai_decision, "metadata", {}).get("ai_selected_label") if ai_decision else None,
            "raw_model_category": ai_decision.category if ai_decision else None,
            "final_organizer_label": decision.category,
        }
        log_entry.update(ai_classifier.log_metadata())
        log_entry.update(furry_rules.log_fields(final_layer_used))
        log_entry.update(ai_log_metadata(ai_decision))
        reports.add_decision(log_entry)

        result = OrganizeResult(
            source=str(path),
            target=str(target_path),
            original_name=path.name,
            clean_name=target_name,
            character=detected_character,
            category=decision.category,
            confidence=decision.confidence,
            used_ai=ai_was_used,
            matched_rules=matched_rules,
            reason=decision.reason,
            duplicate_status=duplicate_status,
            dry_run=dry_run,
        )
        results.append(result)

        if debug:
            print(
                "DEBUG decision:",
                path.name,
                f"-> {detected_character}/{decision.category}",
                f"confidence={decision.confidence:.2f}",
                f"duplicate={duplicate_status}",
                f"reason={decision.reason}",
            )

    report_paths = reports.write()
    return results, report_paths


def parse_args() -> argparse.Namespace:
    # Pre-parse only --config so JSON values can become parser defaults. This
    # keeps every existing command-line argument working while allowing command
    # line values to override the config file.
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--config", type=Path, default=None, help="Optional JSON config file.")
    pre_args, remaining = pre_parser.parse_known_args()
    config_path = resolve_config_path(pre_args.config)
    config = load_config(config_path)

    source_default = resolve_repo_path(config.get("source")) or DEFAULT_SOURCE_DIR
    output_default = resolve_repo_path(config.get("output")) or DEFAULT_OUTPUT_ROOT
    log_dir_default = resolve_repo_path(config.get("log_dir")) or DEFAULT_LOG_DIR
    ai_model_default = resolve_repo_path(config.get("ai_model")) or DEFAULT_AI_MODEL
    ai_labels_default = resolve_repo_path(config.get("ai_labels")) or DEFAULT_AI_LABELS
    corrections_default = resolve_repo_path(config.get("corrections")) or DEFAULT_CORRECTIONS

    parser = argparse.ArgumentParser(
        description="Lightweight local image rating organizer for Aetherion character assets.",
        parents=[pre_parser],
    )
    parser.set_defaults(config=config_path)
    parser.add_argument("--source", type=Path, default=source_default, help=f"Source folder. Default: {DEFAULT_SOURCE_DIR}")
    parser.add_argument("--output", "--target-root", dest="output", type=Path, default=output_default, help=f"Output root. Default: {DEFAULT_OUTPUT_ROOT}")
    parser.add_argument("--character", default=str(config.get("character", DEFAULT_CHARACTER)), help=f"Default character folder. Default: {DEFAULT_CHARACTER}")
    parser.add_argument("--known-character", action="append", default=[], help="Additional character name to detect from paths.")
    parser.add_argument("--recursive", action=argparse.BooleanOptionalAction, default=config_bool(config, "recursive", True), help="Scan recursively. Default: true")
    parser.add_argument("--use-ai", action="store_true", default=config_bool(config, "use_ai", False), help="Enable optional local AI hook when dependencies/model are installed.")
    parser.add_argument("--ai-model", type=Path, default=ai_model_default, help="Optional local ONNX model path for --use-ai.")
    parser.add_argument("--ai-labels", type=Path, default=ai_labels_default, help="Optional JSON labels file for --use-ai.")
    parser.add_argument("--corrections", type=Path, default=corrections_default, help="Manual corrections JSON path.")
    parser.add_argument("--ai-flip-binary-labels", action="store_true", default=config_bool(config, "ai_flip_binary_labels", False), help="Flip two-class SFW/NSFW label order after model inference.")
    parser.add_argument("--ai-debug-outputs", action="store_true", default=config_bool(config, "ai_debug_outputs", False), help="Include raw ONNX debug outputs in logs.")
    parser.add_argument("--force-review-on-suspicious-sfw", action=argparse.BooleanOptionalAction, default=config_bool(config, "force_review_on_suspicious_sfw", True), help="Force Review_Needed when AI says SFW but visual signals look suspicious.")
    parser.add_argument("--dry-run", action="store_true", default=config_bool(config, "dry_run", False), help="Preview decisions without copying files.")
    parser.add_argument("--copy-only", action="store_true", default=config_bool(config, "copy_only", True), help="Safety flag; copy-only is always enforced.")
    parser.add_argument("--confidence-threshold", type=float, default=float(config.get("confidence_threshold", 0.70)), help="Review threshold. Default: 0.70")
    parser.add_argument("--suspicious-skin-ratio-threshold", type=float, default=float(config.get("suspicious_skin_ratio_threshold", 0.16)), help="Skin-like ratio threshold for suspicious SFW override.")
    parser.add_argument("--suspicious-bright-ratio-threshold", type=float, default=float(config.get("suspicious_bright_ratio_threshold", 0.45)), help="Bright ratio threshold for suspicious SFW override.")
    parser.add_argument("--review-uncertain", action=argparse.BooleanOptionalAction, default=config_bool(config, "review_uncertain", True), help="Send low-confidence images to Review_Needed.")
    parser.add_argument("--log-dir", type=Path, default=log_dir_default, help=f"JSON log folder. Default: {DEFAULT_LOG_DIR}")
    parser.add_argument("--no-rename", action="store_true", default=not config_bool(config, "rename", True), help="Keep original filename except when duplicate-safe suffixes are needed.")
    parser.add_argument("--list", action="store_true", help="Only list supported images.")
    parser.add_argument("--debug", action="store_true", default=config_bool(config, "debug", False), help="Print debug output for each decision.")
    return parser.parse_args(remaining)


def main() -> int:
    args = parse_args()

    if args.list:
        count = 0
        for path in iter_images(args.source, recursive=args.recursive):
            count += 1
            print(path)
        print(f"Found {count} supported image(s).")
        return 0

    results, report_paths = organize_images(
        source_dir=args.source,
        output_root=args.output,
        character=args.character,
        recursive=args.recursive,
        dry_run=args.dry_run,
        copy_only=args.copy_only,
        confidence_threshold=args.confidence_threshold,
        review_uncertain=args.review_uncertain,
        use_ai=args.use_ai,
        ai_model=args.ai_model,
        ai_labels=args.ai_labels,
        ai_model_load_mode="source",
        ai_flip_binary_labels=args.ai_flip_binary_labels,
        ai_debug_outputs=args.ai_debug_outputs,
        force_review_on_suspicious_sfw=args.force_review_on_suspicious_sfw,
        suspicious_skin_ratio_threshold=args.suspicious_skin_ratio_threshold,
        suspicious_bright_ratio_threshold=args.suspicious_bright_ratio_threshold,
        corrections_path=args.corrections,
        log_dir=args.log_dir,
        rename=not args.no_rename,
        known_characters=args.known_character,
        debug=args.debug,
    )

    for result in results:
        prefix = "Would copy" if result.dry_run else "Copied"
        print(f"{prefix}: {result.source} -> {result.target} [{result.character}/{result.category} {result.confidence:.2f}]")
    print(f"Processed {len(results)} image(s). Originals were never deleted or modified.")
    for label, path in report_paths.items():
        print(f"{label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
