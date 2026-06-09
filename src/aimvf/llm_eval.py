from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class RAGEvaluationItem:
    """Single RAG/LLM evaluation record.

    Scores use a zero-to-one scale where higher is better, except
    ``unsupported_claims``, where lower is better.
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


def _validate_unit_interval(name: str, value: float) -> None:
    if value < 0.0 or value > 1.0:
        raise ValueError(f"{name} must be between 0 and 1")


def evaluate_rag_item(
    item: RAGEvaluationItem,
    min_groundedness: float = 0.80,
    min_relevance: float = 0.80,
    min_completeness: float = 0.70,
    max_unsupported_claims: int = 0,
) -> dict:
    """Apply transparent acceptance criteria to one RAG/LLM item."""
    if not item.question.strip():
        raise ValueError("question must not be empty")
    if item.unsupported_claims < 0:
        raise ValueError("unsupported_claims must not be negative")
    if max_unsupported_claims < 0:
        raise ValueError("max_unsupported_claims must not be negative")

    for name, value in {
        "groundedness_score": item.groundedness_score,
        "relevance_score": item.relevance_score,
        "completeness_score": item.completeness_score,
        "min_groundedness": min_groundedness,
        "min_relevance": min_relevance,
        "min_completeness": min_completeness,
    }.items():
        _validate_unit_interval(name, value)

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
    accepted = sum(1 for result in results if bool(result.get("passed")))
    review_required = total - accepted
    return {
        "total_items": total,
        "accepted": accepted,
        "review_required": review_required,
        "acceptance_rate": accepted / total if total else 0.0,
    }
