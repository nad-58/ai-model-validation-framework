# Dataset Quality Review Template

## 1. Dataset overview

- Dataset name:
- Dataset version:
- Intended use:
- Data modality:
- Data source:
- Collection period:
- Dataset owner:
- Label or annotation source:

## 2. Representativeness

| Dimension | Evidence | Gap or limitation | Action |
|---|---|---|---|
| Target population or domain |  |  |  |
| Site or geography |  |  |  |
| Device, sensor, or protocol |  |  |  |
| Class balance |  |  |  |
| Rare cases and edge cases |  |  |  |
| Input quality variation |  |  |  |

## 3. Split integrity

- Split method:
- Unit of independence:
- Subject, user, or case-level separation:
- Duplicate records across splits:
- Near-duplicate records across splits:
- Model-selection leakage risk:

## 4. Data quality checks

| Check | Result | Status | Notes |
|---|---|---|---|
| Missing values |  | Open |  |
| Invalid values |  | Open |  |
| Out-of-range values |  | Open |  |
| Unknown categorical values |  | Open |  |
| Data type mismatch |  | Open |  |
| Corrupted files |  | Open |  |
| Duplicate records |  | Open |  |
| Label inconsistency |  | Open |  |

## 5. Leakage and proxy review

- Features generated after prediction time:
- Features derived from label:
- Identifier leakage:
- Timestamp leakage:
- Workflow artefact leakage:
- Proxy-sensitive variables:
- Feature-label correlation concerns:

## 6. Distribution review

- Training vs validation distribution:
- Training vs test distribution:
- Validation vs test distribution:
- Production/reference distribution:
- Feature drift concerns:
- Label distribution concerns:

## 7. Annotation quality

- Annotation guideline available:
- Annotator qualification:
- Number of annotators:
- Adjudication method:
- Inter-annotator agreement:
- Label error review:

## 8. Dataset decision

- Decision: Ready / Ready with limitations / Needs improvement / Not suitable for intended use
- Key evidence:
- Main limitations:
- Required actions:
- Reviewer:
- Date:
