# ImageTools Local AI Models

This folder is for optional local AI model files used by ImageTools.

Current local model file:

```text
AI/ImageTools/models/model_quantized.onnx
```

Expected labels file for the quantized model:

```text
AI/ImageTools/models/rating_labels.quantized.json
```

`model_quantized.onnx` outputs 5 logits. It must use the 5-class `rating_labels.quantized.json` mapping so output indexes match labels.

Index `0` is treated conservatively as `Review_Needed`, not `SFW`, because illustrated/anthro images are being selected there. This keeps Arctic Prime safe while the model behavior is being reviewed.

The broader 8-category files `rating_labels.json` and `rating_labels.example.json` are kept for organizer taxonomy examples and other model variants.

Older examples may refer to `rating_model.onnx` or `model_q4f16.onnx`. The active config can point to any local ONNX file, and it currently uses `model_quantized.onnx`.

AI mode is optional and disabled by default. The image organizer still works without these files by using filename rules and lightweight Pillow analysis.

Keep this folder CPU-friendly for Arctic Prime. Do not add cloud services, online APIs, or heavy AI stacks here.

Do not commit large model files unless intentionally needed. Actual `.onnx` files are ignored by the ImageTools `.gitignore`; keep local model files on the machine unless you specifically decide to version them.
