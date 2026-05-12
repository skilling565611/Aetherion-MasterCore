from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from rating_rules import category_summary


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


class ReportWriter:
    def __init__(self, log_dir: Path) -> None:
        self.log_dir = log_dir
        self.entries: list[dict[str, Any]] = []
        self.scan_entries: list[dict[str, Any]] = []
        self.duplicates: list[dict[str, Any]] = []

    def add_scan(self, entry: dict[str, Any]) -> None:
        self.scan_entries.append(entry)

    def add_decision(self, entry: dict[str, Any]) -> None:
        self.entries.append(entry)

    def add_duplicate(self, entry: dict[str, Any]) -> None:
        self.duplicates.append(entry)

    def write(self) -> dict[str, Path]:
        paths = {
            "scan_report": self.log_dir / "scan_report.json",
            "review_needed": self.log_dir / "review_needed.json",
            "duplicate_report": self.log_dir / "duplicate_report.json",
            "rating_summary": self.log_dir / "rating_summary.json",
            "decision_log": self.log_dir / "decision_log.json",
        }
        review_entries = [entry for entry in self.entries if entry.get("rating_category") == "Review_Needed"]
        summary = {
            "created_at": utc_now(),
            "total_scanned": len(self.scan_entries),
            "total_decisions": len(self.entries),
            "ratings": category_summary(self.entries),
        }

        write_json(paths["scan_report"], {"created_at": utc_now(), "images": self.scan_entries})
        write_json(paths["review_needed"], {"created_at": utc_now(), "images": review_entries})
        write_json(paths["duplicate_report"], {"created_at": utc_now(), "duplicates": self.duplicates})
        write_json(paths["rating_summary"], summary)
        write_json(paths["decision_log"], {"created_at": utc_now(), "decisions": self.entries})
        return paths
