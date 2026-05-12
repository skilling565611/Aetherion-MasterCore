# ImageTools Training Data

This folder stores lightweight local corrections for images the organizer rated incorrectly and turns those corrections into a future training dataset.

Corrections are the first training layer. They do not retrain the ONNX model yet. They are a local override layer that is much lighter and safer for Arctic Prime:

- SHA256 matches are strongest.
- Filename matches are fallback only.
- Manual labels override AI, filename rules, and visual rules.
- Originals are never deleted, moved, or modified.
- Dry-run remains safe.

Add a correction from the repository root:

```powershell
python AI/ImageTools/scripts/add_correction.py `
  --image "AI/PIX/example.jpeg" `
  --label "Explicit" `
  --previous-label "SFW" `
  --notes "wrong AI label"
```

The organizer reads:

```text
AI/ImageTools/Training/corrections.json
```

Build the future dataset from corrected examples:

```powershell
python AI/ImageTools/Training/dataset_builder.py
```

The dataset builder:

- Reads `Training/corrections.json`.
- Finds corrected images by SHA256.
- Copies examples into `Training/Dataset/CATEGORY/`.
- Preserves the original filename in `dataset_manifest.json`.
- Uses duplicate-safe copied names.
- Never deletes, moves, or modifies originals.

Actual model training is not implemented yet. Training should happen later on Control Prime, not Arctic Prime. The future export target is ONNX, and the packaged EXE should use that exported ONNX model instead of shipping a training stack.

Future placeholders:

- `train_custom_classifier.py`
- `export_to_onnx.py`

Keep model files local unless explicitly requested.
