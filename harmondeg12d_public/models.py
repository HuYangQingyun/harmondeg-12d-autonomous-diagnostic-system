"""Core constants for Harmondeg 12-D Autonomous Diagnostic System v1.0 v1.0."""

FRAMEWORK_VERSION = "Harmondeg 12-D Autonomous Diagnostic System v1.0"
PACKAGE_VERSION = "1.0.0"

DIMENSIONS = {
    "D1": "Level Collapse",
    "D2": "Scope Overreach",
    "D3": "Definition Drift",
    "D4": "Observer Ambiguity",
    "D5": "Temporal Flattening",
    "D6": "Hidden Premises",
    "D7": "Category Confusion",
    "D8": "Self-Reference Loops",
    "D9": "Context Erasure",
    "D10": "Language Reification and Infinitization",
    "D11": "Operational Viability",
    "D12": "Consequence Mapping",
}

STATUSES = {"scored", "IE", "N/A"}
CONFIDENCE = {"High", "Medium", "Low"}

OPENING_NOTICE = (
    "Harmondeg 12-D Autonomous Diagnostic System v1.0 — Research Reference Result. "
    "This report is generated under the Harmondeg 12-D standard diagnostic configuration "
    "and is provided for research and reference only. "
    "It is not a legal, regulatory, judicial, institutional, or universally binding determination, "
    "and it does not constitute a final determination of truth or falsity."
)

CLOSING_NOTICE = (
    "Research Reference Only. The findings in this report reflect the Harmondeg 12-D "
    "Autonomous Diagnostic System v1.0 standard, the defined diagnostic scope, and the evidence available "
    "for this analysis. Subsequent interpretation and use remain the responsibility of the user."
)
