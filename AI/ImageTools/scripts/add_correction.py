from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from manual_corrections import load_corrections, validate_label, write_corrections
from reporting import utc_now


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CORRECTIONS = REPO_ROOT / "AI/ImageTools/Training/corrections.json"


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


def repo_display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Add or update a manual ImageTools rating correction.")
    parser.add_argument("--image", required=True, type=Path, help="Image path to correct.")
    parser.add_argument("--label", required=True, help="Correct rating label.")
    parser.add_argument("--previous-label", default="", help="Previous incorrect label, if known.")
    parser.add_argument("--notes", default="", help="Short correction note.")
    parser.add_argument("--corrections", type=Path, default=DEFAULT_CORRECTIONS, help="Corrections JSON path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    image_path = resolve_repo_path(args.image)
    corrections_path = resolve_repo_path(args.corrections)
    label = validate_label(args.label)

    if not image_path.exists() or not image_path.is_file():
        raise SystemExit(f"Image does not exist: {image_path}")

    sha256 = hash_file(image_path)
    corrections = load_corrections(corrections_path)
    new_entry = {
        "sha256": sha256,
        "original_path": repo_display_path(image_path),
        "filename": image_path.name,
        "correct_label": label,
        "previous_label": args.previous_label,
        "notes": args.notes,
        "created_at": utc_now(),
    }

    updated = False
    for index, entry in enumerate(corrections):
        if str(entry.get("sha256", "")).lower() == sha256.lower():
            corrections[index] = {**entry, **new_entry}
            updated = True
            break

    if not updated:
        corrections.append(new_entry)

    write_corrections(corrections_path, corrections)
    action = "Updated" if updated else "Added"
    print(f"{action} correction: {image_path.name} -> {label}")
    print(f"sha256: {sha256}")
    print(f"corrections: {corrections_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
