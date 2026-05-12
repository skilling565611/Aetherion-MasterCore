from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
PROJECT_DIR = REPO_ROOT / "AI/ImageTools"

if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from image_organizer import organize_images  # noqa: E402


def running_as_exe() -> bool:
    return bool(getattr(sys, "frozen", False))


def app_root() -> Path:
    """Return the folder that owns the editable EXE-side files."""

    if running_as_exe():
        return Path(sys.executable).resolve().parent
    return PROJECT_DIR


def model_source_root() -> Path:
    """Return the preferred ONNX model folder for this run mode."""

    if running_as_exe():
        return app_root() / "Models/ONNX"
    return PROJECT_DIR / "Models/ONNX"


def config_path() -> Path:
    root = app_root()
    if running_as_exe():
        return root / "Configs/default_config.json"
    return PROJECT_DIR / "Configs/default_config.json"


def resolve_app_path(value: str | Path | None, fallback: Path) -> Path:
    """Resolve paths relative to the EXE folder or repository root.

    Source runs keep the existing repo-relative behavior. Frozen EXE runs use
    the EXE folder as the base so configs, models, corrections, and logs stay
    editable beside the portable build.
    """

    if value in (None, ""):
        return fallback
    path = Path(value)
    if path.is_absolute():
        return path

    if running_as_exe():
        text = path.as_posix()
        exe_root = app_root()
        remaps = {
            "AI/ImageTools/Configs/default_config.json": exe_root / "Configs/default_config.json",
            "AI/ImageTools/Training/corrections.json": exe_root / "Training/corrections.json",
            "AI/ImageTools/Models/ONNX/model.onnx": exe_root / "Models/ONNX/model.onnx",
            "AI/ImageTools/Models/ONNX/labels.json": exe_root / "Models/ONNX/labels.json",
            "AI/ImageTools/models/model_quantized.onnx": exe_root / "Models/Lite/model_quantized.onnx",
            "AI/ImageTools/models/rating_labels.quantized.json": exe_root / "Models/Lite/rating_labels.quantized.json",
            "AI/ImageTools/Logs": exe_root / "Logs",
        }
        return remaps.get(text, exe_root / path)

    return REPO_ROOT / path


def load_config() -> dict[str, Any]:
    path = config_path()
    if not path.exists():
        raise SystemExit(f"Config file was not found: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise SystemExit(f"Config file must contain a JSON object: {path}")
    return payload


def organizer_paths(config: dict[str, Any]) -> dict[str, Path]:
    root = app_root()
    return {
        "source": resolve_app_path(config.get("source", "Input"), root / "Input"),
        "output": resolve_app_path(config.get("output", "Output"), root / "Output"),
        "log_dir": resolve_app_path(config.get("log_dir", "Logs"), root / "Logs"),
        "ai_model": resolve_app_path(config.get("ai_model", "Models/ONNX/model.onnx"), model_source_root() / "model.onnx"),
        "ai_labels": resolve_app_path(config.get("ai_labels", "Models/ONNX/labels.json"), model_source_root() / "labels.json"),
        "corrections": resolve_app_path(config.get("corrections", "Training/corrections.json"), root / "Training/corrections.json"),
    }


def run_organizer(force_dry_run: bool) -> None:
    config = load_config()
    paths = organizer_paths(config)
    copy_only = bool(config.get("copy_only", True))
    if not copy_only:
        raise SystemExit("Config copy_only must stay true. ImageTools never moves or deletes originals.")

    print()
    print("Aetherion ImageTools")
    print(f"Config: {config_path()}")
    print(f"Source: {paths['source']}")
    print(f"Output: {paths['output']}")
    print(f"Logs:   {paths['log_dir']}")
    print(f"ONNX:   {paths['ai_model']} [{'found' if paths['ai_model'].exists() else 'missing'}]")
    print(f"Mode:   {'DRY RUN' if force_dry_run else 'COPY'}")
    print()

    if not force_dry_run:
        print("Copy mode will copy images into the output folder.")
        print("Originals will not be moved, deleted, or modified.")
        confirm = input("Type COPY to continue: ").strip()
        if confirm != "COPY":
            print("Copy mode cancelled.")
            return

    _results, report_paths = organize_images(
        source_dir=paths["source"],
        output_root=paths["output"],
        character=str(config.get("character", "Nyra_Vale")),
        recursive=bool(config.get("recursive", True)),
        dry_run=True if force_dry_run else bool(config.get("dry_run", False)),
        copy_only=True,
        confidence_threshold=float(config.get("confidence_threshold", 0.7)),
        review_uncertain=bool(config.get("review_uncertain", True)),
        use_ai=bool(config.get("use_ai", False)),
        ai_model=paths["ai_model"],
        ai_labels=paths["ai_labels"],
        ai_model_load_mode="packaged_exe" if running_as_exe() else "source",
        ai_flip_binary_labels=bool(config.get("ai_flip_binary_labels", False)),
        ai_debug_outputs=bool(config.get("ai_debug_outputs", False)),
        force_review_on_suspicious_sfw=bool(config.get("force_review_on_suspicious_sfw", True)),
        suspicious_skin_ratio_threshold=float(config.get("suspicious_skin_ratio_threshold", 0.16)),
        suspicious_bright_ratio_threshold=float(config.get("suspicious_bright_ratio_threshold", 0.45)),
        corrections_path=paths["corrections"],
        log_dir=paths["log_dir"],
        rename=bool(config.get("rename", True)),
        known_characters=list(config.get("known_characters", [])) if isinstance(config.get("known_characters", []), list) else [],
        debug=bool(config.get("debug", False)),
    )

    print("Run complete. Originals were never deleted, moved, or modified.")
    for label, path in report_paths.items():
        print(f"{label}: {path}")


def open_logs_folder() -> None:
    config = load_config()
    logs = organizer_paths(config)["log_dir"]
    logs.mkdir(parents=True, exist_ok=True)
    os.startfile(logs)  # type: ignore[attr-defined]


def check_paths() -> None:
    config = load_config()
    paths = organizer_paths(config)
    print()
    print("Path check")
    print(f"EXE/source root: {app_root()}")
    print(f"Config: {config_path()} [{'OK' if config_path().exists() else 'MISSING'}]")
    for label, path in paths.items():
        status = "OK" if path.exists() else "MISSING"
        print(f"{label}: {path} [{status}]")
    print()
    print("Keep Models/ONNX beside the EXE. Expected model file: Models/ONNX/model.onnx")
    if not paths["ai_model"].exists():
        print("ONNX missing: put model.onnx in Models/ONNX before enabling AI mode.")


def pause() -> None:
    input("\nPress Enter to return to the menu...")


def main() -> int:
    while True:
        print()
        print("Aetherion ImageTools")
        print("1. Run dry-run")
        print("2. Run organizer copy mode")
        print("3. Open logs folder")
        print("4. Check model/config paths")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                run_organizer(force_dry_run=True)
                pause()
            elif choice == "2":
                run_organizer(force_dry_run=False)
                pause()
            elif choice == "3":
                open_logs_folder()
            elif choice == "4":
                check_paths()
                pause()
            elif choice == "5":
                return 0
            else:
                print("Please choose 1, 2, 3, 4, or 5.")
        except Exception as error:
            print(f"Error: {error}")
            pause()


if __name__ == "__main__":
    raise SystemExit(main())
