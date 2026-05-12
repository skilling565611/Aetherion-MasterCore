# ImageTools Local AI Models

This folder is for optional local AI model files used by ImageTools.

Current local model file:

```text
AI/ImageTools/models/model_q4f16.onnx
```

Expected labels file:

```text
AI/ImageTools/models/rating_labels.json
```

Older examples may refer to `rating_model.onnx`. The active config can point to any local ONNX file, and it currently uses `model_q4f16.onnx`.

AI mode is optional and disabled by default. The image organizer still works without these files by using filename rules and lightweight Pillow analysis.

Keep this folder CPU-friendly for Arctic Prime. Do not add cloud services, online APIs, or heavy AI stacks here.

Do not commit large model files unless intentionally needed. Actual `.onnx` files are ignored by the ImageTools `.gitignore`; keep local model files on the machine unless you specifically decide to version them.
