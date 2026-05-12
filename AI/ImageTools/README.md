# AI Image Tools

Lightweight local image organizer for Aetherion character assets. It is built for low-power CPU-only systems like Arctic Prime and does not use online APIs, cloud services, or GPU features.

Original files are never deleted, moved, overwritten, or modified. The organizer only copies images with duplicate-safe target names.

## Install

The rating pipeline uses Pillow for basic local image analysis:

```powershell
python -m pip install Pillow
```

If Pillow is missing, the tool still runs, but visual classification is skipped and uncertain images go to `Review_Needed`.

Optional local AI mode uses CPU-only ONNX Runtime when you provide a local model and labels file:

```powershell
python -m pip install ".[ai]"
```

## Requirements + Runner Setup

The existing `pyproject.toml` setup is still the main project setup. From the repository root, install ImageTools in editable mode with:

```powershell
python -m pip install -e AI/ImageTools
```

Optional CPU-only AI dependencies can be installed with:

```powershell
python -m pip install -e "AI/ImageTools[ai]"
```

You can also install from the beginner-friendly requirements files:

```powershell
python -m pip install -r AI/ImageTools/Requirements/image.txt
```

The requirements files are split so add-ons are easy to remove or reinstall later:

```text
AI/ImageTools/Requirements/base.txt
AI/ImageTools/Requirements/image.txt
AI/ImageTools/Requirements/ai-optional.txt
AI/ImageTools/Requirements/dev.txt
```

Check the environment and create the expected folders without installing anything:

```powershell
python AI/ImageTools/scripts/setup_env.py
```

Open the beginner setup GUI:

```powershell
python AI/ImageTools/scripts/setup_gui.py
```

The setup GUI opens at:

```text
http://127.0.0.1:8767/
```

It shows the active Python executable, dependency status, required folders, and install buttons. Install buttons require the approval checkbox before they run pip, so packages are not installed automatically. Run it with `AI/ImageTools/.venv/Scripts/python.exe` when you want all add-ons to stay inside the removable ImageTools venv.

Install only the pieces you explicitly ask for:

```powershell
python AI/ImageTools/scripts/setup_env.py --install-base --install-image
python AI/ImageTools/scripts/setup_env.py --install-ai
python AI/ImageTools/scripts/setup_env.py --install-dev
python AI/ImageTools/scripts/setup_env.py --install-project
```

`setup_env.py` does not auto-install heavy AI packages. Arctic Prime should avoid `torch`, `transformers`, `tensorflow`, and similar heavy stacks by default.

The default runner config lives here:

```text
AI/ImageTools/Configs/default_config.json
```

Edit that file to change the source folder, output folder, character name, dry-run setting, AI setting, confidence threshold, recursion, and debug output.

The safest first test is dry-run mode:

```powershell
python AI/ImageTools/scripts/run_dry.py
```

`run_dry.py` forces `dry_run=true` and `copy_only=true`. It scans images and writes JSON logs, but it does not copy, move, delete, or modify originals.

Run the organizer from the config file:

```powershell
python AI/ImageTools/scripts/run_organizer.py
```

`run_organizer.py` respects `dry_run`, `copy_only`, `use_ai`, and the other values in `Configs/default_config.json`. It refuses move/delete behavior because originals must never be deleted or modified.

The main CLI can also read a config directly:

```powershell
python AI/ImageTools/scripts/image_organizer.py --config AI/ImageTools/Configs/default_config.json
```

Config values load first, then command-line flags override them.

## Command Line

Preview a run:

```powershell
python AI/ImageTools/scripts/image_organizer.py `
  --source "AI/PIX" `
  --output "AI/Perchance/IMG" `
  --character "Nyra_Vale" `
  --dry-run `
  --debug
```

Copy images into rating folders:

```powershell
python AI/ImageTools/scripts/image_organizer.py `
  --source "AI/PIX" `
  --output "AI/Perchance/IMG" `
  --character "Nyra_Vale"
```

Optional local AI hook:

```powershell
python AI/ImageTools/scripts/image_organizer.py `
  --source "AI/PIX" `
  --output "AI/Perchance/IMG" `
  --character "Nyra_Vale" `
  --use-ai `
  --ai-model "AI/ImageTools/models/rating_model.onnx" `
  --ai-labels "AI/ImageTools/models/rating_labels.json"
```

AI mode is optional. If AI dependencies or a local model are missing, the tool continues with keyword rules and Pillow heuristics and records the AI status in the JSON decision log. ONNX inference is forced to `CPUExecutionProvider` with one worker thread so it remains appropriate for Arctic Prime-style low-power hardware.

## Local AI Model Folder

Optional local AI model files go here:

```text
AI/ImageTools/models/
```

Current ONNX model path in `Configs/default_config.json`:

```text
AI/ImageTools/models/model_q4f16.onnx
```

Expected labels file:

```text
AI/ImageTools/models/rating_labels.json
```

An example labels file is included:

```text
AI/ImageTools/models/rating_labels.example.json
```

AI mode is optional and disabled by default in `Configs/default_config.json`. ImageTools still runs without `rating_model.onnx` or `rating_labels.json`; it falls back to filename rules and Pillow-based local analysis.

Do not commit large model files unless intentionally needed. Actual `.onnx` files are ignored by the local ImageTools `.gitignore` so Arctic Prime can keep model files local.

## Rating Categories

- `SFW`: clothed, ordinary, or low-risk visual signal where private body parts are not clearly exposed.
- `Suggestive`: mild adult framing or medium skin-like color signal without clear explicit exposure.
- `Lingerie`: underwear, lingerie, swimsuit, or similar signal without clear explicit exposure.
- `Partial_Nude`: partial nudity wording or uncertain adult visual signal that should be handled carefully.
- `Nude`: filename/folder or local AI model indicates full nudity.
- `Explicit`: filename/folder or local AI model indicates explicit sexual content.
- `Unknown`: not enough signal to classify.
- `Review_Needed`: unclear, low-confidence, missing Pillow analysis, or visual signal needs human review.

## Decision Flow

1. Filename and folder keyword rules.
2. Basic Pillow analysis using tiny thumbnails and color ratios.
3. Optional local AI classifier hook when enabled, installed, and configured with a local model.
4. Low-confidence results fall back to `Review_Needed`.

Visual uncertainty can override safe-looking filenames. The Pillow stage is intentionally conservative; it does not claim to detect nudity directly. SFW vs NSFW decisions follow the project rule: clothed, underwear, and lingerie images stay `SFW`, `Suggestive`, or `Lingerie` unless private body parts are clearly exposed; unclear images go to `Review_Needed`.

## Outputs

Folder example:

```text
AI/Perchance/IMG/Nyra_Vale/
├── SFW/
├── Suggestive/
├── Lingerie/
├── Partial_Nude/
├── Nude/
├── Explicit/
├── Unknown/
└── Review_Needed/
```

JSON logs are written to:

```text
AI/ImageTools/Logs/
```

Reports:

```text
scan_report.json
review_needed.json
duplicate_report.json
rating_summary.json
decision_log.json
```

Every decision logs original path, output path, filename, detected character, rating category, confidence, AI usage, matched rules, reason, timestamp, and duplicate status.

## GUI

The browser GUI is still available:

```powershell
AI/AudioTools/.venv/Scripts/python.exe AI/ImageTools/scripts/image_gui.py
```

It opens at:

```text
http://127.0.0.1:8766/
```

The GUI calls the same copy-only organizer logic as the command-line tool.

GUI controls include dry-run, recursive scan, clean renaming, optional local AI, review threshold, and `Review_Needed` fallback for uncertain ratings.
