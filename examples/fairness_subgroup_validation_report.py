from aimvf.fairness import (
    fairness_review_decision,
    metric_gap,
    subgroup_classification_summary,
)


def main() -> None:
    # Synthetic example: binary decision-support model output.
    # In a real validation project, subgroup variables should be justified by
    # the intended use, clinical/operational risk, and dataset characteristics.
    y_true = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    y_pred = [1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0]
    age_group = [
        "under_50",
        "under_50",
        "under_50",
        "under_50",
        "50_and_over",
        "50_and_over",
        "50_and_over",
        "50_and_over",
        "50_and_over",
        "50_and_over",
        "under_50",
        "under_50",
    ]

    subgroup_results = subgroup_classification_summary(
        y_true=y_true,
        y_pred=y_pred,
        subgroup=age_group,
    )

    recall_gap = metric_gap(subgroup_results, metric_name="recall_macro")
    decision = fairness_review_decision(
        metric_gap_value=recall_gap["absolute_gap"],
        investigation_threshold=0.10,
    )

    print("Fairness and subgroup validation report")
    print("=======================================")
    print("\nSubgroup results")
    for group_name, values in subgroup_results.items():
        print(f"- {group_name}: n={values['n']}, recall_macro={values['recall_macro']:.3f}, f1_macro={values['f1_macro']:.3f}")

    print("\nGap analysis")
    print(recall_gap)

    print("\nReview decision")
    print(decision)

    print("\nInterpretation")
    if decision == "investigation_required":
        print(
            "The predefined subgroup performance gap threshold was exceeded. "
            "A reviewer should investigate data coverage, subgroup sample size, "
            "label quality, failure modes, and potential mitigations before release."
        )
    else:
        print(
            "The subgroup gap did not exceed the predefined investigation threshold. "
            "The result should still be documented with sample size limitations."
        )


if __name__ == "__main__":
    main()
