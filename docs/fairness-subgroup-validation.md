# Fairness and Subgroup Validation

Fairness and subgroup validation assesses whether model performance remains acceptable across relevant populations, operating conditions, devices, sites, or input-quality groups.

This type of review is important because a model may meet the overall acceptance criterion while performing materially worse for a clinically, operationally, or ethically relevant subgroup.

## Typical subgroup variables

Subgroup variables should be selected based on the intended use and risk profile of the system. Examples include:

- Age group
- Sex or gender where relevant and justified
- Ethnicity where legally, ethically, and operationally appropriate
- Imaging device, scanner, sensor, or acquisition protocol
- Clinical site or geography
- Lighting, noise, blur, compression, or input-quality group
- Disease severity or case complexity
- Hardware or deployment environment

## Recommended validation steps

1. Define relevant subgroup variables before validation.
2. Confirm that subgroup labels are reliable and ethically appropriate to use.
3. Report sample size for each subgroup.
4. Calculate primary and secondary performance metrics for each subgroup.
5. Compare each subgroup against the predefined acceptance criterion.
6. Calculate between-subgroup performance gaps.
7. Define an investigation threshold for material gaps.
8. Investigate root causes when gaps exceed the threshold.
9. Document mitigations, residual risk, and monitoring needs.

## Example acceptance logic

A project may define two layers of fairness acceptance:

1. Each subgroup must meet the minimum performance requirement.
2. The absolute performance gap between the best and worst subgroup must not exceed a predefined threshold.

Example:

```text
Each subgroup recall must be >= 0.80
Absolute recall gap between subgroups must be <= 0.10
```

If either condition fails, the validation team should investigate before release.

## Investigation questions

When subgroup disparity is observed, reviewers should consider:

- Is the subgroup sample size too small?
- Is the subgroup under-represented in training or validation data?
- Is there label noise or inconsistent annotation quality?
- Are acquisition conditions different between subgroups?
- Are there hidden confounders such as site, device, protocol, or operator?
- Does the model fail on a specific phenotype, visual pattern, or input-quality condition?
- Is the intended use still appropriate for all subgroups?

## Possible mitigations

- Improve dataset coverage
- Add targeted data collection
- Improve annotation quality control
- Adjust model training strategy
- Add subgroup-specific monitoring
- Add user warnings or limitations
- Restrict intended use where evidence is insufficient
- Perform further independent validation

## Documentation expectation

The validation report should document the subgroup definition, sample size, metrics, acceptance criteria, gap analysis, investigation outcome, mitigation actions, and residual risk decision.
