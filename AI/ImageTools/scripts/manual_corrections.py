from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from rating_rules import RATING_CATEGORIES


@dataclass(frozen=True)
class ManualCorrection:
    correct_label: str
    reason: str
    entry: dict[str, Any]


def empty_payload() -> dict[str, list[dict[str, Any]]]:
    return {"corrections": []}


def load_corrections(path: Path | None) -> list[dict[str, Any]]:
    """Load correction entries, treating a missing file as no corrections."""

    if path is None or not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    corrections = payload.get("corrections", []) if isinstance(payload, dict) else []
    if not isinstance(corrections, list):
        raise SystemExit(f"Corrections file must contain a corrections list: {path}")
    return [entry for entry in corrections if isinstance(entry, dict)]


def validate_label(label: str) -> str:
    if label not in RATING_CATEGORIES:
        valid = ", ".join(RATING_CATEGORIES)
        raise SystemExit(f"Invalid label '{label}'. Valid labels: {valid}")
    return label


def find_manual_correction(
    corrections: list[dict[str, Any]],
    sha256: str,
    filename: str,
) -> ManualCorrection | None:
    """Find the strongest manual correction for this image.

    SHA256 wins because it identifies exact file content. Filename fallback is
    useful for quick local workflows, but it is intentionally weaker.
    """

    filename_lower = filename.lower()
    for entry in corrections:
        if str(entry.get("sha256", "")).lower() == sha256.lower():
            label = validate_label(str(entry.get("correct_label", "")))
            return ManualCorrection(label, "sha256_match", entry)

    for entry in corrections:
        entry_filename = str(entry.get("filename", "")).lower()
        if entry_filename and entry_filename == filename_lower:
            label = validate_label(str(entry.get("correct_label", "")))
            return ManualCorrection(label, "filename_match", entry)

    return None


def write_corrections(path: Path, corrections: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"corrections": corrections}, indent=2), encoding="utf-8")
