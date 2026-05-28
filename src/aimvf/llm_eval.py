from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class RAGEvaluationItem:
    """Single RAG/LLM evaluation record.

    Scores use a 0-1 scale where higher is better, except unsupported_claims,
    where lower is better.
    """

    question: str
    answer: str
    retrieved_sources: Sequence[str]
    expected_key_points: Sequence[str]
    groundedness_score: float
    relevance_score: float
    completeness_score: float
    unsupported_claims: int
    human_review_required: bool = False


def evaluate_rag_item(
    item: RAGEvaluationItem,
    min_groundedness: float = 0.80,
    min_relevance: float = 0.80,
    min_completeness: float = 0.70,
    max_unsupported_claims: int = 0,
) -> dict:
    """Apply simple acceptance criteria to a RAG/LLM evaluation item."""
    checks = {
        "groundedness_pass": item.groundedness_score >= min_groundedness,
        "relevance_pass": item.relevance_score >= min_relevance,
        "completeness_pass": item.completeness_score >= min_completeness,
        "unsupported_claims_pass": item.unsupported_claims <= max_unsupported_claims,
        "source_traceability_present": len(item.retrieved_sources) > 0,
    }
    passed = all(checks.values()) and not item.human_review_required
    return {
        "question": item.question,
        "checks": checks,
        "passed": passed,
        "review_decision": "accepted" if passed else "review_required",
    }


def aggregate_rag_evaluation(results: Sequence[dict]) -> dict:
    """Summarise RAG/LLM evaluation decisions across multiple items."""
    total = len(results)
    accepted = sum(1 for result in results if result["passed"])
    review_required = total - accepted
    return {
        "total_items": total,
        "accepted": accepted,
        "review_required": review_required,
        "acceptance_rate": accepted / total if total else 0.0,
    }
