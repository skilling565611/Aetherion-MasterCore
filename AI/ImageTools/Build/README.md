# ImageTools EXE Build

This folder contains the Control Prime build helper for the Arctic Prime test EXE.

The build uses PyInstaller in one-folder mode. Models, configs, corrections, training data, and logs stay external to the EXE so they can be edited or replaced without rebuilding.

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
AI/ImageTools/Build/Aetherion_ImageTools/
|-- AetherionImageTools.exe
|-- Configs/
|   `-- default_config.json
|-- Models/
|   |-- Lite/
|   |-- Medium/
|   `-- Heavy/
|-- Training/
|   `-- corrections.json
|-- Logs/
`-- README.txt
```

PyInstaller may also create an internal support folder beside the EXE. Keep it with the EXE folder.

## Safety

- Build on Control Prime.
- Test the output folder on Arctic Prime.
- Do not bundle ONNX model files.
- Do not bundle large image datasets.
- Keep dry-run and copy-only enabled for first tests.
- Real copy mode in the EXE menu asks for confirmation.

