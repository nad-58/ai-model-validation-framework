# LLM and RAG Evaluation

LLM and retrieval-augmented generation (RAG) systems require validation beyond conventional machine-learning accuracy metrics. Evaluation should test whether generated outputs are relevant, grounded in supplied evidence, traceable to sources, complete enough for the intended use, and safe for the operating context.

This document provides a lightweight evaluation structure for LLM/RAG systems used in workflow automation, summarisation, question answering, decision support, or human-in-the-loop review.

## Evaluation dimensions

| Dimension | Review question | Example evidence |
|---|---|---|
| Relevance | Does the answer address the user question? | Human scoring, rubric-based evaluation |
| Groundedness | Is the answer supported by retrieved sources? | Source-to-claim checking |
| Traceability | Can key claims be linked to source documents? | Citations, source IDs, retrieved passages |
| Completeness | Does the answer include required key points? | Expected key point checklist |
| Unsupported claims | Does the model introduce facts not present in evidence? | Hallucination / unsupported-claim review |
| Robustness | Does the output remain stable under prompt variations? | Prompt perturbation testing |
| Human oversight | Does the answer require review or approval before use? | Escalation and review policy |

## Suggested acceptance criteria

Acceptance criteria should be predefined before formal validation. A simple example is:

```text
Groundedness score >= 0.80
Relevance score >= 0.80
Completeness score >= 0.70
Unsupported claims = 0
Source traceability must be present
Human review required for uncertain, incomplete, or unsupported outputs
```

## Recommended validation workflow

1. Define the intended use of the LLM/RAG feature.
2. Define unacceptable outputs and misuse scenarios.
3. Build a representative test set of user questions and expected key points.
4. Record retrieved sources for each response.
5. Score relevance, groundedness, completeness, and unsupported claims.
6. Check source traceability for important claims.
7. Review failure modes and assign mitigations.
8. Define monitoring signals and escalation rules.
9. Document residual risk and release decision.

## Common failure modes

- Hallucinated or unsupported statements
- Correct answer but wrong or missing source traceability
- Overconfident answer when evidence is weak
- Incomplete answer for complex user tasks
- Misinterpretation of retrieved documents
- Prompt sensitivity or inconsistent output
- Failure to refuse out-of-scope requests
- Unsafe automation without human review

## Possible mitigations

- Improve retrieval quality and document chunking
- Add source citation requirements
- Add answer abstention rules
- Use stricter system prompts and guardrails
- Add human review before high-impact use
- Add confidence or evidence-quality thresholds
- Expand evaluation test sets
- Monitor user feedback and override rates

## Documentation expectation

A validation report should include the test-set design, scoring rubric, acceptance criteria, evaluation results, failure analysis, mitigations, monitoring plan, and release decision.
