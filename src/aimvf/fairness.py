from __future__ import annotations

from collections import defaultdict
from typing import Iterable, Sequence

from aimvf.metrics import classification_summary


def subgroup_classification_summary(
    y_true: Sequence[int],
    y_pred: Sequence[int],
    subgroup: Sequence[str],
) -> dict:
    """Calculate classification metrics for each subgroup.

    This utility is intentionally simple and transparent. It is suitable for
    demonstration, documentation, and portfolio examples rather than production
    validation without further statistical review.
    """
    grouped_indices: dict[str, list[int]] = defaultdict(list)
    for index, group_name in enumerate(subgroup):
        grouped_indices[str(group_name)].append(index)

    results = {}
    for group_name, indices in grouped_indices.items():
        group_y_true = [y_true[i] for i in indices]
        group_y_pred = [y_pred[i] for i in indices]
        results[group_name] = {
            "n": len(indices),
            **classification_summary(group_y_true, group_y_pred),
        }

    return results


def metric_gap(
    subgroup_results: dict,
    metric_name: str = "recall_macro",
) -> dict:
    """Calculate the absolute gap between the best and worst subgroup metric."""
    values = {
        group_name: values[metric_name]
        for group_name, values in subgroup_results.items()
        if metric_name in values
    }
    if not values:
        raise ValueError(f"Metric '{metric_name}' was not found in subgroup results")

    best_group = max(values, key=values.get)
    worst_group = min(values, key=values.get)
    return {
        "metric": metric_name,
        "best_group": best_group,
        "best_value": values[best_group],
        "worst_group": worst_group,
        "worst_value": values[worst_group],
        "absolute_gap": abs(values[best_group] - values[worst_group]),
    }


def fairness_review_decision(metric_gap_value: float, investigation_threshold: float = 0.10) -> str:
    """Return a simple review decision based on a predefined gap threshold."""
    if metric_gap_value > investigation_threshold:
        return "investigation_required"
    return "no_investigation_required"
