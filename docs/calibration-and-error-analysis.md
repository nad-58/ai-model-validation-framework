# Calibration and Error Analysis

Calibration and error analysis help determine whether model outputs are reliable, interpretable, and appropriate for the intended use.

## Calibration review

Calibration evaluates whether predicted probabilities or confidence scores correspond to observed correctness.

Review questions:

- When the model predicts high confidence, is it usually correct?
- Are confident incorrect outputs present?
- Does calibration vary across subgroups or sites?
- Does calibration change after model updates?
- Are probability thresholds justified for the intended workflow?
- Are users likely to over-rely on confidence scores?

## Evidence to include

- Calibration curve
- Expected calibration error or equivalent metric
- Confidence distribution
- Threshold sensitivity analysis
- Review of confident incorrect outputs
- Calibration by subgroup or segment

## Error analysis review

Error analysis identifies the most important model failures and whether they are acceptable for the intended use.

Classification review should include:

- Confusion matrix
- Positive-class error review
- Negative-class error review
- Confident incorrect predictions
- Class confusion patterns
- Error concentration by subgroup or input quality

Regression review should include:

- Largest positive residuals
- Largest negative residuals
- Error distribution
- Extreme target-value errors
- Systematic overprediction or underprediction

Computer vision review should include:

- Missed objects or regions
- Background detections
- Class confusion
- Localization issues
- Segmentation boundary issues
- Low-quality input failures

Text and LLM review should include:

- Unsupported claims
- Missing key points
- Poor relevance
- Weak source traceability
- Overconfident answers
- Refusal or escalation issues

## Reviewer conclusion

The reviewer should identify whether errors are random, systematic, concentrated in important subgroups, linked to dataset limitations, linked to poor calibration, or caused by potential label issues.
