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
