# Aetherion MasterCore

Aetherion MasterCore is a Java/JavaFX offline-first AI control hub and modular runtime dashboard for Control Prime and Arctic Prime.

## Current Version

V1.0 foundation:

- JavaFX dashboard shell
- top bar, left sidebar, center workspace, right rail, and status footer
- dark cyber/offline-AI theme
- Gradle project setup for IntelliJ
- local AI placeholder classes for later expansion
- docs for UI lock rules, roadmap, JavaFX CSS notes, and device targets

## Run

From IntelliJ, import the project as a Gradle project and run:

`Aetherion MasterCore` from the Run Configurations menu.

If you create a plain Java run configuration, use:

`com.dev.aetherion.AetherionLauncher`

Do not run `AetherionApplication` directly from IntelliJ. It extends `javafx.application.Application`, and direct Java launches can fail if IntelliJ does not add the JavaFX runtime modules.

From a terminal:

```powershell
.\gradlew.bat run
```

## Project Layout

```text
src/main/java/com/dev/aetherion/
src/main/resources/com/dev/aetherion/
res/Docs/
res/Exe/
res/Config/
res/Data/
```

## Design Rules

The global shell is protected after V1.0. Future work should swap content inside the center workspace instead of redesigning the full layout unless explicitly approved.
