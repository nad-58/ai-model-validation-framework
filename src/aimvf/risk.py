from __future__ import annotations


def risk_priority_number(severity: int, occurrence: int, detectability: int) -> dict:
    """Calculate a simple risk priority number and qualitative level.

    Scores are expected on a 1-5 scale, where higher values indicate higher risk.
    """
    for name, value in {
        "severity": severity,
        "occurrence": occurrence,
        "detectability": detectability,
    }.items():
        if value < 1 or value > 5:
            raise ValueError(f"{name} must be between 1 and 5")

    rpn = severity * occurrence * detectability
    if rpn >= 60:
        level = "high"
    elif rpn >= 25:
        level = "medium"
    else:
        level = "low"

    return {"rpn": rpn, "level": level}
