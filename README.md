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

`com.dev.aetherion.AetherionApplication`

From a terminal:

```powershell
gradle run
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
