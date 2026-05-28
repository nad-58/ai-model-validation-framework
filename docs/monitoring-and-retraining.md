# Monitoring and Retraining Plan

## Monitoring signals

- Input data distribution changes
- Output distribution changes
- Performance trend where ground truth is available
- User feedback
- Complaint or incident reports
- Human override frequency
- Low-confidence output rate

## Investigation triggers

- Monitoring threshold exceeded
- Material reduction in performance metric
- Increase in failed quality-control cases
- Subgroup performance gap above predefined threshold
- New use environment, device, site, or data source

## Retraining decision logic

Retraining should be considered when monitoring evidence shows that current model behaviour no longer supports the intended use or acceptance criteria.

## Re-validation

Any model update, dataset update, threshold change, or intended-use change should be assessed for impact and may require partial or full re-validation.
