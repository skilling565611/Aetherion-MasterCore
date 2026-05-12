# Aetherion AI Tools Hub

The hub is a lightweight launcher for project tools. It is made for Arctic Prime, the low-power Windows laptop used for verification and recovery work.

Run it from the repository root:

```powershell
python AI/Hub/launcher.py
```

The hub starts ImageTools without needing to remember long commands. It can:

- run the recommended ImageTools dry-run
- run real copy mode after confirmation
- open the ImageTools logs folder
- check ImageTools requirements
- open the ImageTools browser GUI when available
- show the local ONNX model folder paths
- add a manual ImageTools correction without remembering the full command

Dry-run mode is safest. It scans images and writes JSON logs without copying, moving, deleting, or modifying originals.

The hub does not install heavy AI automatically. It does not add `torch`, `transformers`, `tensorflow`, cloud APIs, online AI services, or large model files.

Optional AI mode requires the user to place a local ONNX model in:

```text
AI/ImageTools/models/
```

Expected files:

```text
AI/ImageTools/models/model_quantized.onnx
AI/ImageTools/models/rating_labels.quantized.json
```

ImageTools still works without those files because AI mode is optional and disabled by default.

Manual corrections are stored locally in:

```text
AI/ImageTools/Training/corrections.json
```

The hub prompts for image path, correct label, previous label, and notes, then calls `AI/ImageTools/scripts/add_correction.py`. Corrections override AI/rules during future organizer runs, but they do not modify the original image.
