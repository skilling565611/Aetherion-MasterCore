from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from rating_rules import RatingDecision, VisualSignals


@dataclass(frozen=True)
class AIConfig:
    """Small local model settings.

    The default organizer does not require a model. These paths are only used
    when the user opts in with --use-ai and supplies a local CPU-friendly ONNX
    classifier plus a JSON label map.
    """

    model_path: Path | None = None
    labels_path: Path | None = None
    input_size: int = 224


class LocalAIClassifier:
    """Optional CPU-only AI classifier hook.

    This keeps the base tool lightweight. If no local model is configured, or
    optional dependencies are missing, classification simply falls back to the
    rules + Pillow pipeline. No online APIs are used.
    """

    LABEL_TO_CATEGORY = {
        "sfw": "SFW",
        "safe": "SFW",
        "suggestive": "Suggestive",
        "lingerie": "Lingerie",
        "partial_nude": "Partial_Nude",
        "partial nude": "Partial_Nude",
        "nude": "Nude",
        "nudity": "Nude",
        "explicit": "Explicit",
        "nsfw": "Explicit",
        "unknown": "Unknown",
        "review_needed": "Review_Needed",
        "review needed": "Review_Needed",
    }

    def __init__(self, enabled: bool = False, config: AIConfig | None = None) -> None:
        self.enabled = enabled
        self.available = False
        self.reason = "AI mode disabled"
        self.config = config or AIConfig()
        self.session = None
        self.labels: list[str] = []
        self.input_name: str | None = None

        if not enabled:
            return

        if not self.config.model_path:
            self.reason = "AI mode requested, but no local ONNX model path was provided"
            return
        if not self.config.model_path.exists():
            self.reason = f"AI model was not found: {self.config.model_path}"
            return
        if not self.config.labels_path or not self.config.labels_path.exists():
            self.reason = "AI labels JSON was not provided or was not found"
            return

        try:
            import onnxruntime as ort
        except Exception:
            self.reason = "Optional AI dependencies are missing; continuing with rules and Pillow heuristics"
            return

        try:
            labels_payload = json.loads(self.config.labels_path.read_text(encoding="utf-8"))
            if isinstance(labels_payload, dict):
                ordered = sorted(labels_payload.items(), key=lambda item: int(item[0]))
                self.labels = [str(label) for _, label in ordered]
            elif isinstance(labels_payload, list):
                self.labels = [str(label) for label in labels_payload]
            else:
                self.reason = "AI labels JSON must be a list or an index-to-label object"
                return

            options = ort.SessionOptions()
            options.intra_op_num_threads = 1
            options.inter_op_num_threads = 1
            self.session = ort.InferenceSession(
                str(self.config.model_path),
                sess_options=options,
                providers=["CPUExecutionProvider"],
            )
            self.input_name = self.session.get_inputs()[0].name
        except Exception as error:
            self.reason = f"Local AI model could not be loaded: {error}"
            return

        self.available = True
        self.reason = "Local CPU ONNX classifier loaded"

    def classify(self, path: Path, signals: VisualSignals) -> RatingDecision | None:
        if not self.enabled or not self.available or self.session is None or self.input_name is None:
            return None

        try:
            import numpy as np
            from PIL import Image

            with Image.open(path) as image:
                image = image.convert("RGB").resize((self.config.input_size, self.config.input_size))
                array = np.asarray(image, dtype="float32") / 255.0
                array = np.transpose(array, (2, 0, 1))[None, :, :, :]

            outputs = self.session.run(None, {self.input_name: array})
            scores = np.asarray(outputs[0]).reshape(-1)
            scores = scores - scores.max()
            probabilities = np.exp(scores) / np.exp(scores).sum()
            index = int(probabilities.argmax())
            confidence = float(probabilities[index])
            raw_label = self.labels[index] if index < len(self.labels) else "Unknown"
            category = self.LABEL_TO_CATEGORY.get(raw_label.strip().lower(), "Unknown")
        except Exception as error:
            return RatingDecision("Review_Needed", 0.35, ["ai_inference_error"], f"local_ai_error:{error}")

        return RatingDecision(
            category,
            confidence,
            [f"ai_label:{raw_label}", f"ai_confidence:{confidence:.3f}", "ai_provider:cpu_onnx"],
            "local_cpu_ai_classifier",
        )
