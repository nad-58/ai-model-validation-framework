import pytest

from aimvf.llm_eval import RAGEvaluationItem, aggregate_rag_evaluation, evaluate_rag_item


def make_item(**overrides):
    values = {
        "question": "What evidence supports the answer?",
        "answer": "The answer is supported by the supplied sources.",
        "retrieved_sources": ["source-a"],
        "expected_key_points": ["evidence"],
        "groundedness_score": 0.9,
        "relevance_score": 0.9,
        "completeness_score": 0.8,
        "unsupported_claims": 0,
    }
    values.update(overrides)
    return RAGEvaluationItem(**values)


def test_rag_item_passes():
    result = evaluate_rag_item(make_item())
    assert result["passed"] is True
    assert result["review_decision"] == "accepted"


def test_rag_item_requires_review():
    result = evaluate_rag_item(make_item(groundedness_score=0.4))
    assert result["passed"] is False
    assert result["review_decision"] == "review_required"


def test_rag_item_requires_traceability():
    result = evaluate_rag_item(make_item(retrieved_sources=[]))
    assert result["checks"]["source_traceability_present"] is False


def test_rag_input_validation():
    with pytest.raises(ValueError):
        evaluate_rag_item(make_item(question=""))
    with pytest.raises(ValueError):
        evaluate_rag_item(make_item(groundedness_score=1.1))
    with pytest.raises(ValueError):
        evaluate_rag_item(make_item(unsupported_claims=-1))


def test_rag_aggregation():
    results = [evaluate_rag_item(make_item()), evaluate_rag_item(make_item(relevance_score=0.2))]
    summary = aggregate_rag_evaluation(results)
    assert summary == {
        "total_items": 2,
        "accepted": 1,
        "review_required": 1,
        "acceptance_rate": 0.5,
    }
