# AI Risk Register Template

| ID | Hazard / failure mode | Cause | Impact | Existing control | Severity | Occurrence | Detectability | RPN | Mitigation | Owner | Status |
|---|---|---|---|---|---:|---:|---:|---:|---|---|---|
| R-001 | Incorrect model output | Dataset shift or low-quality input | Wrong decision support | Human review and confidence threshold | 4 | 3 | 2 | 24 | Add monitoring and subgroup review | AI lead | Open |
| R-002 | Biased subgroup performance | Under-represented validation subgroup | Unequal performance | Subgroup analysis | 4 | 2 | 3 | 24 | Improve dataset coverage | Data lead | Open |
