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
    flip_binary_labels: bool = False
    debug_outputs: bool = False
    load_mode: str = "source"


class LocalAIClassifier:
    """Optional CPU-only AI classifier hook.

    This keeps the base tool lightweight. If no local model is configured, or
    optional dependencies are missing, classification simply falls back to the
    rules + Pillow pipeline. No online APIs are used.
    """

    LABEL_TO_CATEGORY = {
        "anime picture": "SFW",
        "anime_picture": "SFW",
        "sfw": "SFW",
        "safe": "SFW",
        "enticing or sensual": "Suggestive",
        "enticing_or_sensual": "Suggestive",
        "suggestive": "Suggestive",
        "lingerie": "Lingerie",
        "partial_nude": "Partial_Nude",
        "partial nude": "Partial_Nude",
        "nude": "Nude",
        "nudity": "Nude",
        "explicit": "Explicit",
        "nsfw": "Explicit",
        "hentai": "Explicit",
        "hential": "Explicit",
        "pornography": "Explicit",
        "porn": "Explicit",
        "sexy": "Suggestive",
        "neutral": "SFW",
        "drawings": "SFW",
        "drawing": "SFW",
        "illustration": "SFW",
        "illustrated": "SFW",
        "unknown": "Unknown",
    }

    def __init__(self, enabled: bool = False, config: AIConfig | None = None) -> None:
        self.enabled = enabled
        self.available = False
        self.reason = "AI mode disabled"
        self.config = config or AIConfig()
        self.model_path = self.config.model_path
        self.labels_path = self.config.labels_path
        self.model_exists = bool(self.model_path and self.model_path.exists())
        self.labels_exist = bool(self.labels_path and self.labels_path.exists())
        self.load_mode = self.config.load_mode
        self.session = None
        self.labels: list[str] = []
        self.label_mapping: dict[str, str] = {}
        self.input_name: str | None = None
        self.input_shapes: list[dict[str, object]] = []
        self.output_shapes: list[dict[str, object]] = []

        if not enabled:
            return

        if not self.config.model_path:
            self.reason = "AI mode requested, but no local ONNX model path was provided"
            return
        if not self.config.model_path.exists():
            self.reason = (
                "ONNX model missing. Expected model file at "
                f"{self.config.model_path}. Put model.onnx in Models/ONNX beside the EXE "
                "or in AI/ImageTools/Models/ONNX when running from source."
            )
            return
        if not self.config.labels_path or not self.config.labels_path.exists():
            self.reason = f"AI labels JSON was not provided or was not found: {self.config.labels_path}"
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
                self.label_mapping = {str(index): str(label) for index, label in ordered}
                self.labels = [str(label) for _, label in ordered]
            elif isinstance(labels_payload, list):
                self.labels = [str(label) for label in labels_payload]
                self.label_mapping = {str(index): str(label) for index, label in enumerate(self.labels)}
            else:
                self.reason = "AI labels JSON must be a list or an index-to-label object"
                return

            options = ort.SessionOptions()
            options.intra_op_num_threads = 1
            options.inter_op_num_threads = 1
            # Quantized or converted ONNX models can fail during optional graph
            # fusion passes even when the model itself is usable. Disabling
            # graph optimization is slower, but safer for Arctic Prime and keeps
            # the local AI hook CPU-only and conservative.
            options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_DISABLE_ALL
            self.session = ort.InferenceSession(
                str(self.config.model_path),
                sess_options=options,
                providers=["CPUExecutionProvider"],
            )
            inputs = self.session.get_inputs()
            outputs = self.session.get_outputs()
            self.input_name = inputs[0].name
            self.input_shapes = [{"name": item.name, "shape": list(item.shape)} for item in inputs]
            self.output_shapes = [{"name": item.name, "shape": list(item.shape)} for item in outputs]
        except Exception as error:
            self.reason = f"Local AI model could not be loaded: {error}"
            return

        self.available = True
        self.reason = "Local CPU ONNX classifier loaded"

    def log_metadata(self) -> dict[str, object]:
        return {
            "ai_model_path": str(self.model_path) if self.model_path else None,
            "ai_model_exists": self.model_exists,
            "ai_model_load_mode": self.load_mode,
            "ai_labels_path": str(self.labels_path) if self.labels_path else None,
            "ai_labels_exists": self.labels_exist,
            "ai_status": self.reason,
        }

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
            raw_scores = np.asarray(outputs[0]).reshape(-1)
            stable_scores = raw_scores - raw_scores.max()
            probabilities = np.exp(stable_scores) / np.exp(stable_scores).sum()
            index = int(probabilities.argmax())
            flip_applied = self.config.flip_binary_labels and len(probabilities) == 2
            selected_index = 1 - index if flip_applied else index
            confidence = float(probabilities[index])
            raw_label = self.labels[selected_index] if selected_index < len(self.labels) else "Unknown"
            category = self.LABEL_TO_CATEGORY.get(raw_label.strip().lower(), "Unknown")
        except Exception as error:
            return RatingDecision("Review_Needed", 0.35, ["ai_inference_error"], f"local_ai_error:{error}")

        adult_labels = {"nsfw", "nude", "nudity", "explicit", "partial_nude", "partial nude"}
        label_values = [label.strip().lower() for label in self.labels]
        output_count = int(len(probabilities))
        label_count_matches_output = len(self.labels) == output_count
        label_count_warning = None
        if not label_count_matches_output:
            label_count_warning = f"label_count:{len(self.labels)} output_count:{output_count}"
        labels_may_be_reversed = (
            len(label_values) == 2
            and label_values[0] in adult_labels
            and label_values[1] in {"sfw", "safe"}
        )
        suspicious_high_sfw = (
            category == "SFW"
            and confidence >= 0.9
            and signals.skin_like_ratio is not None
            and signals.skin_like_ratio >= 0.16
        )
        if suspicious_high_sfw:
            labels_may_be_reversed = True

        metadata = {
            "ai_raw_outputs": raw_scores.astype(float).round(6).tolist() if self.config.debug_outputs else None,
            "ai_probabilities": probabilities.astype(float).round(6).tolist() if self.config.debug_outputs else None,
            "ai_selected_index": selected_index,
            "ai_original_selected_index": index,
            "ai_selected_label": raw_label,
            "ai_label_mapping": self.label_mapping,
            "ai_model_input_shape": self.input_shapes,
            "ai_model_output_shape": self.output_shapes,
            "ai_actual_output_shape": [list(np.asarray(output).shape) for output in outputs],
            "ai_preprocessing_mode": f"rgb_resize_{self.config.input_size}_chw_float32_0_1",
            "ai_flip_binary_labels": flip_applied,
            "ai_flip_binary_labels_requested": self.config.flip_binary_labels,
            "ai_labels_may_be_reversed": labels_may_be_reversed,
            "ai_label_count_matches_output": label_count_matches_output,
            "ai_label_count_warning": label_count_warning,
        }
        matched = [f"ai_label:{raw_label}", f"ai_confidence:{confidence:.3f}", "ai_provider:cpu_onnx"]
        if self.config.flip_binary_labels and len(probabilities) == 2:
            matched.append("ai_flip_binary_labels")
        elif self.config.flip_binary_labels:
            matched.append(f"ai_flip_binary_labels_ignored_for_output_count:{len(probabilities)}")
        if labels_may_be_reversed:
            matched.append("ai_labels_may_be_reversed")
        if label_count_warning:
            matched.append(f"ai_label_count_warning:{label_count_warning}")

        return RatingDecision(
            category,
            confidence,
            matched,
            "local_cpu_ai_classifier",
            metadata,
        )
