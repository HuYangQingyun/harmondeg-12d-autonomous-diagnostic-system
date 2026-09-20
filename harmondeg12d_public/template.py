"""Generate an empty diagnostic template conforming to Autonomous Diagnostic System v1.0."""

from .models import DIMENSIONS, FRAMEWORK_VERSION


def make_template(include_meta=True):
    """
    Return a fresh diagnostic dict.

    Integrated-conclusion fields are pre-filled with a short placeholder
    so that validate() does not immediately fail on an empty template.
    Users must replace the placeholders before treating the result as a
    finished diagnosis.
    """
    dims = {}
    for code, name in DIMENSIONS.items():
        dims[code] = {
            "name": name,
            "status": "IE",
            "score": None,
            "confidence": None,
            "evidence": "",
            "structural_observation": "",
            "structural_impact": "",
            "score_rationale": "",
            "active_management_evidence": False,
            "rationale": "Insufficient evidence has not yet been resolved.",
        }

    data = {
        "framework_version": FRAMEWORK_VERSION,
        "target": "",
        "scope": "",
        "evidence_basis": "",
        "dimensions": dims,
        "integrated_conclusion": {
            "theory_position": "[to be completed]",
            "foundational_evidential_basis": "[to be completed]",
            "supported_explanatory_domain": "[to be completed]",
            "application_boundary": "[to be completed]",
            "major_explanatory_strengths": "[to be completed]",
            "unresolved_structural_conditions": "[to be completed]",
            "evidential_status": "[to be completed]",
            "overall_structural_profile": "[to be completed]",
            "reference_use_boundary": (
                "Research reference result under the Harmondeg 12-D "
                "Autonomous Diagnostic System standard."
            ),
        },
    }

    if include_meta:
        data["operating_mode"] = ""
        data["external_evidence_used"] = False

    return data
