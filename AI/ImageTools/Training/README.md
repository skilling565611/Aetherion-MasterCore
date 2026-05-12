# ImageTools Manual Corrections

This folder stores lightweight local corrections for images the organizer rated incorrectly.

Corrections do not retrain the ONNX model. They are a local override layer that is much lighter and safer for Arctic Prime:

- SHA256 matches are strongest.
- Filename matches are fallback only.
- Manual labels override AI, filename rules, and visual rules.
- Originals are never deleted, moved, or modified.
- Dry-run remains safe.

Add a correction from the repository root:

```powershell
python AI/ImageTools/scripts/add_correction.py `
  --image "AI/PIX/example.jpeg" `
  --label "Explicit" `
  --previous-label "SFW" `
  --notes "wrong AI label"
```

The organizer reads:

```text
AI/ImageTools/Training/corrections.json
```

Real retraining can be added later on Control Prime. For now, corrections are a simple, inspectable JSON file.
