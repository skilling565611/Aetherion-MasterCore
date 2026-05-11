# PIX Rules

Purpose:
This file contains the permanent rules for the PIX area. Both Arctic Prime and Control Prime must read this file before making changes involving PIX.

Rules:

1. Do not delete PIX.
2. Do not remove PIX files unless explicitly approved by the user.
3. Do not rename PIX files unless explicitly approved.
4. Do not overwrite PIX recovery files.
5. Do not auto-clean PIX.
6. Do not hard reset or force overwrite PIX.
7. Do not push PIX changes to GitHub without approval.
8. Before editing PIX, verify these files exist:
   - PIX/PC_Pix.dev
   - PIX/Pix.dev
9. Arctic Prime may act as the recovery/verification copy.
10. Control Prime may act as the main build/workstation copy.
11. If PIX rules need changes, update PIX_RULES.md first.
12. Always read PIX_RULES.md before touching anything inside PIX.

System names:

- Control Prime = Main PC / build workstation
- Arctic Prime = Laptop / verification and recovery system

Command Keywords:

Control Prime:

- "Good to go!"
  Meaning:
  Approved to safely push verified changes to GitHub.

Arctic Prime:

- "push"
  Meaning:
  Approved to safely push recovery/verification updates to GitHub.

Both Systems:

- "pull"
  Meaning:
  Approved to safely sync latest verified repository state.

Important command rules:

1. Commands must only execute after verification.
2. No automatic push behavior.
3. No force push unless explicitly approved.
4. Read PIX_RULES.md before performing Git operations involving PIX.
5. Arctic Prime may act as temporary recovery source-of-truth.
6. Control Prime may act as main build/development source.

Command purpose:
Reduce accidental sync conflicts and maintain stable coordination between Control Prime and Arctic Prime.

Important:
This file should only change when the user updates the PIX rules.
