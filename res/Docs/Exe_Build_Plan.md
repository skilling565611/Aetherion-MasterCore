# EXE Build Plan

`res/Exe/` is reserved for Windows packaging notes and controlled build assets.

Generated package output should go under ignored paths:

- `res/Exe/output/`
- `res/Exe/generated/`

Future packaging can use Gradle, jpackage, or a dedicated release workflow. V1.0 does not bundle a Windows EXE.
