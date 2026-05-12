from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator


REPO_ROOT = Path(__file__).resolve().parents[3]
TRAINING_ROOT = REPO_ROOT / "AI/ImageTools/Training"
DEFAULT_CORRECTIONS = TRAINING_ROOT / "corrections.json"
DEFAULT_DATASET_ROOT = TRAINING_ROOT / "Dataset"
DEFAULT_MANIFEST = TRAINING_ROOT / "dataset_manifest.json"
DEFAULT_SEARCH_ROOTS = [REPO_ROOT / "AI/PIX", REPO_ROOT / "AI/Perchance/IMG"]
LABELS = (
    "SFW",
    "Suggestive",
    "Lingerie",
    "Partial_Nude",
    "Nude",
    "Explicit",
    "Unknown",
    "Review_Needed",
)
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def resolve_repo_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def hash_file(path: Path, chunk_size: int = 1024 * 256) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def iter_images(search_roots: list[Path]) -> Iterator[Path]:
    seen: set[Path] = set()
    for root in search_roots:
        if not root.exists():
            continue
        iterator = root.rglob("*") if root.is_dir() else [root]
        for path in iterator:
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
                yield path


def load_corrections(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    corrections = payload.get("corrections", []) if isinstance(payload, dict) else []
    if not isinstance(corrections, list):
        raise SystemExit(f"Corrections file must contain a corrections list: {path}")
    return [entry for entry in corrections if isinstance(entry, dict)]


def load_manifest(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return [entry for entry in payload if isinstance(entry, dict)]
    raise SystemExit(f"Dataset manifest must contain a JSON list: {path}")


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def repo_display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def duplicate_safe_path(folder: Path, filename: str) -> Path:
    candidate = folder / filename
    if not candidate.exists():
        return candidate

    stem = candidate.stem
    suffix = candidate.suffix
    counter = 1
    while True:
        next_candidate = folder / f"{stem}_{counter:02d}{suffix}"
        if not next_candidate.exists():
            return next_candidate
        counter += 1


def build_sha_index(search_roots: list[Path]) -> dict[str, Path]:
    index: dict[str, Path] = {}
    for image in iter_images(search_roots):
        sha256 = hash_file(image)
        index.setdefault(sha256.lower(), image)
    return index


def find_corrected_image(entry: dict[str, Any], sha_index: dict[str, Path]) -> Path | None:
    original_path = entry.get("original_path")
    if original_path:
        candidate = resolve_repo_path(str(original_path))
        if candidate.exists() and candidate.is_file():
            return candidate

    sha256 = str(entry.get("sha256", "")).lower()
    if sha256:
        return sha_index.get(sha256)
    return None


def ensure_dataset_folders(dataset_root: Path) -> None:
    for label in LABELS:
        (dataset_root / label).mkdir(parents=True, exist_ok=True)


def build_dataset(
    corrections_path: Path,
    dataset_root: Path,
    manifest_path: Path,
    search_roots: list[Path],
    dry_run: bool = False,
) -> list[dict[str, Any]]:
    corrections = load_corrections(corrections_path)
    manifest = load_manifest(manifest_path)
    existing = {str(entry.get("sha256", "")).lower() for entry in manifest if entry.get("sha256")}
    sha_index = build_sha_index(search_roots)
    ensure_dataset_folders(dataset_root)

    for correction in corrections:
        sha256 = str(correction.get("sha256", "")).lower()
        correct_label = str(correction.get("correct_label", ""))
        if not sha256 or sha256 in existing or correct_label not in LABELS:
            continue

        image_path = find_corrected_image(correction, sha_index)
        if image_path is None:
            continue

        target_folder = dataset_root / correct_label
        target_name = f"{sha256[:8]}_{image_path.name}"
        target_path = duplicate_safe_path(target_folder, target_name)
        if not dry_run:
            shutil.copy2(image_path, target_path)

        manifest.append(
            {
                "original_path": repo_display_path(image_path),
                "copied_dataset_path": repo_display_path(target_path),
                "sha256": sha256,
                "filename": image_path.name,
                "correct_label": correct_label,
                "previous_label": correction.get("previous_label", ""),
                "character": correction.get("character", ""),
                "notes": correction.get("notes", ""),
                "created_at": utc_now(),
            }
        )
        existing.add(sha256)

    if not dry_run:
        write_json(manifest_path, manifest)
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Copy corrected ImageTools examples into a future training dataset.")
    parser.add_argument("--corrections", type=Path, default=DEFAULT_CORRECTIONS, help="Corrections JSON path.")
    parser.add_argument("--dataset-root", type=Path, default=DEFAULT_DATASET_ROOT, help="Dataset output folder.")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="Dataset manifest JSON path.")
    parser.add_argument("--search-root", action="append", default=[], help="Folder or image path to search for corrected images.")
    parser.add_argument("--dry-run", action="store_true", help="Preview manifest changes without copying files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    search_roots = [resolve_repo_path(path) for path in args.search_root] or DEFAULT_SEARCH_ROOTS
    manifest = build_dataset(
        corrections_path=resolve_repo_path(args.corrections),
        dataset_root=resolve_repo_path(args.dataset_root),
        manifest_path=resolve_repo_path(args.manifest),
        search_roots=search_roots,
        dry_run=args.dry_run,
    )
    action = "Would write" if args.dry_run else "Wrote"
    print(f"{action} dataset manifest with {len(manifest)} entr{'y' if len(manifest) == 1 else 'ies'}.")
    print("Original images were never moved, deleted, or modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
