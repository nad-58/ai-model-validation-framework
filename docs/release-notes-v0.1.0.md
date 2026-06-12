# Release notes — v0.1.0

## AI Model Validation Framework

Initial public release of a practical, public-safe framework for validating AI and machine learning systems across the lifecycle.

### Included

- Dataset quality and leakage review guidance
- Classification and regression validation utilities
- Calibration and error-analysis documentation
- Fairness and subgroup evaluation examples
- LLM/RAG evaluation example
- Full-lifecycle synthetic validation report
- Monitoring, retraining, and change-control guidance
- Reusable model, dataset, risk, and regression-testing templates
- Python package metadata and automated validation examples

### Public-safe boundary

The release uses synthetic and generic material only. It excludes confidential client information, patient data, employer documentation, proprietary product evidence, and restricted assessment content.

### Validation before release

```bash
python -m compileall -q src tests examples
python -m pytest tests -q
python -m build
python -m twine check dist/*
```

### Suggested GitHub release title

```text
v0.1.0 — Initial Public Validation Framework
```
