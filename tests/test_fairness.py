import pytest

from aimvf.fairness import fairness_review_decision, metric_gap, subgroup_classification_summary


def test_subgroup_summary_and_gap():
    results = subgroup_classification_summary(
        [1, 0, 1, 0],
        [1, 0, 0, 0],
        ["a", "a", "b", "b"],
    )
    assert results["a"]["n"] == 2
    assert results["b"]["n"] == 2
    assert metric_gap(results, "recall_macro")["absolute_gap"] >= 0.0


def test_subgroup_length_check():
    with pytest.raises(ValueError):
        subgroup_classification_summary([1, 0], [1, 0], ["a"])


def test_subgroup_empty_check():
    with pytest.raises(ValueError):
        subgroup_classification_summary([], [], [])


def test_missing_metric_check():
    with pytest.raises(ValueError):
        metric_gap({"a": {"accuracy": 1.0}}, "recall_macro")


def test_review_decision():
    assert fairness_review_decision(0.11, 0.10) == "investigation_required"
    assert fairness_review_decision(0.10, 0.10) == "no_investigation_required"
    with pytest.raises(ValueError):
        fairness_review_decision(-0.1, 0.1)
