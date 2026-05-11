# Aetherion MasterCore Updates

This file tracks lightweight project handoff notes, sync status, and device-role context.

## Current Device Roles

### Arctic Prime / Laptop

Arctic Prime is the lightweight laptop/dev companion.

Allowed work:

- small CSS edits
- small FXML adjustments
- documentation edits
- README updates
- notes cleanup
- small UI text edits
- small config edits
- GitHub pull/push checks
- lightweight inspection
- simple bug notes

Do not do heavy builds, major refactors, dependency changes, packaging, major UI redesigns, or full project rewrites on Arctic Prime.

Preserve:

- current UI identity
- Main.css theme
- project structure
- GitHub-safe files

If a task is too heavy, mark it for Control Prime.

### Control Prime / PC

Control Prime is the primary build/runtime/development workstation.

Current Control Prime focus:

- properly set up Java
- properly set up JavaFX
- properly set up Gradle
- verify IntelliJ project configuration
- verify JavaFX runtime configuration
- verify FXML loading
- verify Main.css loading
- verify controller connections
- verify GitHub repo structure
- verify project launches successfully

Control Prime should handle heavier validation, setup, Gradle checks, JavaFX runtime checks, and launch verification.

Do not redesign the approved UI, replace the Aetherion visual identity, or restructure the approved shell layout unless explicitly requested.

## Lightweight Verification Notes

When pulling updates on Arctic Prime, run a lightweight verification pass:

- check Git status
- confirm key files are present
- confirm `Aetherion.fxml` parses as valid XML
- confirm controller/resource wiring is present
- confirm `Main.css` exists at the expected path
- note optional image references without treating them as blockers

Avoid heavy builds/tests on Arctic Prime unless explicitly requested.

## Recent Status

- `dev` was synced with `origin/dev`.
- Resource check confirmed `Main.css` and `Aetherion.fxml` are present.
- Current FXML is controller-wired again and includes the expected controller IDs.
- `logo.png` is user-managed and optional for now.
