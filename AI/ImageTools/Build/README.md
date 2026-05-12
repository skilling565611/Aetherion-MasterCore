# ImageTools EXE Build

This folder contains the Control Prime build helper for the Arctic Prime test EXE.

The build uses PyInstaller in one-folder mode. Configs, corrections, logs, and output stay external to the EXE so they can be edited or replaced without rebuilding. The ONNX model folder is copied beside the EXE so Arctic Prime can run AI mode without a separate model install.

## Install Build Requirement

```powershell
python -m pip install -r AI/ImageTools/Requirements/build.txt
```

## Build

```powershell
python AI/ImageTools/Build/build_exe.py
```

Or run:

```powershell
AI/ImageTools/Build/build_image_tools.bat
```

## Output

The final portable folder is:

```text
dist/AetherionImageTools/
|-- AetherionImageTools.exe
|-- Configs/
|   `-- default_config.json
|-- Models/
|   `-- ONNX/
|       |-- model.onnx
|       |-- labels.json
|       |-- config.json
|       `-- preprocessor_config.json
|-- Training/
|   `-- corrections.json
|-- Logs/
|-- Output/
|-- README_Run_First.txt
`-- README.txt
```

PyInstaller may also create an internal support folder beside the EXE. Keep it with the EXE folder.

## Safety

- Build on Control Prime.
- Test the output folder on Arctic Prime.
- Keep `Models/ONNX` beside the EXE.
- Do not bundle large image datasets.
- Keep dry-run and copy-only enabled for first tests.
- Real copy mode in the EXE menu asks for confirmation.

Before building, put the ONNX files here:

```text
AI/ImageTools/Models/ONNX/
```

If `model.onnx` is missing, the build still completes but prints a warning.
