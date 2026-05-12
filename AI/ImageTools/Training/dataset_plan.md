# ImageTools Dataset Plan

The current ImageTools classifier is a layered organizer:

1. Manual corrections by SHA256.
2. Strong filename and folder rules.
3. General ONNX mature-content model.
4. Furry/anthro rule refinement.
5. `Review_Needed` fallback.

Manual corrections are the first local learning layer. They let ImageTools remember known-good labels without retraining the ONNX model.

Later, corrected examples can be copied into `Training/Dataset/` and used to train a custom Aetherion/furry/anthro-aware classifier on Control Prime. Arctic Prime should stay in Lite mode and only run the exported ONNX model after training is complete.

Do not add heavy training packages here yet. Do not install `torch` by default. Training is intentionally postponed.
