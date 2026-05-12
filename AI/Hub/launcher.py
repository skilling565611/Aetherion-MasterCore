from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


# This hub intentionally uses only the Python standard library. It is meant to
# be a small Windows-friendly launcher for Arctic Prime, not a heavy tool app.
REPO_ROOT = Path(__file__).resolve().parents[2]
IMAGE_TOOLS = REPO_ROOT / "AI/ImageTools"
SCRIPTS = IMAGE_TOOLS / "scripts"
CONFIG = IMAGE_TOOLS / "Configs/default_config.json"
LOGS = IMAGE_TOOLS / "Logs"
MODELS = IMAGE_TOOLS / "models"
TRAINING = IMAGE_TOOLS / "Training"
MODEL_FILE = MODELS / "model_quantized.onnx"
LABELS_FILE = MODELS / "rating_labels.quantized.json"
CORRECTIONS_FILE = TRAINING / "corrections.json"
RATING_LABELS = (
    "SFW",
    "Suggestive",
    "Lingerie",
    "Partial_Nude",
    "Nude",
    "Explicit",
    "Unknown",
    "Review_Needed",
)


def print_header() -> None:
    print("")
    print("Aetherion AI Tools Hub")
    print("=====================")
    print("Dry-run is the safest default. ImageTools is copy-only and never deletes originals.")
    print("")


def run_command(command: list[str], wait: bool = True) -> None:
    print("")
    print("Running:")
    print(" ".join(command))
    print("")
    if wait:
        subprocess.run(command, cwd=REPO_ROOT, check=False)
    else:
        subprocess.Popen(command, cwd=REPO_ROOT)


def run_dry() -> None:
    print("Starting ImageTools dry run. This writes logs only and does not copy files.")
    run_command([sys.executable, str(SCRIPTS / "run_dry.py")])


def run_real_copy() -> None:
    print("Real copy mode copies images into organized output folders.")
    print("It still does not delete, move, or modify originals.")
    answer = input("Type COPY to confirm real copy mode, or press Enter to cancel: ").strip()
    if answer != "COPY":
        print("Canceled real copy mode.")
        return

    # The default config is intentionally dry_run=true, so real copy mode calls
    # the organizer directly with explicit safe paths and no --dry-run flag.
    run_command(
        [
            sys.executable,
            str(SCRIPTS / "image_organizer.py"),
            "--source",
            "AI/PIX",
            "--output",
            "AI/Perchance/IMG",
            "--character",
            "Nyra_Vale",
            "--copy-only",
            "--confidence-threshold",
            "0.70",
            "--review-uncertain",
        ]
    )


def open_logs() -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    print(f"Opening logs folder: {LOGS}")
    if os.name == "nt":
        os.startfile(LOGS)  # type: ignore[attr-defined]
    else:
        run_command(["python", "-c", f"print(r'{LOGS}')"])


def check_requirements() -> None:
    print("Checking ImageTools requirements. This does not install anything unless setup_env.py flags are used manually.")
    run_command([sys.executable, str(SCRIPTS / "setup_env.py")])


def open_image_gui() -> None:
    script = SCRIPTS / "image_gui.py"
    if not script.exists():
        print("ImageTools GUI script is not available yet.")
        return
    print("Opening ImageTools GUI. Close its terminal window or press Ctrl+C there when finished.")
    run_command([sys.executable, str(script)], wait=False)


def show_model_folder() -> None:
    MODELS.mkdir(parents=True, exist_ok=True)
    print("")
    print("ONNX model folder:")
    print("AI/ImageTools/models/")
    print("")
    print("Expected ONNX model file:")
    print("AI/ImageTools/models/model_quantized.onnx")
    print("")
    print("Expected labels file:")
    print("AI/ImageTools/models/rating_labels.quantized.json")
    print("")
    print(f"Full folder path: {MODELS}")
    print(f"Full model path: {MODEL_FILE}")
    print(f"Full labels path: {LABELS_FILE}")
    print("")
    print("AI mode is optional and disabled by default. The organizer works without these files.")


def add_manual_correction() -> None:
    print("")
    print("Add ImageTools Manual Correction")
    print("--------------------------------")
    print("This records a local JSON override. It does not edit, move, or delete the image.")
    print("")
    image_path = input("Image path: ").strip().strip('"')
    if not image_path:
        print("Canceled: image path is required.")
        return

    print("")
    print("Valid labels:")
    for label in RATING_LABELS:
        print(f"- {label}")
    print("")
    label = input("Correct label: ").strip()
    if label not in RATING_LABELS:
        print(f"Canceled: '{label}' is not a valid label.")
        return

    previous_label = input("Previous label, if known: ").strip()
    notes = input("Notes: ").strip()
    run_command(
        [
            sys.executable,
            str(SCRIPTS / "add_correction.py"),
            "--image",
            image_path,
            "--label",
            label,
            "--previous-label",
            previous_label,
            "--notes",
            notes,
            "--corrections",
            str(CORRECTIONS_FILE),
        ]
    )


def menu() -> None:
    while True:
        print_header()
        print("1. Run ImageTools dry run")
        print("2. Run ImageTools real copy mode")
        print("3. Open ImageTools logs folder")
        print("4. Check ImageTools requirements")
        print("5. Open ImageTools GUI if available")
        print("6. Show ONNX model folder path")
        print("7. Add ImageTools manual correction")
        print("8. Exit")
        print("")
        choice = input("Choose an option, or press Enter for dry run: ").strip() or "1"

        if choice == "1":
            run_dry()
        elif choice == "2":
            run_real_copy()
        elif choice == "3":
            open_logs()
        elif choice == "4":
            check_requirements()
        elif choice == "5":
            open_image_gui()
        elif choice == "6":
            show_model_folder()
        elif choice == "7":
            add_manual_correction()
        elif choice == "8":
            print("Exiting AI Tools Hub.")
            return
        else:
            print("Unknown option. Choose 1 through 8.")

        input("\nPress Enter to return to the hub menu...")


if __name__ == "__main__":
    menu()
