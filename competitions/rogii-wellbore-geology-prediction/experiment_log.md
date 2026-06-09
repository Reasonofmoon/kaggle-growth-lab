# ROGII Experiment Log

## exp_000_workspace_setup

Date: 2026-06-09

### Hypothesis

ROGII is a strong standard ML portfolio track because it supports EDA, validation design, regression baselines, and feature engineering.

### Change

- Added ROGII workspace
- Added dataset notes
- Added baseline plan
- Added notebook submission checklist

### Result

| Item | Status |
|---|---|
| Competition joined | TODO |
| Rules accepted | TODO |
| Dataset inspected | TODO |
| Baseline notebook created | TODO |
| First submission | TODO |

### Interpretation

The key risk is validation leakage. A random row split will likely overstate model quality because rows within a well are strongly correlated.

### Decision

Start with EDA and a simple `TVT_input` interpolation baseline before training a model.

---

## exp_001_submission_shape

Date:

### Hypothesis

A constant or median baseline can verify the notebook-only submission pipeline.

### Change

### Result

| Metric / Output | Value |
|---|---|
| submission.csv generated | TBD |
| NaN count | TBD |
| Public RMSE | TBD |

### Interpretation

### Decision

---

## exp_002_tvt_input_interpolation

Date:

### Hypothesis

Interpolating `TVT_input` within each well can create a strong simple baseline because `TVT_input` is copied from the target outside the evaluation zone.

### Change

### Result

| Metric / Output | Value |
|---|---|
| Local validation RMSE | TBD |
| Public RMSE | TBD |

### Interpretation

### Decision

---

## exp_006_public_ridge_artifact_review

Date: 2026-06-09

### Hypothesis

Reviewing a strong public ridge/PF notebook can teach useful domain-specific solution structure, but it should not replace my own baseline and validation work.

### Change

- Reviewed `ROGII Ridge Artifact Projection D4 - Koolbox Fallback`
- Captured profile parameters and final submission contract
- Recorded public references and dependency risks

### Result

| Area | Observation |
|---|---|
| Active profile | `ridge_artifact_experiment` |
| Ridge weight | `0.30` |
| PF particles | `500` |
| PF seeds | `128` |
| Initial spread | `4.5` |
| Projection | enabled, degree `4` |
| Final contract | `id,tvt`, 14151 rows, finite, pass |

### Interpretation

The notebook is a useful advanced reference because it combines physical heuristics, ridge artifacts, PF/beam selection, and trajectory projection. It also has artifact dependencies and many public-solution references, so it should be treated as a study target rather than a first original submission.

### Decision

Keep the first ROGII milestone as my own EDA and interpolation baseline. Revisit the ridge/PF public notebook only after the first valid submission.
