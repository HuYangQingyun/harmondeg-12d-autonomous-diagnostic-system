from .models import FRAMEWORK_VERSION, PACKAGE_VERSION
"""Stricter validation for Harmondeg 12-D Autonomous Diagnostic System v1.0."""

from .models import DIMENSIONS, STATUSES, CONFIDENCE, FRAMEWORK_VERSION

REQUIRED_TOP = [
    "framework_version",
    "target",
    "scope",
    "evidence_basis",
    "dimensions",
    "integrated_conclusion",
]

REQUIRED_IC = [
    "theory_position",
    "foundational_evidential_basis",
    "supported_explanatory_domain",
    "application_boundary",
    "major_explanatory_strengths",
    "unresolved_structural_conditions",
    "evidential_status",
    "overall_structural_profile",
    "reference_use_boundary",
]

RECOMMENDED_META = [
    "operating_mode",
    "external_evidence_used",
]


def validate(data, strict_meta=False):
    """
    Validate a Harmondeg 12-D diagnostic input.

    Parameters
    ----------
    data : dict
        Diagnostic payload.
    strict_meta : bool
        If True, also require operating_mode and external_evidence_used.

    Returns
    -------
    list[str]
        Error messages. Empty list means valid.
    """
    errors = []

    for k in REQUIRED_TOP:
        if k not in data:
            errors.append(f"Missing required field: {k}")

    fv = str(data.get("framework_version", "")).strip()
    if fv and fv not in {FRAMEWORK_VERSION, PACKAGE_VERSION}:
        errors.append(
            f"framework_version '{fv}' does not match package version "
            f"'{FRAMEWORK_VERSION}'. Update the field or the package."
        )

    if strict_meta:
        for k in RECOMMENDED_META:
            if k not in data or data.get(k) in (None, ""):
                errors.append(f"strict_meta: missing recommended field: {k}")

    dims = data.get("dimensions", {})
    if not isinstance(dims, dict):
        errors.append("dimensions must be an object/dict")
        return errors

    for code, name in DIMENSIONS.items():
        if code not in dims:
            errors.append(f"Missing dimension: {code}")
            continue
        d = dims[code]
        if not isinstance(d, dict):
            errors.append(f"{code}: dimension entry must be an object")
            continue

        st = d.get("status")
        if st not in STATUSES:
            errors.append(f"{code}: status must be one of {sorted(STATUSES)}")
            continue

        if st == "scored":
            score = d.get("score")
            if not isinstance(score, int) or not (-5 <= score <= 5):
                errors.append(f"{code}: scored status requires integer score in -5..+5")
            if d.get("confidence") not in CONFIDENCE:
                errors.append(f"{code}: scored status requires confidence in {sorted(CONFIDENCE)}")
            if not str(d.get("evidence", "")).strip():
                errors.append(f"{code}: scored status requires non-empty evidence")
            if not str(d.get("structural_observation", "")).strip():
                errors.append(f"{code}: scored status requires non-empty structural_observation")
            if score not in (None, 0) and not str(d.get("score_rationale", "")).strip():
                errors.append(f"{code}: nonzero score requires score_rationale")
            if isinstance(score, int) and score > 0:
                if not d.get("active_management_evidence", False):
                    errors.append(
                        f"{code}: positive score requires active_management_evidence=true "
                        "(mere absence of defect is not sufficient)"
                    )
            if score == -5:
                if not str(d.get("score_rationale", "")).strip():
                    errors.append(
                        f"{code}: score -5 requires score_rationale documenting "
                        "core_relevance, structural_dependence, and failure_consequence"
                    )
            ev = str(d.get("evidence", "")).lower()
            if any(p in ev for p in ("see the cited", "example public-test", "consult the accompanying")):
                errors.append(
                    f"{code}: evidence appears to be a demonstration placeholder; "
                    "replace with concrete, locatable evidence before publication"
                )
        else:
            if d.get("score") is not None:
                errors.append(f"{code}: status {st} must not carry a numeric score (got {d.get('score')})")
            if not str(d.get("rationale", "")).strip():
                errors.append(f"{code}: status {st} requires a non-empty rationale")

    ic = data.get("integrated_conclusion", {})
    if not isinstance(ic, dict):
        errors.append("integrated_conclusion must be an object/dict")
    else:
        for k in REQUIRED_IC:
            if not str(ic.get(k, "")).strip():
                errors.append(f"integrated_conclusion missing or empty: {k}")

    if not str(data.get("target", "")).strip():
        errors.append("target must be non-empty")
    if not str(data.get("scope", "")).strip():
        errors.append("scope must be non-empty")
    if not str(data.get("evidence_basis", "")).strip():
        errors.append("evidence_basis must be non-empty")

    return errors


def validate_or_raise(data, strict_meta=False):
    """Validate and raise ValueError on failure."""
    errs = validate(data, strict_meta=strict_meta)
    if errs:
        raise ValueError("Validation failed:\n- " + "\n- ".join(errs))
    return True
