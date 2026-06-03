# Model Evaluation Report Template

## 1. Model and system overview

- Model name:
- Model version:
- Use case:
- Intended users:
- Input data:
- Output:
- Decision impact:
- Deployment environment:

## 2. Intended use and limitations

- Intended use:
- Out-of-scope use:
- Target population / operating context:
- Known limitations:
- Human oversight requirements:

## 3. Dataset summary

| Dataset | Purpose | Source | Size | Date range | Notes |
|---|---|---|---:|---|---|
| Training | Model development |  |  |  |  |
| Validation | Model selection |  |  |  |  |
| Test | Final evaluation |  |  |  |  |

## 4. Data quality review

- Missing values:
- Invalid values:
- Duplicate records:
- Label quality:
- Split leakage review:
- Subgroup coverage:
- Distribution mismatch:

## 5. Performance metrics

| Metric | Result | Acceptance criterion | Status | Notes |
|---|---:|---:|---|---|
| Accuracy / primary metric |  |  | Open |  |
| Precision |  |  | Open |  |
| Recall / sensitivity |  |  | Open |  |
| Specificity |  |  | Open |  |
| F1 / Dice / task metric |  |  | Open |  |

## 6. Calibration and confidence

- Calibration method:
- Calibration metric:
- High-confidence error review:
- Threshold sensitivity:
- User interpretation risk:

## 7. Subgroup and segment performance

| Segment | N | Primary metric | Gap vs overall | Acceptance met? | Notes |
|---|---:|---:|---:|---|---|
| Overall |  |  |  |  |  |
| Segment A |  |  |  |  |  |
| Segment B |  |  |  |  |  |

## 8. Error analysis

- Top false positives:
- Top false negatives:
- High-confidence errors:
- Class confusion:
- Edge cases:
- Potential label errors:

## 9. Robustness testing

| Test | Result | Acceptance criterion | Status | Notes |
|---|---:|---:|---|---|
| Input noise / perturbation |  |  | Open |  |
| Missing / invalid input |  |  | Open |  |
| Low-quality input |  |  | Open |  |
| Out-of-distribution input |  |  | Open |  |

## 10. Explainability and behaviour review

- Global explanation method:
- Local explanation method:
- Shortcut or leakage signals:
- Human interpretability:
- Explanation limitations:

## 11. Monitoring and change control

- Monitoring signals:
- Drift indicators:
- Investigation triggers:
- Re-validation triggers:
- Model update process:

## 12. Governance decision

- Decision: Accept / Accept with monitoring / Limited use / Further validation required / Not acceptable
- Key evidence:
- Open risks:
- Required mitigations:
- Reviewer:
- Date:
