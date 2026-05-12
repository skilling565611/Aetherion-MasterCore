from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from rating_rules import RatingDecision, VisualSignals, filename_context


ANTHRO_KEYWORDS = {
    "anthro",
    "anthropomorphic",
    "furry",
    "fursona",
    "kemono",
}
EAR_KEYWORDS = {"ear", "ears", "foxears", "wolfears", "cat_ears"}
TAIL_KEYWORDS = {"tail", "tails", "fluffy_tail", "foxtail", "wolftail"}
SPECIES_KEYWORDS = {
    "canine",
    "cat",
    "dragon",
    "feline",
    "fox",
    "german",
    "husky",
    "kitsune",
    "shep",
    "shepherd",
    "wolf",
}
FUR_COLOR_KEYWORDS = {
    "blackfur",
    "bluefur",
    "brownfur",
    "fur",
    "furred",
    "grayfur",
    "greyfur",
    "whitefur",
}
OUTFIT_KEYWORDS = {
    "armor",
    "bodysuit",
    "boots",
    "coat",
    "dress",
    "hoodie",
    "jacket",
    "outfit",
    "shirt",
    "suit",
    "uniform",
}
LINGERIE_KEYWORDS = {
    "bikini",
    "bra",
    "garter",
    "lingerie",
    "panties",
    "stockings",
    "thong",
    "underwear",
}
EXPOSURE_KEYWORDS = {
    "bare",
    "bottomless",
    "exposed",
    "naked",
    "nude",
    "topless",
}
EXPLICIT_EXPOSURE_KEYWORDS = {
    "explicit",
    "genitals",
    "hardcore",
    "porn",
    "pornography",
    "sex",
    "sexual",
}
CYBERPUNK_KEYWORDS = {
    "cyber",
    "cyberpunk",
    "glow",
    "neon",
    "techwear",
}
CHARACTER_HINTS = {
    "nyra": "Nyra_Vale",
    "vale": "Nyra_Vale",
    "nyra_vale": "Nyra_Vale",
}


@dataclass(frozen=True)
class FurryRuleResult:
    applied: bool
    score: float
    furry_detected: bool
    outfit_hint: str | None
    exposure_hint: str | None
    species_hint: str | None
    character_hint: str | None
    style_hint: str | None
    matched_rules: list[str]

    def log_fields(self, final_layer_used: str) -> dict[str, object]:
        return {
            "furry_rules_applied": self.applied,
            "furry_rule_score": round(self.score, 3),
            "furry_detected": self.furry_detected,
            "outfit_hint": self.outfit_hint,
            "exposure_hint": self.exposure_hint,
            "species_hint": self.species_hint,
            "character_hint": self.character_hint,
            "final_layer_used": final_layer_used,
        }


def _first_hit(tokens: set[str], keywords: set[str]) -> str | None:
    hits = sorted(tokens & keywords)
    return hits[0] if hits else None


def detect_furry_rules(path: Path, signals: VisualSignals) -> FurryRuleResult:
    tokens = filename_context(path)
    matched: list[str] = []
    score = 0.0

    anthro_hit = _first_hit(tokens, ANTHRO_KEYWORDS)
    ear_hit = _first_hit(tokens, EAR_KEYWORDS)
    tail_hit = _first_hit(tokens, TAIL_KEYWORDS)
    species_hit = _first_hit(tokens, SPECIES_KEYWORDS)
    fur_hit = _first_hit(tokens, FUR_COLOR_KEYWORDS)
    outfit_hit = _first_hit(tokens, OUTFIT_KEYWORDS)
    lingerie_hit = _first_hit(tokens, LINGERIE_KEYWORDS)
    exposure_hit = _first_hit(tokens, EXPOSURE_KEYWORDS)
    explicit_hit = _first_hit(tokens, EXPLICIT_EXPOSURE_KEYWORDS)
    cyberpunk_hit = _first_hit(tokens, CYBERPUNK_KEYWORDS)

    for label, hit, weight in (
        ("anthro", anthro_hit, 0.35),
        ("ears", ear_hit, 0.14),
        ("tail", tail_hit, 0.14),
        ("species", species_hit, 0.18),
        ("fur", fur_hit, 0.12),
        ("outfit", outfit_hit, 0.08),
        ("lingerie", lingerie_hit, 0.12),
        ("exposure", exposure_hit, 0.18),
        ("explicit", explicit_hit, 0.24),
        ("style", cyberpunk_hit, 0.08),
    ):
        if hit:
            score += weight
            matched.append(f"furry_{label}:{hit}")

    neon = signals.neon_ratio or 0.0
    if neon >= 0.18:
        score += 0.06
        matched.append(f"furry_visual_neon_ratio:{neon:.3f}")

    character_hint = None
    for token, character in CHARACTER_HINTS.items():
        if token in tokens:
            character_hint = character
            score += 0.12
            matched.append(f"furry_character:{character}")
            break

    furry_detected = bool(anthro_hit or species_hit or ((ear_hit or tail_hit) and fur_hit))
    applied = bool(matched)
    outfit_hint = lingerie_hit or outfit_hit
    exposure_hint = explicit_hit or exposure_hit
    style_hint = cyberpunk_hit or ("neon" if neon >= 0.18 else None)

    return FurryRuleResult(
        applied=applied,
        score=min(score, 1.0),
        furry_detected=furry_detected,
        outfit_hint=outfit_hint,
        exposure_hint=exposure_hint,
        species_hint=species_hit or fur_hit,
        character_hint=character_hint,
        style_hint=style_hint,
        matched_rules=matched,
    )


def refine_with_furry_rules(decision: RatingDecision, rules: FurryRuleResult) -> RatingDecision:
    """Conservatively refine organizer labels for anthro character art.

    This layer is intentionally filename/folder and low-cost visual context.
    It never replaces manual corrections and does not claim to be a custom
    trained classifier.
    """

    if not rules.applied:
        return decision

    matched = decision.matched_rules + rules.matched_rules
    category = decision.category
    confidence = max(decision.confidence, min(0.82, 0.45 + rules.score))
    reason = decision.reason

    if rules.exposure_hint in EXPLICIT_EXPOSURE_KEYWORDS:
        category = "Explicit"
        confidence = max(confidence, 0.86)
        reason = "furry_rules_explicit_exposure_hint"
    elif rules.exposure_hint in EXPOSURE_KEYWORDS and category in {"SFW", "Unknown", "Suggestive", "Review_Needed"}:
        category = "Nude"
        confidence = max(confidence, 0.78)
        reason = "furry_rules_exposure_hint"
    elif rules.outfit_hint in LINGERIE_KEYWORDS and category in {"SFW", "Unknown", "Review_Needed"}:
        category = "Lingerie"
        confidence = max(confidence, 0.76)
        reason = "furry_rules_lingerie_hint"
    elif rules.furry_detected and category == "Unknown":
        category = "SFW"
        confidence = max(confidence, 0.58)
        reason = "furry_rules_anthro_character_context"

    return RatingDecision(category, confidence, matched, reason, decision.metadata)

