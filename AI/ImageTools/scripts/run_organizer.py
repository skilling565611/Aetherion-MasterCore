from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PROJECT_DIR = REPO_ROOT / "AI/ImageTools"
CONFIG_PATH = PROJECT_DIR / "Configs/default_config.json"

sys.path.insert(0, str(PROJECT_DIR / "scripts"))

from image_organizer import DEFAULT_LOG_DIR, organize_images  # noqa: E402


def repo_path(value: str | None, fallback: Path) -> Path:
    if not value:
        return fallback
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def load_config() -> dict[str, object]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def main() -> int:
    config = load_config()
    source = repo_path(str(config.get("source", "AI/PIX")), REPO_ROOT / "AI/PIX")
    output = repo_path(str(config.get("output", "AI/Perchance/IMG")), REPO_ROOT / "AI/Perchance/IMG")
    log_dir = repo_path(str(config.get("log_dir", "AI/ImageTools/Logs")), DEFAULT_LOG_DIR)
    ai_model = repo_path(str(config.get("ai_model", "")), PROJECT_DIR / "models/rating_model.onnx")
    ai_labels = repo_path(str(config.get("ai_labels", "")), PROJECT_DIR / "models/rating_labels.json")
    corrections = repo_path(str(config.get("corrections", "AI/ImageTools/Training/corrections.json")), PROJECT_DIR / "Training/corrections.json")
    copy_only = bool(config.get("copy_only", True))

    # This runner never enables move/delete behavior. The existing organizer
    # also refuses to run when copy_only is false.
    if not copy_only:
        raise SystemExit("Config copy_only must stay true. ImageTools never moves or deletes originals.")

    print("ImageTools organizer")
    print(f"Source: {source}")
    print(f"Output: {output}")
    print(f"Character: {config.get('character', 'Nyra_Vale')}")
    print(f"dry_run: {bool(config.get('dry_run', True))}")
    print(f"use_ai: {bool(config.get('use_ai', False))}")
    print(f"confidence_threshold: {float(config.get('confidence_threshold', 0.7))}")

    _results, report_paths = organize_images(
        source_dir=source,
        output_root=output,
        character=str(config.get("character", "Nyra_Vale")),
        recursive=bool(config.get("recursive", True)),
        dry_run=bool(config.get("dry_run", True)),
        copy_only=True,
        confidence_threshold=float(config.get("confidence_threshold", 0.7)),
        review_uncertain=bool(config.get("review_uncertain", True)),
        use_ai=bool(config.get("use_ai", False)),
        ai_model=ai_model,
        ai_labels=ai_labels,
        ai_flip_binary_labels=bool(config.get("ai_flip_binary_labels", False)),
        ai_debug_outputs=bool(config.get("ai_debug_outputs", True)),
        force_review_on_suspicious_sfw=bool(config.get("force_review_on_suspicious_sfw", True)),
        suspicious_skin_ratio_threshold=float(config.get("suspicious_skin_ratio_threshold", 0.16)),
        suspicious_bright_ratio_threshold=float(config.get("suspicious_bright_ratio_threshold", 0.45)),
        corrections_path=corrections,
        log_dir=log_dir,
        debug=bool(config.get("debug", True)),
    )

    print("Organizer complete. Originals were never deleted, moved, or modified.")
    for label, path in report_paths.items():
        print(f"{label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
