from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


RATING_CATEGORIES = (
    "SFW",
    "Suggestive",
    "Lingerie",
    "Partial_Nude",
    "Nude",
    "Explicit",
    "Unknown",
    "Review_Needed",
)

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

EXPLICIT_KEYWORDS = {"explicit", "sex", "sexual", "hardcore", "genitals"}
NUDE_KEYWORDS = {"nude", "naked", "topless", "bottomless", "bare"}
PARTIAL_NUDE_KEYWORDS = {"partial", "partially", "implied", "covered"}
LINGERIE_KEYWORDS = {"lingerie", "underwear", "bra", "panties", "bikini"}
SUGGESTIVE_KEYWORDS = {"suggestive", "pinup", "seductive", "boudoir", "bedroom"}
SFW_KEYWORDS = {"sfw", "clothed", "casual", "portrait", "shirt", "dress", "jacket", "armor"}
CHARACTER_HINT_KEYWORDS = {"anthro", "furry", "canine", "wolf", "fox", "dog", "shepherd", "tail", "muzzle"}


@dataclass(frozen=True)
class VisualSignals:
    width: int | None = None
    height: int | None = None
    skin_like_ratio: float | None = None
    bright_ratio: float | None = None
    neon_ratio: float | None = None
    pillow_available: bool = False
    error: str | None = None


@dataclass(frozen=True)
class RatingDecision:
    category: str
    confidence: float
    matched_rules: list[str]
    reason: str
    metadata: dict[str, Any] = field(default_factory=dict)


def tokenize(value: str) -> list[str]:
    return [token for token in re.split(r"[^a-z0-9]+", value.lower()) if token]


def safe_name(value: str, fallback: str = "Unknown") -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "_", value.strip()).strip("_")
    return cleaned or fallback


def filename_context(path: Path) -> set[str]:
    return set(tokenize(path.stem) + tokenize(str(path.parent)))


def detect_character(path: Path, default_character: str, known_characters: list[str] | None = None) -> tuple[str, list[str]]:
    tokens = filename_context(path)
    rules: list[str] = []

    for character in known_characters or []:
        character_tokens = set(tokenize(character))
        if character_tokens and character_tokens.issubset(tokens):
            safe = safe_name(character)
            return safe, [f"character_keyword:{safe}"]

    default_tokens = set(tokenize(default_character))
    if default_tokens and default_tokens.issubset(tokens):
        safe = safe_name(default_character)
        rules.append(f"character_keyword:{safe}")
        return safe, rules

    rules.append("character_default")
    return safe_name(default_character), rules


def keyword_rating(path: Path) -> RatingDecision:
    tokens = filename_context(path)
    matched: list[str] = []

    # Filename and folder rules are fast and run first, but later visual checks
    # can lower confidence or force Review_Needed when the signal is unclear.
    checks = (
        ("Explicit", EXPLICIT_KEYWORDS, 0.9),
        ("Nude", NUDE_KEYWORDS, 0.84),
        ("Partial_Nude", PARTIAL_NUDE_KEYWORDS, 0.74),
        ("Lingerie", LINGERIE_KEYWORDS, 0.76),
        ("Suggestive", SUGGESTIVE_KEYWORDS, 0.66),
        ("SFW", SFW_KEYWORDS, 0.72),
    )

    for category, keywords, confidence in checks:
        hits = sorted(tokens & keywords)
        if hits:
            matched.extend(f"keyword:{hit}" for hit in hits)
            return RatingDecision(category, confidence, matched, f"filename_or_folder_matched_{category.lower()}")

    if tokens & CHARACTER_HINT_KEYWORDS:
        matched.extend(f"character_appearance:{hit}" for hit in sorted(tokens & CHARACTER_HINT_KEYWORDS))
        return RatingDecision("SFW", 0.58, matched, "character_appearance_keywords_without_adult_terms")

    return RatingDecision("Unknown", 0.2, ["no_keyword_rating_match"], "no_rating_keywords_found")


def visual_rating(signals: VisualSignals) -> RatingDecision:
    if not signals.pillow_available:
        return RatingDecision(
            "Review_Needed",
            0.35,
            ["pillow_unavailable"],
            signals.error or "Pillow is not installed, visual analysis skipped",
        )

    skin = signals.skin_like_ratio
    neon = signals.neon_ratio
    matched: list[str] = []

    if neon is not None and neon >= 0.18:
        matched.append(f"visual_neon_ratio:{neon:.3f}")

    # This is deliberately conservative. Color ratios are not nudity detection;
    # they only decide whether a human review is safer on low-confidence cases.
    if skin is None:
        return RatingDecision("Review_Needed", 0.4, ["visual_missing_skin_ratio"], "could_not_compute_visual_ratio")
    if skin >= 0.55:
        return RatingDecision("Review_Needed", 0.56, [f"visual_high_skin_ratio:{skin:.3f}"], "high_skin_like_ratio_needs_review")
    if skin >= 0.36:
        return RatingDecision("Suggestive", 0.6, [f"visual_medium_skin_ratio:{skin:.3f}"], "medium_skin_like_ratio")
    if skin <= 0.18:
        return RatingDecision("SFW", 0.72, [f"visual_low_skin_ratio:{skin:.3f}"], "low_skin_like_ratio")

    return RatingDecision("Unknown", 0.48, [f"visual_unclear_skin_ratio:{skin:.3f}"], "visual_signal_unclear")


def combine_decisions(
    keyword: RatingDecision,
    visual: RatingDecision,
    ai_decision: RatingDecision | None,
    confidence_threshold: float,
    review_uncertain: bool,
) -> RatingDecision:
    candidates = [keyword, visual]
    if ai_decision:
        candidates.append(ai_decision)

    matched_rules: list[str] = []
    for decision in candidates:
        matched_rules.extend(decision.matched_rules)

    adult_ai_categories = {"Suggestive", "Lingerie", "Partial_Nude", "Nude", "Explicit"}

    # A high-confidence local AI adult result should not be downgraded just
    # because the lightweight color heuristic asks for review. The visual
    # heuristic is intentionally cautious, but it is weaker than an explicit
    # model result when the model maps into an adult organizer category.
    if (
        ai_decision
        and ai_decision.category in adult_ai_categories
        and ai_decision.confidence >= confidence_threshold
    ):
        combined = RatingDecision(
            ai_decision.category,
            ai_decision.confidence,
            matched_rules + ["ai_adult_result_overrode_visual_review"],
            ai_decision.reason,
            ai_decision.metadata,
        )
    # Visual review warnings override SFW-style filename guesses. This keeps the
    # tool from blindly trusting filenames when the image signal is unclear.
    elif visual.category == "Review_Needed" and keyword.category in {"SFW", "Unknown", "Suggestive"}:
        combined = RatingDecision(
            "Review_Needed",
            min(visual.confidence, 0.6),
            matched_rules,
            f"visual_uncertain_overrode_keyword:{keyword.category}",
        )
    elif ai_decision and ai_decision.confidence >= max(keyword.confidence, visual.confidence):
        combined = RatingDecision(
            ai_decision.category,
            ai_decision.confidence,
            matched_rules,
            ai_decision.reason,
            ai_decision.metadata,
        )
    elif visual.confidence > keyword.confidence + 0.12:
        combined = RatingDecision(visual.category, visual.confidence, matched_rules, visual.reason)
    else:
        combined = RatingDecision(keyword.category, keyword.confidence, matched_rules, keyword.reason)

    if review_uncertain and combined.confidence < confidence_threshold:
        return RatingDecision(
            "Review_Needed",
            combined.confidence,
            matched_rules + [f"below_confidence_threshold:{confidence_threshold:.2f}"],
            f"low_confidence_original_category:{combined.category}",
        )

    if combined.category not in RATING_CATEGORIES:
        return RatingDecision("Review_Needed", combined.confidence, matched_rules, "invalid_category_fallback")

    return combined


def category_summary(entries: list[dict[str, Any]]) -> dict[str, int]:
    counts = {category: 0 for category in RATING_CATEGORIES}
    for entry in entries:
        category = str(entry.get("rating_category", "Unknown"))
        counts[category] = counts.get(category, 0) + 1
    return counts
