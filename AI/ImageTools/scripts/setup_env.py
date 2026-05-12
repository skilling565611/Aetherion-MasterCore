from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PROJECT_DIR = REPO_ROOT / "AI/ImageTools"
REQUIREMENTS_DIR = PROJECT_DIR / "Requirements"
CONFIGS_DIR = PROJECT_DIR / "Configs"
LOGS_DIR = PROJECT_DIR / "Logs"
MODELS_DIR = PROJECT_DIR / "models"


DEPENDENCY_CHECKS = (
    ("Pillow", "PIL", "AI/ImageTools/Requirements/image.txt"),
    ("ImageHash", "imagehash", "AI/ImageTools/Requirements/image.txt"),
    ("numpy", "numpy", "AI/ImageTools/Requirements/ai-optional.txt"),
    ("onnxruntime", "onnxruntime", "AI/ImageTools/Requirements/ai-optional.txt"),
)


def run_command(command: list[str]) -> None:
    """Run a pip command with the current Python executable.

    Using sys.executable keeps installs inside the active venv when this script
    is run from AI/ImageTools/.venv or another project environment.
    """

    print(f"Running: {' '.join(command)}")
    subprocess.check_call(command, cwd=REPO_ROOT)


def ensure_folders() -> None:
    """Create beginner-friendly project folders if they are missing."""

    for folder in (REQUIREMENTS_DIR, CONFIGS_DIR, LOGS_DIR, MODELS_DIR):
        folder.mkdir(parents=True, exist_ok=True)
        print(f"OK folder: {folder}")


def check_python() -> None:
    print(f"Python: {sys.version.split()[0]}")
    if sys.version_info < (3, 10):
        print("WARNING: ImageTools expects Python 3.10 or newer.")
    else:
        print("OK Python version is new enough.")


def check_pip() -> bool:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "--version"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode == 0:
        print(f"OK pip: {result.stdout.strip()}")
        return True
    print("MISSING pip. Install or repair pip before installing requirements.")
    return False


def check_dependencies() -> None:
    """Show dependency status without installing anything automatically."""

    missing: list[tuple[str, str]] = []
    for display_name, import_name, requirement_file in DEPENDENCY_CHECKS:
        if importlib.util.find_spec(import_name):
            print(f"OK dependency: {display_name}")
        else:
            print(f"MISSING dependency: {display_name}")
            missing.append((display_name, requirement_file))

    if not missing:
        print("All checked ImageTools dependencies are available.")
        return

    print("")
    print("Install suggestions:")
    print("  python -m pip install -e AI/ImageTools")
    print("  python -m pip install -r AI/ImageTools/Requirements/image.txt")
    print("  python -m pip install -r AI/ImageTools/Requirements/ai-optional.txt")
    print('  python -m pip install -e "AI/ImageTools[ai]"')
    print("")
    print("Nothing was installed because install flags were not requested.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check or install the lightweight ImageTools environment.")
    parser.add_argument("--install-base", action="store_true", help="Install AI/ImageTools/Requirements/base.txt")
    parser.add_argument("--install-image", action="store_true", help="Install Pillow and ImageHash requirements.")
    parser.add_argument("--install-ai", action="store_true", help="Install optional CPU-only AI requirements.")
    parser.add_argument("--install-dev", action="store_true", help="Install developer requirements.")
    parser.add_argument("--install-project", action="store_true", help="Install the pyproject package in editable mode.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ensure_folders()
    check_python()
    pip_ready = check_pip()

    if not pip_ready:
        return 1

    # These install only when the user explicitly asks. Heavy AI packages such
    # as torch, transformers, tensorflow, and opencv-python are intentionally
    # not installed by this script.
    if args.install_base:
        run_command([sys.executable, "-m", "pip", "install", "-r", "AI/ImageTools/Requirements/base.txt"])
    if args.install_image:
        run_command([sys.executable, "-m", "pip", "install", "-r", "AI/ImageTools/Requirements/image.txt"])
    if args.install_ai:
        run_command([sys.executable, "-m", "pip", "install", "-r", "AI/ImageTools/Requirements/ai-optional.txt"])
        print('Optional equivalent: python -m pip install -e "AI/ImageTools[ai]"')
    if args.install_dev:
        run_command([sys.executable, "-m", "pip", "install", "-r", "AI/ImageTools/Requirements/dev.txt"])
    if args.install_project:
        run_command([sys.executable, "-m", "pip", "install", "-e", "AI/ImageTools"])

    check_dependencies()
    print("Setup check complete. Originals are never modified by setup.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
