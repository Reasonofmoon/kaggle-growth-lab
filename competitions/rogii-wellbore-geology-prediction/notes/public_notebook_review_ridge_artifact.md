# Public Notebook Review: Ridge Artifact Projection D4

Date: 2026-06-09

Reviewed notebook:

```text
ROGII Ridge Artifact Projection D4 - Koolbox Fallback
```

## Role in This Project

This is not a first-baseline notebook.

It is a strong public-reference candidate to study after:

1. EDA
2. `TVT_input` interpolation baseline
3. first valid `submission.csv`
4. well-level validation notes

## High-Level Idea

The notebook combines a saved ridge estimate with a physical / particle-filter heuristic:

```text
T_blend = w_r * T_ridge + (1 - w_r) * T_heuristic
```

The heuristic estimate is controlled by:

- `N_p`: particle count
- `S`: number of PF seeds
- `sigma_0`: initial TVT spread around the last known anchor

It can then apply a per-well projection in:

```text
U = TVT + Z - anchor
```

and recover final TVT:

```text
T_final = anchor + U_projected - Z
```

## Active Profile in Pasted Run

```python
SUBMISSION_PROFILE = "ridge_artifact_experiment"
RIDGE_ARTIFACT_EXPERIMENT_LABEL = "ridge_exp_w030_p500_s128_sp45_proj_d4"
RIDGE_ARTIFACT_RIDGE_WEIGHT = 0.30
RIDGE_ARTIFACT_PF_N_PARTICLES = 500
RIDGE_ARTIFACT_PF_N_SEEDS = 128
RIDGE_ARTIFACT_PF_INIT_SPREAD = 4.5
RIDGE_ARTIFACT_APPLY_PROJECTION = True
RIDGE_ARTIFACT_PROJECTION_DEGREE = 4
RIDGE_ARTIFACT_PROJECTION_ROBUST_ITERS = 4
RIDGE_ARTIFACT_PROJECTION_ROBUST_C = 2.0
```

Note:

- the pasted explanation later mentions a robust degree-5 projection
- the active parameter block says `RIDGE_ARTIFACT_PROJECTION_DEGREE = 4`
- when reproducing, trust the active first-cell parameter values and log any changes explicitly

The pasted run reports final output:

```text
submission_profile = ridge_artifact_experiment
source_label = ridge_exp_w030_p500_s128_sp45_proj_d4
rows = 14151
columns = id,tvt
contract_pass = True
```

## Runtime / Complexity Observations

This notebook is significantly heavier than the starter baseline.

Observed from pasted output:

- `Parallel(n_jobs=4)` ran 773 tasks in about 34.7 minutes
- multiple LightGBM / CatBoost folds were trained or evaluated
- visible test processing covered 3 example wells
- final `submission.csv` was written successfully

This is acceptable for study, but it is too much complexity for the first original baseline.

## Dependency / Artifact Notes

The notebook uses artifact-backed ridge roots:

```python
RIDGE_ARTIFACT_ROOTS = [
    "/kaggle/input/datasets/ravaghi/wellbore-geology-prediction-artifacts",
    "/kaggle/input/wellbore-geology-prediction-artifacts",
]
```

It also includes a `koolbox` fallback/shim path:

```text
koolbox candidates: []
koolbox shim installed: ModuleNotFoundError("No module named 'koolbox'")
```

Practical implication:

- if I use this notebook, I must attach the required public artifact dataset or verify the fallback path works
- I must keep the references and attribution intact
- I should not copy public solution code into this repository as my own original implementation

## Reported CV Signals in Pasted Run

Several model blocks report overall RMSE values:

| Block | Overall RMSE |
|---|---:|
| Ridge-like block | 10.5881 |
| LightGBM-like block | 10.4813 |
| Variant block | 10.4678 |
| CatBoost-like block | 10.6717 |
| CatBoost variant | 10.6553 |
| Final listed fold summary | 10.4357 |

These are not directly comparable to my future local validation unless I reproduce the same folds and preprocessing.

## References Listed in Notebook

- PF selector / physical model: https://www.kaggle.com/code/aiwody/physical-model-less-overfitting-noise
- PF selector rerun: https://www.kaggle.com/code/aidensong123/rogii-sel15-rerun
- Ridge artifact reference: https://www.kaggle.com/code/overvalueawareness/wellbore-geology-prediction-ridge/notebook
- Ridge artifact reference: https://www.kaggle.com/code/ravaghi/wellbore-geology-prediction-ridge
- Ridge SP45 variant: https://www.kaggle.com/code/needless090/rogii-ridge-sp45
- Better solution LB 9.956: https://www.kaggle.com/code/romantamrazov/rogii-better-solution-lb-9-956
- Super solution LB top 3: https://www.kaggle.com/code/romantamrazov/rogii-super-solution-lb-top-3
- Physics-informed baseline: https://www.kaggle.com/code/karnakbaevarthur/physics-informed-baseline?scriptVersionId=317950936
- Triple-signal beam search / dual PF / LightGBM: https://www.kaggle.com/code/shinyanagai123/triple-signal-beam-search-dual-pf-lightgbm
- Plane-fit formation-top KNN: https://www.kaggle.com/code/konbu17/rogii-plane-fit-formation-top-knn
- Wellbore geology prediction baseline: https://www.kaggle.com/code/vishwasmishra1234/rogii-wellbore-geology-prediction
- XGB starter CV 15: https://www.kaggle.com/code/cdeotte/xgb-starter-cv-15

## Decision

Do not start here.

Use this as the advanced comparison target after I have:

- my own EDA
- my own interpolation baseline
- one valid submission
- a written validation strategy

Then study this notebook to understand:

- why physical/PF heuristics work
- how ridge artifacts are blended
- how projection in `U = TVT + Z - anchor` stabilizes trajectories
- whether a simpler version can be implemented and explained independently
