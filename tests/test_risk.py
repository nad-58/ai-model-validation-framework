import pytest

from aimvf.risk import risk_priority_number


def test_risk_priority_levels():
    assert risk_priority_number(1, 1, 1) == {"rpn": 1, "level": "low"}
    assert risk_priority_number(5, 2, 3) == {"rpn": 30, "level": "medium"}
    assert risk_priority_number(5, 4, 3) == {"rpn": 60, "level": "high"}


def test_risk_priority_rejects_invalid_values():
    with pytest.raises(ValueError):
        risk_priority_number(0, 1, 1)
    with pytest.raises(ValueError):
        risk_priority_number(1, 6, 1)
