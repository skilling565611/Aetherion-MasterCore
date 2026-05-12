# Train Later Notes

Training is not implemented yet.

Future direction:

- Build a cleaned dataset from `Training/corrections.json`.
- Train on Control Prime using corrected examples and extra reviewed data.
- Export the final model to ONNX.
- Keep the EXE workflow using exported ONNX only.
- Keep Arctic Prime in Lite mode for organizing and review.

Placeholder scripts:

- `train_custom_classifier.py` is only a future hook.
- `export_to_onnx.py` is only a future hook.

Keep model files local unless explicitly requested.
