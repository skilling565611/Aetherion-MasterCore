# ONNX Model Folder

Place the exported ImageTools ONNX classifier files here before building the EXE.

Expected files:

- `model.onnx`
- `labels.json`
- `config.json`
- `preprocessor_config.json`
- tokenizer/config files if the exported model needs them

The build copies this folder beside the EXE:

```text
dist/AetherionImageTools/Models/ONNX/
```

Keep `model.onnx` local unless you explicitly decide to track a model file.
