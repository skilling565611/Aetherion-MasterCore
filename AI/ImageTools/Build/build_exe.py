from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PROJECT_DIR = REPO_ROOT / "AI/ImageTools"
BUILD_DIR = PROJECT_DIR / "Build"
ENTRY_POINT = PROJECT_DIR / "scripts/exe_launcher.py"
PYINSTALLER_DIST = BUILD_DIR / "PyInstallerDist"
PYINSTALLER_WORK = BUILD_DIR / "PyInstallerWork"
FINAL_FOLDER = BUILD_DIR / "Aetherion_ImageTools"
EXE_NAME = "AetherionImageTools"


def remove_folder(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)


def copy_file_if_exists(source: Path, target: Path) -> None:
    if source.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def write_exe_config(source_config: Path, target_config: Path) -> None:
    """Create an editable EXE-side config with portable relative paths."""

    config = json.loads(source_config.read_text(encoding="utf-8")) if source_config.exists() else {}
    if not isinstance(config, dict):
        config = {}

    config.update(
        {
            "source": "Input",
            "output": "Output",
            "log_dir": "Logs",
            "corrections": "Training/corrections.json",
            "ai_model": "Models/Lite/model_quantized.onnx",
            "ai_labels": "Models/Lite/rating_labels.quantized.json",
            "dry_run": True,
            "copy_only": True,
            "use_ai": False,
        }
    )
    target_config.parent.mkdir(parents=True, exist_ok=True)
    target_config.write_text(json.dumps(config, indent=2), encoding="utf-8")


def write_readme(path: Path) -> None:
    text = """Aetherion ImageTools EXE

This folder is a portable Windows test build for Arctic Prime.

Start:
  AetherionImageTools.exe

Folders:
  Configs/default_config.json
    Editable settings for source, output, AI mode, model paths, and dry-run.

  Models/Lite/
  Models/Medium/
  Models/Heavy/
    Put external ONNX model files and label JSON files here.
    Large model files are not bundled inside the EXE.

  Training/corrections.json
    Editable local manual corrections. Keep this file with the EXE folder.

  Logs/
    JSON reports are written here beside the EXE.

Safety:
  Dry-run is kept.
  Copy-only safety is kept.
  Originals are never deleted, moved, or modified.
  Real copy mode asks for confirmation before running.

Notes:
  Arctic Prime does not need Python installed to run this EXE.
  Build this package on Control Prime with PyInstaller.
"""
    path.write_text(text, encoding="utf-8")


def run_pyinstaller() -> None:
    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--onedir",
        "--console",
        "--name",
        EXE_NAME,
        "--distpath",
        str(PYINSTALLER_DIST),
        "--workpath",
        str(PYINSTALLER_WORK),
        "--specpath",
        str(BUILD_DIR),
        str(ENTRY_POINT),
    ]
    subprocess.run(command, cwd=REPO_ROOT, check=True)


def create_final_folder() -> None:
    pyinstaller_output = PYINSTALLER_DIST / EXE_NAME
    if not pyinstaller_output.exists():
        raise SystemExit(f"PyInstaller output was not found: {pyinstaller_output}")

    remove_folder(FINAL_FOLDER)
    shutil.copytree(pyinstaller_output, FINAL_FOLDER)

    write_exe_config(
        PROJECT_DIR / "Configs/default_config.json",
        FINAL_FOLDER / "Configs/default_config.json",
    )
    copy_file_if_exists(
        PROJECT_DIR / "Training/corrections.json",
        FINAL_FOLDER / "Training/corrections.json",
    )
    if not (FINAL_FOLDER / "Training/corrections.json").exists():
        (FINAL_FOLDER / "Training").mkdir(parents=True, exist_ok=True)
        (FINAL_FOLDER / "Training/corrections.json").write_text('{"corrections": []}\n', encoding="utf-8")

    for folder in (
        FINAL_FOLDER / "Models/Lite",
        FINAL_FOLDER / "Models/Medium",
        FINAL_FOLDER / "Models/Heavy",
        FINAL_FOLDER / "Logs",
        FINAL_FOLDER / "Input",
        FINAL_FOLDER / "Output",
    ):
        folder.mkdir(parents=True, exist_ok=True)

    copy_file_if_exists(PROJECT_DIR / "README.md", FINAL_FOLDER / "ImageTools_README.md")
    copy_file_if_exists(PROJECT_DIR / "Training/README.md", FINAL_FOLDER / "Training/README.md")
    write_readme(FINAL_FOLDER / "README.txt")


def main() -> int:
    if not ENTRY_POINT.exists():
        raise SystemExit(f"EXE launcher was not found: {ENTRY_POINT}")

    print("Cleaning old ImageTools build output...")
    remove_folder(PYINSTALLER_DIST)
    remove_folder(PYINSTALLER_WORK)
    remove_folder(FINAL_FOLDER)

    print("Running PyInstaller...")
    run_pyinstaller()

    print("Creating portable Aetherion_ImageTools folder...")
    create_final_folder()

    print()
    print("Build complete.")
    print(f"Final output: {FINAL_FOLDER}")
    print("Copy this folder to Arctic Prime for testing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

