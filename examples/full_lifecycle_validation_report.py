from aimvf.fairness import fairness_review_decision, metric_gap, subgroup_classification_summary
from aimvf.metrics import classification_summary
from aimvf.risk import risk_priority_number


def dataset_quality_review() -> dict:
    rows = [
        {"case_id": "C001", "feature_missing": False, "duplicate": False, "split": "test"},
        {"case_id": "C002", "feature_missing": False, "duplicate": False, "split": "test"},
        {"case_id": "C003", "feature_missing": True, "duplicate": False, "split": "test"},
        {"case_id": "C004", "feature_missing": False, "duplicate": True, "split": "test"},
        {"case_id": "C005", "feature_missing": False, "duplicate": False, "split": "test"},
    ]

    total = len(rows)
    missing_count = sum(row["feature_missing"] for row in rows)
    duplicate_count = sum(row["duplicate"] for row in rows)

    return {
        "total_records": total,
        "missing_feature_rate": missing_count / total,
        "duplicate_rate": duplicate_count / total,
        "split_review": "test split only in this synthetic example",
        "dataset_ready": missing_count <= 1 and duplicate_count <= 1,
    }


def confidence_review(y_true: list[int], y_pred: list[int], confidence: list[float]) -> dict:
    confident_errors = []
    for index, (truth, pred, score) in enumerate(zip(y_true, y_pred, confidence)):
        if truth != pred and score >= 0.80:
            confident_errors.append({"index": index, "truth": truth, "prediction": pred, "confidence": score})

    return {
        "mean_confidence": sum(confidence) / len(confidence),
        "confident_error_count": len(confident_errors),
        "confident_errors": confident_errors,
        "calibration_review_needed": len(confident_errors) > 0,
    }


def governance_decision(checks: dict[str, bool]) -> dict:
    failed = [name for name, passed in checks.items() if not passed]
    if not failed:
        decision = "acceptable_for_controlled_use"
    elif len(failed) <= 2:
        decision = "acceptable_with_actions"
    else:
        decision = "further_validation_required"

    return {
        "decision": decision,
        "passed_checks": sum(checks.values()),
        "total_checks": len(checks),
        "failed_checks": failed,
    }


def main() -> None:
    y_true = [1, 0, 1, 1, 0, 0, 1, 0]
    y_pred = [1, 0, 1, 0, 0, 1, 1, 0]
    confidence = [0.92, 0.81, 0.88, 0.84, 0.76, 0.91, 0.86, 0.79]
    subgroup = ["site_a", "site_a", "site_b", "site_b", "site_a", "site_b", "site_a", "site_b"]

    dataset = dataset_quality_review()
    metrics = classification_summary(y_true, y_pred)
    confidence_result = confidence_review(y_true, y_pred, confidence)
    subgroup_results = subgroup_classification_summary(y_true, y_pred, subgroup)
    subgroup_gap = metric_gap(subgroup_results, metric_name="recall_macro")
    fairness_decision = fairness_review_decision(subgroup_gap["absolute_gap"], investigation_threshold=0.20)
    risk = risk_priority_number(severity=4, occurrence=2, detectability=2)

    checks = {
        "dataset_quality_ready": dataset["dataset_ready"],
        "primary_metric_above_threshold": metrics["f1_macro"] >= 0.70,
        "no_material_subgroup_gap": fairness_decision == "no_investigation_required",
        "confidence_review_complete": True,
        "risk_level_not_high": risk["level"] != "high",
    }
    decision = governance_decision(checks)

    print("Full-lifecycle validation report")
    print("================================")
    print("\nDataset quality")
    print(dataset)
    print("\nModel performance")
    print(metrics)
    print("\nConfidence review")
    print(confidence_result)
    print("\nSubgroup performance")
    print(subgroup_results)
    print("\nSubgroup gap")
    print(subgroup_gap)
    print("\nRisk review")
    print(risk)
    print("\nGovernance decision")
    print(decision)


if __name__ == "__main__":
    main()
