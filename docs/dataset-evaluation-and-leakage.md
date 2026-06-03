# Dataset Evaluation and Leakage Review

Dataset evaluation is a core part of AI model validation. A model can appear to perform well while relying on leakage, duplicates, shortcuts, or unrepresentative data.

## Review objectives

- Confirm that the dataset is representative of the intended use.
- Confirm that training, validation, and test sets are independent.
- Identify duplicates and near-duplicates across splits.
- Detect features that leak label information.
- Identify proxy variables that may encode sensitive or operationally inappropriate information.
- Confirm that labels or annotations are reliable enough for evaluation.

## Split integrity checks

A robust split strategy should define the unit of independence. Depending on the domain, this may be:

- Subject or patient
- User or customer
- Device or sensor
- Site or acquisition centre
- Case or study
- Time period
- Operational event

Repeated samples from the same unit should normally remain within the same split where leakage could otherwise inflate performance.

## Leakage review questions

- Was the test set used during model selection?
- Are duplicate records present across train, validation, and test sets?
- Are identifiers, timestamps, filenames, or workflow artefacts predictive of the label?
- Are any features generated after the intended prediction time?
- Are any features derived directly or indirectly from the target label?
- Are preprocessing steps fitted only on training data before being applied to validation or test data?
- Are labels or annotations generated using information unavailable at deployment?

## Distribution review

Training, validation, test, and deployment data should be compared across:

- Numeric feature distributions
- Categorical value frequencies
- Missingness rates
- Label distribution
- Class balance
- Input quality indicators
- Site/device/protocol coverage
- Subgroup coverage
- Correlation structure

Material distribution differences should be investigated and documented.

## Duplicate and near-duplicate review

Duplicate review should include:

- Exact duplicate records
- Partial duplicates using key identifiers
- Repeated measurements from the same subject or case
- Similar or near-identical images
- Reused text prompts or outputs
- Repeated time-series windows from the same event

Duplicates are not always wrong, but they must be understood and controlled.

## Output of the review

The dataset review should conclude whether the dataset is ready for model evaluation, ready with limitations, requires improvement, or is not suitable for the intended validation purpose.
