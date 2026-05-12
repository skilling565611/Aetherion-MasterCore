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
FINAL_FOLDER = REPO_ROOT / "dist/AetherionImageTools"
EXE_NAME = "AetherionImageTools"
SOURCE_ONNX_FOLDER = PROJECT_DIR / "Models/ONNX"
SOURCE_ONNX_FALLBACK = PROJECT_DIR / "models/ONNX"


def remove_folder(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)


def copy_file_if_exists(source: Path, target: Path) -> None:
    if source.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def copy_folder_if_exists(source: Path, target: Path) -> None:
    """Copy an external editable folder into the portable EXE folder."""

    if source.exists():
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)


def source_onnx_folder() -> Path | None:
    """Find the source ONNX folder without depending on path casing."""

    if SOURCE_ONNX_FOLDER.exists():
        return SOURCE_ONNX_FOLDER
    if SOURCE_ONNX_FALLBACK.exists():
        return SOURCE_ONNX_FALLBACK
    return None


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
            "ai_model": "Models/ONNX/model.onnx",
            "ai_labels": "Models/ONNX/labels.json",
            "dry_run": True,
            "copy_only": True,
            "use_ai": True,
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
  Models/ONNX/
    Keep model.onnx, labels.json, config.json, and preprocessor_config.json here.
    This folder is copied from AI/ImageTools/Models/ONNX during the Control Prime build.

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


def write_run_first_readme(path: Path) -> None:
    text = """Aetherion ImageTools - Run First

1. Keep the Models/ONNX folder beside AetherionImageTools.exe.
2. Run dry-run first from the EXE menu.
3. Do not move or delete the Models folder.
4. If the classifier says ONNX missing, check:
   Models/ONNX/model.onnx

The EXE should not require Python on Arctic Prime.
Logs are written to the Logs folder beside the EXE.
Original images are never deleted, moved, or modified.
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
        FINAL_FOLDER / "Models/ONNX",
        FINAL_FOLDER / "Models/Lite",
        FINAL_FOLDER / "Models/Medium",
        FINAL_FOLDER / "Models/Heavy",
        FINAL_FOLDER / "Logs",
        FINAL_FOLDER / "Input",
        FINAL_FOLDER / "Output",
    ):
        folder.mkdir(parents=True, exist_ok=True)

    onnx_folder = source_onnx_folder()
    if onnx_folder is not None:
        copy_folder_if_exists(onnx_folder, FINAL_FOLDER / "Models/ONNX")
    if not (FINAL_FOLDER / "Models/ONNX/model.onnx").exists():
        print("WARNING: ONNX model was not found at AI/ImageTools/Models/ONNX/model.onnx")
        print("         The EXE was built, but AI mode needs Models/ONNX/model.onnx beside the EXE.")

    copy_file_if_exists(PROJECT_DIR / "README.md", FINAL_FOLDER / "ImageTools_README.md")
    copy_file_if_exists(PROJECT_DIR / "Training/README.md", FINAL_FOLDER / "Training/README.md")
    copy_file_if_exists(PROJECT_DIR / "Training/labels.json", FINAL_FOLDER / "Training/labels.json")
    write_readme(FINAL_FOLDER / "README.txt")
    write_run_first_readme(FINAL_FOLDER / "README_Run_First.txt")


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
