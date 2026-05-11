# Aetherion MasterCore Update Log

This file tracks lightweight handoff notes between Arctic Prime, Control Prime, and phone ChatGPT planning.

## Current Flow

- Arctic Prime is the laptop/dev companion for small edits, notes, lightweight checks, and GitHub pull/push work.
- Control Prime is the main PC for setup, Java/JavaFX/Gradle validation, runtime checks, and heavier project work.
- Phone ChatGPT can be used for planning, notes, and ideas that later get copied into this repo intentionally.

## Pull Verification Rule

After every pull on Arctic Prime, run a lightweight verification pass:

- check Git status
- confirm key files are present
- confirm `Aetherion.fxml` parses as valid XML
- confirm controller/resource wiring is present
- confirm `Main.css` exists at the expected path
- note optional image references without treating them as blockers

Do not run heavy builds/tests on Arctic Prime unless explicitly requested.

## Recent Status

- `dev` was synced with `origin/dev`.
- `Main.css` and `Aetherion.fxml` are present in resources.
- Current FXML is controller-wired and includes expected controller IDs.
- `logo.png` is user-managed and optional for now.
