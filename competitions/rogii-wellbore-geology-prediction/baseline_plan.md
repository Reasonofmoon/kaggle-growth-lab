# Baseline Plan

## Baseline 0: Submission Shape

Goal:

- read `sample_submission.csv`
- create a valid `submission.csv`
- fill all `tvt` values with a constant
- submit once if needed to verify the notebook pipeline

Candidate constants:

- train global median `TVT`
- train global median `TVT_input`
- sample submission value if available

## Baseline 1: Per-Well TVT Input Interpolation

Goal:

Use `TVT_input` wherever it exists and interpolate missing evaluation-zone rows within each test well.

Strategy:

1. Load each test horizontal well file.
2. Find rows where submission ids are requested.
3. Use row index from submission id.
4. Interpolate `TVT_input` over row order or `MD`.
5. Fill remaining NaNs with per-well median.
6. Fill final missing values with train global median.

Why this is reasonable:

- `TVT_input` is a direct copy of `TVT` outside evaluation zones.
- Geological position usually changes smoothly along the well.
- It creates a strong simple baseline without model complexity.

Risk:

- If evaluation zones are long or discontinuous, interpolation may be weak.
- If test hidden data lacks enough known `TVT_input`, fallback matters.

## Baseline 2: Light Tabular Model

Goal:

Train a small model using only features likely available in both train and test.

Candidate features:

- `MD`
- `X`
- `Y`
- `Z`
- `GR`
- `TVT_input`
- row index
- normalized row position
- local `GR` rolling mean/std
- local `Z` gradient

Models:

- `HistGradientBoostingRegressor`
- `RandomForestRegressor`
- LightGBM if available in Kaggle environment

Validation:

- group split by well id
- compare against interpolation baseline

## Baseline 3: Typewell Correlation Features

Goal:

Use the vertical reference log to add correlation features between horizontal GR and typewell GR.

Initial ideas:

- nearest typewell `GR` match
- rolling correlation windows
- typewell formation label near predicted TVT

This should come after the simple interpolation baseline.

## Advanced Public Reference: Ridge Artifact / PF Projection

The pasted public notebook `ROGII Ridge Artifact Projection D4 - Koolbox Fallback` is an advanced reference, not a first baseline.

Key concepts to study later:

- blend a saved ridge estimate with a physical / particle-filter heuristic
- tune particle count, seed count, and initial TVT spread
- smooth the trajectory with a robust per-well projection in `U = TVT + Z - anchor`
- keep a final submission contract guard for `id,tvt`, row count, id order, and finite predictions

Do not copy this directly as my first submission.

Use it after:

1. own EDA
2. interpolation baseline
3. valid `submission.csv`
4. well-level validation notes
5. attribution and dependency review

## Minimum Experiment Order

1. `exp_001_constant_submission`
2. `exp_002_tvt_input_interpolation`
3. `exp_003_group_validation_split`
4. `exp_004_light_tabular_model`
5. `exp_005_typewell_correlation_features`
6. `exp_006_public_ridge_artifact_review`
