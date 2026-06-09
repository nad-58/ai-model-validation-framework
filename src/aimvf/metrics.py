from __future__ import annotations

from typing import Sequence

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score


def _validate_lengths(first: Sequence[object], second: Sequence[object]) -> None:
    if len(first) != len(second):
        raise ValueError("inputs must have the same length")
    if len(first) == 0:
        raise ValueError("inputs must not be empty")


def classification_summary(y_true: Sequence[int], y_pred: Sequence[int]) -> dict:
    """Return a compact binary or multiclass classification summary."""
    _validate_lengths(y_true, y_pred)
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision_macro": float(precision_score(y_true, y_pred, average="macro", zero_division=0)),
        "recall_macro": float(recall_score(y_true, y_pred, average="macro", zero_division=0)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
    }


def dice_score(y_true: Sequence[int], y_pred: Sequence[int]) -> float:
    """Calculate Dice score for binary masks represented as zero and one values."""
    _validate_lengths(y_true, y_pred)
    if any(value not in (0, 1, False, True) for value in [*y_true, *y_pred]):
        raise ValueError("Dice inputs must be binary")
    intersection = sum(1 for truth, prediction in zip(y_true, y_pred) if truth == 1 and prediction == 1)
    total_positive = sum(int(value) for value in y_true) + sum(int(value) for value in y_pred)
    if total_positive == 0:
        return 1.0
    return float((2 * intersection) / total_positive)
