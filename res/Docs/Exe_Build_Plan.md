# EXE Build Plan

`res/Exe/` is reserved for Windows packaging notes and controlled build assets.

Generated package output should go under ignored paths:

- `res/Exe/output/`
- `res/Exe/generated/`

## Current Gradle Tasks

Build a runnable app folder:

```powershell
.\gradlew.bat packageAppImage
```

Output:

`res/Exe/generated/AetherionMasterCore/`

Build a Windows `.exe` installer:

```powershell
.\gradlew.bat packageWindowsExe
```

Output:

`res/Exe/output/`

## Windows EXE Requirement

The JDK provides `jpackage`, but `jpackage --type exe` requires WiX Toolset on Windows.

Control Prime currently has:

- `jpackage`: available through the JDK
- WiX `candle.exe`: required for installer EXE
- WiX `light.exe`: required for installer EXE

If `packageWindowsExe` reports that WiX is missing, install WiX 3.x or add `candle.exe` and `light.exe` to PATH, then rerun the task.

The app-image task does not require WiX and is the current safe packaging path before installer setup.
