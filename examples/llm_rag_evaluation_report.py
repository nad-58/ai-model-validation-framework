from aimvf.llm_eval import (
    RAGEvaluationItem,
    aggregate_rag_evaluation,
    evaluate_rag_item,
)


def main() -> None:
    # Synthetic RAG/LLM evaluation examples.
    # These records demonstrate evaluation logic only and do not use client data.
    items = [
        RAGEvaluationItem(
            question="What evidence is needed before deploying a model update?",
            answer="The update should be assessed through change impact analysis, validation evidence, monitoring review, and human approval.",
            retrieved_sources=["change-control-procedure", "validation-plan"],
            expected_key_points=["impact analysis", "validation", "monitoring", "approval"],
            groundedness_score=0.92,
            relevance_score=0.95,
            completeness_score=0.86,
            unsupported_claims=0,
        ),
        RAGEvaluationItem(
            question="Can the AI output be used without human review?",
            answer="Yes, the model can always be used directly without review.",
            retrieved_sources=["human-oversight-policy"],
            expected_key_points=["human review", "override", "escalation"],
            groundedness_score=0.40,
            relevance_score=0.62,
            completeness_score=0.30,
            unsupported_claims=2,
            human_review_required=True,
        ),
    ]

    results = [evaluate_rag_item(item) for item in items]
    summary = aggregate_rag_evaluation(results)

    print("LLM/RAG evaluation report")
    print("=========================")

    for index, result in enumerate(results, start=1):
        print(f"\nItem {index}")
        print(f"Question: {result['question']}")
        print(f"Decision: {result['review_decision']}")
        print("Checks:")
        for check_name, passed in result["checks"].items():
            print(f"- {check_name}: {passed}")

    print("\nSummary")
    print(summary)

    print("\nInterpretation")
    if summary["review_required"] > 0:
        print(
            "At least one answer requires review. The validation team should inspect "
            "grounding, relevance, unsupported claims, source traceability, and whether "
            "human oversight is required before release."
        )
    else:
        print(
            "All evaluated answers passed the predefined checks. Results should still be "
            "documented with test-set coverage and known limitations."
        )


if __name__ == "__main__":
    main()
