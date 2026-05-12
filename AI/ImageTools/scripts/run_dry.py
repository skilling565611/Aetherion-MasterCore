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

    # Dry-run is forced here. This runner is the safest first test: it scans and
    # writes JSON logs, but it never copies, moves, deletes, or modifies images.
    source = repo_path(str(config.get("source", "AI/PIX")), REPO_ROOT / "AI/PIX")
    output = repo_path(str(config.get("output", "AI/Perchance/IMG")), REPO_ROOT / "AI/Perchance/IMG")
    log_dir = repo_path(str(config.get("log_dir", "AI/ImageTools/Logs")), DEFAULT_LOG_DIR)
    ai_model = repo_path(str(config.get("ai_model", "")), PROJECT_DIR / "models/rating_model.onnx")
    ai_labels = repo_path(str(config.get("ai_labels", "")), PROJECT_DIR / "models/rating_labels.json")

    print("ImageTools dry-run")
    print(f"Source: {source}")
    print(f"Output preview: {output}")
    print("dry_run: true")
    print("copy_only: true")

    _results, report_paths = organize_images(
        source_dir=source,
        output_root=output,
        character=str(config.get("character", "Nyra_Vale")),
        recursive=bool(config.get("recursive", True)),
        dry_run=True,
        copy_only=True,
        confidence_threshold=float(config.get("confidence_threshold", 0.7)),
        review_uncertain=bool(config.get("review_uncertain", True)),
        use_ai=bool(config.get("use_ai", False)),
        ai_model=ai_model,
        ai_labels=ai_labels,
        log_dir=log_dir,
        debug=bool(config.get("debug", True)),
    )

    print("Dry-run complete. No files were copied or modified.")
    for label, path in report_paths.items():
        print(f"{label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
