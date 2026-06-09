import pytest

from aimvf.metrics import classification_summary, dice_score


def test_classification_summary():
    result = classification_summary([1, 0, 1, 0], [1, 0, 0, 0])
    assert result["accuracy"] == 0.75
    assert result["confusion_matrix"] == [[2, 0], [1, 1]]


def test_classification_summary_length_check():
    with pytest.raises(ValueError):
        classification_summary([1, 0], [1])


def test_classification_summary_empty_check():
    with pytest.raises(ValueError):
        classification_summary([], [])


def test_dice_score():
    assert dice_score([1, 1, 0, 0], [1, 0, 1, 0]) == 0.5
    assert dice_score([0, 0], [0, 0]) == 1.0


def test_dice_score_binary_check():
    with pytest.raises(ValueError):
        dice_score([0, 2], [0, 1])
