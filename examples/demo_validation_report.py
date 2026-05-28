from aimvf.metrics import classification_summary, dice_score
from aimvf.risk import risk_priority_number


def main() -> None:
    y_true = [1, 0, 1, 1, 0, 0]
    y_pred = [1, 0, 1, 0, 0, 1]

    print("Classification validation summary")
    print(classification_summary(y_true, y_pred))

    print("\nBinary segmentation Dice example")
    print({"dice": dice_score(y_true, y_pred)})

    print("\nRisk assessment example")
    print(risk_priority_number(severity=4, occurrence=3, detectability=2))


if __name__ == "__main__":
    main()
