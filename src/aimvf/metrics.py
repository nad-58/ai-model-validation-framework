from __future__ import annotations

from typing import Sequence

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


def classification_summary(y_true: Sequence[int], y_pred: Sequence[int]) -> dict:
    """Return a compact binary/multiclass classification validation summary."""
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision_macro": float(precision_score(y_true, y_pred, average="macro", zero_division=0)),
        "recall_macro": float(recall_score(y_true, y_pred, average="macro", zero_division=0)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
    }


def dice_score(y_true: Sequence[int], y_pred: Sequence[int]) -> float:
    """Calculate Dice score for binary segmentation masks represented as 0/1 arrays."""
    intersection = sum(1 for a, b in zip(y_true, y_pred) if a == 1 and b == 1)
    total_positive = sum(y_true) + sum(y_pred)
    if total_positive == 0:
        return 1.0
    return float((2 * intersection) / total_positive)
