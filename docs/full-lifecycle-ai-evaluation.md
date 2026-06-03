# Full-Lifecycle AI Model and Dataset Evaluation

## 1. Purpose

Machine learning systems are often developed under the assumption that training, validation, testing, and deployment data follow similar distributions. In practice, this assumption is frequently violated after deployment. Real-world data can shift, input quality can degrade, labels may be delayed or unavailable, user behaviour may change, and models may produce confident but incorrect predictions.

This document provides a generic framework for evaluating AI systems across the full lifecycle, including dataset quality, model performance, explainability, calibration, subgroup performance, robustness, error analysis, model comparison, monitoring, and governance decisions.

The purpose is to move beyond a narrow focus on training accuracy and provide structured evidence that an AI system is reliable, maintainable, and appropriate for its intended use.

## 2. Evaluation scope

This framework can be applied to several AI system types:

- Tabular classification and regression models
- Image classification models
- Object detection models
- Semantic segmentation models
- Time-series models
- Text and LLM-based systems
- Retrieval-augmented generation systems
- Multimodal AI systems

The evaluation should be adapted to the intended use, risk level, data modality, deployment environment, and user workflow.

## 3. Key evaluation principles

### 3.1 Overall performance is not enough

A single metric such as accuracy, AUC, mean squared error, Dice score, or F1 score does not provide enough evidence for real-world reliability. A model may perform well on average while failing on important subgroups, rare cases, low-quality inputs, or shifted data distributions.

### 3.2 Evaluation must include dataset quality

Model performance depends heavily on the quality and representativeness of the dataset. Dataset evaluation should include missingness, duplicates, invalid values, label quality, leakage, distribution mismatch, subgroup coverage, and sensitive or proxy-sensitive variables.

### 3.3 Deployment reliability requires monitoring

AI systems can degrade after deployment because input data, user behaviour, acquisition devices, clinical practice, operational conditions, or external environments may change. Monitoring should therefore include data drift, prediction drift, performance signals, human feedback, incidents, and change-control triggers.

### 3.4 Model updates require comparison and regression testing

A new model version should not only be assessed against the overall performance of the previous model. It should also be checked for new errors, changed predictions, performance regressions on important cases, subgroup changes, and compatibility with downstream workflows.

### 3.5 Human oversight should be risk-based

Where AI outputs influence important decisions, evaluation should define when users can rely on the output, when human review is required, and when escalation is necessary.

## 4. Recommended report structure

A full AI model evaluation report should include:

1. Model and dataset overview
2. Intended use and operating context
3. Dataset quality and representativeness
4. Train/validation/test split integrity
5. Duplicate and leakage checks
6. Model performance metrics
7. Calibration and confidence reliability
8. Prediction distribution analysis
9. Subgroup and segment-level performance
10. Error analysis and top failure modes
11. Robustness and perturbation testing
12. Explainability and model behaviour review
13. Model comparison and regression testing
14. Drift monitoring and invalid-input detection
15. Human review and governance decision
16. Change-control and re-validation triggers

## 5. Dataset evaluation

### 5.1 Dataset overview

The dataset review should describe dataset purpose, intended use, data source, data modality, collection period, inclusion and exclusion criteria, target population or operating environment, label or annotation process, dataset version, and known limitations.

### 5.2 Data representativeness

The dataset should be assessed for how well it represents the intended-use environment. This may include population coverage, device or acquisition-site coverage, geographic coverage, environmental conditions, input-quality variation, class balance, rare-case coverage, and edge-case representation.

### 5.3 Train/validation/test split integrity

The split strategy should prevent leakage and support reliable evaluation. Review questions include:

- Are training, validation, and test sets clearly separated?
- Is the test set independent from model development?
- Are repeated measurements from the same subject, user, device, site, or case kept within the same split where appropriate?
- Are duplicates removed or controlled?
- Is the test set representative of the intended-use environment?
- Are model-selection decisions separated from final test evaluation?

### 5.4 Missing, invalid, and out-of-range inputs

The dataset should be checked for invalid inputs, including missing required features, values outside expected ranges, unknown categorical values, incorrect data types, corrupted files, unexpected image sizes or formats, invalid timestamps, inconsistent units, and implausible values.

### 5.5 Duplicate and near-duplicate data

Duplicate data can cause overoptimistic performance estimates if similar or identical samples appear across splits. Evaluation should include exact duplicate checks, partial duplicate checks using key identifiers, near-duplicate image or text checks where relevant, cross-split duplicate analysis, and subject-level or case-level leakage analysis.

### 5.6 Correlation and leakage review

Feature-label correlations and feature-feature relationships should be reviewed to identify possible information leakage. High correlation with the label may be legitimate, but it can also indicate that a feature contains information unavailable at prediction time.

Review questions include:

- Are any features derived from the target label?
- Are any features generated after the prediction time point?
- Are identifiers, timestamps, or workflow artefacts acting as shortcuts?
- Do training and test datasets have materially different feature correlations?
- Are proxy variables unintentionally encoding sensitive characteristics?

## 6. Model performance evaluation

### 6.1 Classification metrics

For classification systems, the report may include accuracy, precision, recall, specificity, F1 score, F-beta score, AUROC, AUPRC, false positive rate, false negative rate, confusion matrix, balanced accuracy, class-wise metrics, and macro, micro, or weighted averages.

The selected metrics should reflect the intended use. For example, false negatives may be more important in screening applications, while false positives may be more important where unnecessary intervention causes harm or operational burden.

### 6.2 Regression metrics

For regression systems, the report may include mean absolute error, mean squared error, root mean squared error, mean absolute percentage error, error distribution, prediction distribution, residual analysis, outlier analysis, and performance across target-value ranges.

A regression model should not only minimise average error. Its prediction distribution should also be compared with the true-label distribution to confirm that the model covers the real range of expected values.

### 6.3 Object detection metrics

For object detection systems, the report may include precision, recall, localization quality, intersection over union, class confusion, missed detections, background detections, duplicate detections, per-class detection performance, and performance by object size, occlusion, and image quality.

### 6.4 Segmentation metrics

For segmentation systems, the report may include Dice coefficient, intersection over union, pixel-level precision and recall, per-class segmentation performance, boundary error, small-structure performance, and false-positive or false-negative mask analysis.

### 6.5 Text and LLM evaluation metrics

For text or LLM-based systems, evaluation may include answer relevance, factual consistency, groundedness, completeness, source traceability, unsupported-claim rate, conciseness, refusal appropriateness, human preference alignment, and automated metric versus manual review agreement.

For retrieval-augmented systems, evaluation should also include retrieval quality and whether generated claims are supported by retrieved sources.

## 7. Calibration and confidence reliability

Many models produce probability or confidence scores. These scores should be evaluated to determine whether they are reliable.

Calibration review asks:

- When the model predicts 90% confidence, is it correct approximately 90% of the time?
- Are high-confidence errors present?
- Are probabilities useful for human decision-making?
- Does calibration vary across subgroups?
- Does calibration degrade after deployment or model update?

Possible evidence includes calibration curves, expected calibration error, confidence distribution, high-confidence error review, calibration by subgroup, and threshold sensitivity analysis.

Poor calibration may require calibration methods, threshold adjustment, user-interface changes, or additional human review.

## 8. Prediction distribution analysis

Prediction distributions should be compared against true-label or expected-output distributions.

For classification systems, this may include distribution of predicted classes, distribution of prediction probabilities, class imbalance effects, overconfident predictions, and under-predicted classes.

For regression systems, this may include predicted-value distribution, true-label distribution, range coverage, tail performance, and extreme-case performance.

A model whose predictions are too narrow or concentrated may fail to represent real-world variation.

## 9. Subgroup and segment-level analysis

Subgroup and segment-level evaluation identifies areas where the model performs worse than the average.

Possible segment variables include age group, sex or gender where appropriate, geography, site or device, acquisition protocol, lighting or image quality, sensor type, disease severity or case complexity, input length or prompt category, user group, and operational environment.

The report should include performance for each segment, segment sample size, comparison against overall performance, comparison against predefined thresholds, gap analysis between best and worst segments, investigation of materially low-performing segments, and mitigation or monitoring plans.

Segment-level analysis is important because an acceptable overall metric can hide unacceptable performance on a clinically, operationally, or ethically important subgroup.

## 10. Error analysis

Error analysis should identify and explain the model's most important failures.

### 10.1 Classification errors

For classification systems, review the confusion matrix, top false positives, top false negatives, high-confidence wrong predictions, class confusion patterns, error distribution by subgroup, and error distribution by input quality.

### 10.2 Regression errors

For regression systems, review largest positive errors, largest negative errors, error distribution, extreme target-value errors, errors by subgroup or segment, and systematic overprediction or underprediction.

### 10.3 Object detection errors

For object detection systems, review missed objects, background false detections, class confusion, localization failures, small-object failures, occlusion-related failures, and image-quality-related failures.

### 10.4 Dataset errors

Some apparent model errors may be caused by incorrect labels or annotation inconsistency. The evaluation should include a process for detecting and reviewing potential label errors.

## 11. Explainability and model behaviour review

Explainability evidence should help reviewers understand what the model appears to rely on.

Possible methods include global feature importance, local explanation for individual predictions, perturbation-based explanations, counterfactual examples, occlusion sensitivity for images, feature or token contribution analysis, and human review of explanation plausibility.

Review questions include:

- Does the model rely on plausible features?
- Are there features with suspiciously high importance?
- Are low-importance features unnecessary or noisy?
- Does the model rely on background, metadata, or shortcut signals?
- Are explanations stable across similar inputs?
- Are explanations understandable for the intended user?

Explainability should not be treated as proof of correctness, but it can support model debugging, risk analysis, and user oversight.

## 12. Robustness testing

Robustness testing evaluates whether model behaviour remains acceptable under realistic input variation.

### 12.1 Tabular robustness

Tabular robustness may include missing feature simulation, out-of-range input testing, categorical value shift, noise injection, input unit errors, feature perturbation, and stress testing rare combinations.

### 12.2 Image robustness

Image robustness may include brightness changes, darkening, blur, noise, pixelation, rotation, occlusion, compression, contrast variation, camera artefacts, and environmental artefacts.

Robustness should be measured by comparing performance before and after perturbation. The report should define acceptable performance degradation thresholds.

### 12.3 Text and LLM robustness

Text robustness may include rephrased prompts, ambiguous prompts, long prompts, missing context, conflicting instructions, prompt injection attempts, out-of-scope requests, and low-quality retrieved sources.

The evaluation should confirm that the system remains grounded, relevant, and safe under prompt variation.

## 13. Model comparison and regression testing

When a model is retrained or updated, it should be compared with the previous version.

Comparison should include overall performance difference, segment-level performance difference, new errors introduced by the updated model, cases improved by the updated model, prediction changes, high-impact prediction changes, calibration changes, robustness changes, and compatibility with downstream workflows.

A new model should not be accepted only because its average performance improves. It may still introduce unacceptable regressions on important cases or subgroups.

## 14. Data drift, prediction drift, and monitoring

Post-deployment monitoring should detect changes that may affect reliability.

### 14.1 Data drift

Data drift occurs when input feature distributions change compared with the reference dataset. Monitoring may include numeric feature distribution changes, categorical frequency changes, image quality changes, text topic changes, missingness changes, invalid input rate, and correlation changes.

### 14.2 Prediction drift

Prediction drift occurs when model outputs change over time. Monitoring may include predicted class distribution, confidence distribution, output score distribution, positive prediction rate, refusal or escalation rate, and generated answer categories.

Prediction drift can indicate changes in data, behaviour, system configuration, or model suitability.

### 14.3 Label drift

Label drift occurs when the distribution of ground truth outcomes changes. It is often harder to monitor because labels may be delayed or unavailable.

### 14.4 Invalid input monitoring

Invalid input monitoring should detect missing required fields, unknown categories, out-of-range values, corrupted images or files, unexpected data types, unexpected input length, unsupported input format, and duplicate or repeated inputs.

## 15. Data cards and model cards

### 15.1 Dataset documentation

A dataset card should include dataset name and version, intended use, out-of-scope use, data source, collection process, labeling or annotation process, data quality checks, sensitive or proxy-sensitive attributes, known limitations, update process, and downstream usage.

### 15.2 Model documentation

A model card should include model name and version, intended use, out-of-scope use, input and output description, training data summary, model architecture or method, training process, validation strategy, performance metrics, subgroup performance, robustness results, explainability evidence, known limitations, human oversight requirements, monitoring, and change-control plan.

### 15.3 System documentation for LLM applications

For LLM systems, a system card should include base model or model provider, prompt design, retrieval design, knowledge sources, guardrails, evaluation dataset, automated and manual evaluation metrics, groundedness and traceability evidence, human review policy, monitoring, and update triggers.

## 16. Human review and governance decision

The evaluation report should end with a clear governance decision.

Possible decisions include:

- Acceptable for controlled use
- Acceptable with monitoring
- Acceptable only for limited use
- Further validation required
- Dataset improvement required
- Model update required
- Human review required before use
- Not acceptable for deployment

The decision should be linked to evidence, residual risk, limitations, and required follow-up actions.

## 17. Change control and re-validation triggers

Re-validation should be considered when there is a change to model architecture, model weights, training data, validation data, input features, output format, thresholds, preprocessing, post-processing, prompt templates, retrieval pipeline, knowledge base, deployment environment, intended use, user workflow, target population, or operating conditions.

The level of re-validation should be proportional to the expected impact of the change.

## 18. Recommended repository mapping

### AI Model Validation Framework

Recommended additions:

- Full-lifecycle AI evaluation report
- Dataset evaluation and leakage checklist
- Calibration and error analysis documentation
- Model comparison and regression testing template
- Generic validation report template

### Edge AI Computer Vision Deployment

Recommended additions:

- Image robustness testing plan
- Computer vision error-analysis report
- Object detection evaluation checklist
- Segmentation evaluation checklist
- Hardware-aware robustness and input-quality template

### LLM RAG Evaluation Governance

Recommended additions:

- Text and LLM evaluation workflow
- Automated versus manual evaluation guide
- Metric threshold and pass-rate template
- Human annotation template
- Model comparison template for generated outputs

### Medical AI Governance Toolkit

Recommended additions:

- Post-deployment model reliability review
- Clinical AI model review report template
- Monitoring and re-validation trigger checklist
- Subgroup and error-analysis governance template
