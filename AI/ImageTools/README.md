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

## Windows EXE Build

Use the PyInstaller build only on Control Prime. The EXE output is for testing on Arctic Prime without requiring Python to be installed there.

Before build, copy, push, or pull work, run the read-only Git preflight check:

```powershell
python AI/ImageTools/scripts/preflight_check.py
```

Strict mode returns a non-zero exit code when Git lock files or unfinished Git operations are found:

```powershell
python AI/ImageTools/scripts/preflight_check.py --strict
```

The preflight check only reports. It does not kill processes, edit files, clean the repo, or fix Git state.

Install the build requirement:

```powershell
python -m pip install -r AI/ImageTools/Requirements/build.txt
```

Build the portable folder:

```powershell
python AI/ImageTools/Build/build_exe.py
```

The final folder is written to:

```text
AI/ImageTools/Build/Aetherion_ImageTools/
```

The EXE keeps configs, corrections, training labels, logs, and output external beside the EXE. The build copies `AI/ImageTools/Models/ONNX` into `dist/AetherionImageTools/Models/ONNX` so Arctic Prime can run the ONNX classifier without a manual model install. Real copy mode asks for confirmation, and the organizer remains copy-only.

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
  --ai-model "AI/ImageTools/models/model_quantized.onnx" `
  --ai-labels "AI/ImageTools/models/rating_labels.quantized.json"
```

AI debug and safety switches:

```powershell
python AI/ImageTools/scripts/image_organizer.py `
  --config AI/ImageTools/Configs/default_config.json `
  --use-ai `
  --ai-debug-outputs `
  --force-review-on-suspicious-sfw
```

Use `--ai-flip-binary-labels` only for a two-class model when the SFW/NSFW labels are known to be reversed.

AI mode is optional. If AI dependencies or a local model are missing, the tool continues with keyword rules and Pillow heuristics and records the AI status in the JSON decision log. ONNX inference is forced to `CPUExecutionProvider` with one worker thread so it remains appropriate for Arctic Prime-style low-power hardware.

AI decision logs include raw ONNX outputs, softmax probabilities, model input/output tensor names and shapes, selected class index, selected label, and the loaded label mapping when `ai_debug_outputs` is enabled. If AI reports `SFW` but visual signals look suspicious and the filename has no clothing or safe keyword, `force_review_on_suspicious_sfw` sends the image to `Review_Needed` with reason `suspicious_sfw_ai_result`.

## Manual Corrections

Manual corrections let you teach ImageTools the correct label without retraining the ONNX model. This is lightweight, local, and better suited for Arctic Prime than model training.

Corrections live here:

```text
AI/ImageTools/Training/corrections.json
```

Add or update a correction:

```powershell
python AI/ImageTools/scripts/add_correction.py `
  --image "AI/PIX/example.jpeg" `
  --label "Explicit" `
  --previous-label "SFW" `
  --notes "wrong AI label"
```

Corrections match by SHA256 first. Filename matching is fallback only. A manual correction overrides AI, filename rules, and visual rules, and the decision log records:

```text
manual_correction_applied
manual_correct_label
manual_correction_reason
manual_previous_label
automated_rating_category
automated_confidence
automated_reason
```

This does not delete, move, or modify originals. Real retraining can be added later on Control Prime.

## Local AI Model Folder

Optional local AI model files go here:

```text
AI/ImageTools/models/
```

Current ONNX model path in `Configs/default_config.json`:

```text
AI/ImageTools/models/model_quantized.onnx
```

Expected labels file for the quantized model:

```text
AI/ImageTools/models/rating_labels.quantized.json
```

The prithivMLmods/Vit-Mature-Content-Detection style 5-label mapping is:

```text
0 = Anime Picture -> SFW
1 = Hentai -> Explicit
2 = Neutral -> SFW
3 = Pornography -> Explicit
4 = Enticing or Sensual -> Suggestive
```

`Review_Needed` is never a direct model label. It is only a fallback when the layered organizer cannot make a safe final decision.

An 8-category example labels file is also included:

```text
AI/ImageTools/models/rating_labels.example.json
```

AI mode is optional and disabled by default in `Configs/default_config.json`. ImageTools still runs without `model_quantized.onnx` or `rating_labels.quantized.json`; it falls back to filename rules and Pillow-based local analysis.

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

1. Manual correction by SHA256.
2. Strong filename and folder rules.
3. Optional general ONNX mature-content classifier when enabled, installed, and configured with a local model.
4. Furry/anthro rule refinement.
5. Low-confidence or unclear results fall back to `Review_Needed`.

Visual uncertainty can override safe-looking filenames. The Pillow stage is intentionally conservative; it does not claim to detect nudity directly. SFW vs NSFW decisions follow the project rule: clothed, underwear, and lingerie images stay `SFW`, `Suggestive`, or `Lingerie` unless private body parts are clearly exposed; unclear images go to `Review_Needed`.

Raw model labels are logged separately from final organizer labels. This keeps the ONNX output inspectable while allowing local rules and corrections to produce the final folder label.

## Furry/Anthro Classifier Roadmap

ImageTools now uses a layered classifier architecture for Aetherion character images:

- Current system: general ONNX model + filename/folder rules + furry/anthro rules + manual corrections.
- Manual corrections teach the organizer locally by SHA256 before any future model training exists.
- Future training can use corrected examples from `AI/ImageTools/Training/corrections.json`.
- Arctic Prime should use Lite mode: dry-run, copy-only, rules, corrections, and exported ONNX inference.
- Control Prime should run Medium/Heavy testing and future training experiments.

The furry/anthro layer is lightweight and rule-based. It checks filename/folder context for anthro/furry terms, ears, tails, fur/body clues, outfit and lingerie terms, exposed/nude terms, cyberpunk/neon style hints, and character hints such as `Nyra_Vale`.

Decision logs include:

```text
furry_rules_applied
furry_rule_score
furry_detected
outfit_hint
exposure_hint
species_hint
character_hint
final_layer_used
raw_model_label
raw_model_category
final_organizer_label
```

Future custom classifier hooks are intentionally placeholders only. Do not train a model here yet, do not install `torch` by default, and do not commit large model files.

## Future Training Data Pipeline

Training data lives under:

```text
AI/ImageTools/Training/
```

The dataset builder reads `Training/corrections.json`, matches corrected images by SHA256, copies examples into `Training/Dataset/CATEGORY/`, and writes `dataset_manifest.json`. It never deletes originals, never moves originals, preserves original filenames in the manifest, and uses duplicate-safe copied names.

Run it from the repository root:

```powershell
python AI/ImageTools/Training/dataset_builder.py
```

Training itself is not implemented yet. Later, Control Prime can train a custom Aetherion/furry/anthro-aware classifier and export it to ONNX. The packaged EXE should use that exported ONNX model rather than including heavy training dependencies.

## Outputs

Folder example:

```text
AI/Perchance/IMG/Nyra_Vale/
|-- SFW/
|-- Suggestive/
|-- Lingerie/
|-- Partial_Nude/
|-- Nude/
|-- Explicit/
|-- Unknown/
`-- Review_Needed/
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
