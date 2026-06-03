# Model Comparison and Regression Testing Template

## 1. Comparison overview

- Baseline model:
- Candidate model:
- Reason for update:
- Intended-use change: Yes / No
- Dataset used for comparison:
- Reviewer:
- Date:

## 2. Overall performance comparison

| Metric | Baseline | Candidate | Difference | Status | Notes |
|---|---:|---:|---:|---|---|
| Primary metric |  |  |  | Open |  |
| Secondary metric 1 |  |  |  | Open |  |
| Secondary metric 2 |  |  |  | Open |  |
| Calibration metric |  |  |  | Open |  |

## 3. Subgroup comparison

| Segment | Baseline metric | Candidate metric | Difference | Concern? | Notes |
|---|---:|---:|---:|---|---|
| Overall |  |  |  |  |  |
| Segment A |  |  |  |  |  |
| Segment B |  |  |  |  |  |

## 4. Prediction-change review

- Number of changed predictions:
- Percentage of changed predictions:
- Largest changes:
- High-impact changes:
- Changes requiring review:

## 5. New error review

| Case ID | Baseline result | Candidate result | Error type | Impact | Action |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 6. Improved case review

| Case ID | Baseline result | Candidate result | Improvement type | Notes |
|---|---|---|---|---|
|  |  |  |  |  |

## 7. Compatibility assessment

- Does the candidate model preserve expected behaviour on important cases?
- Are downstream workflows affected?
- Are thresholds, outputs, or confidence scores changed?
- Does documentation need updating?
- Is partial or full re-validation required?

## 8. Decision

- Decision: Accept candidate / Accept with monitoring / Further validation required / Keep baseline
- Rationale:
- Required actions:
- Approval:
