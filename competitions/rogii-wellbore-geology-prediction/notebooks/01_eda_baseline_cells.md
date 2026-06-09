# 01 ROGII EDA and Baseline Cells

These cells are intended for a Kaggle Notebook.

The goal is to inspect the data and generate a first valid `submission.csv`.

## Cell 1: Imports and Paths

```python
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path("/kaggle/input/rogii-wellbore-geology-prediction")
TRAIN_DIR = DATA_DIR / "train"
TEST_DIR = DATA_DIR / "test"
SAMPLE_PATH = DATA_DIR / "sample_submission.csv"

print(DATA_DIR)
print("train exists:", TRAIN_DIR.exists())
print("test exists:", TEST_DIR.exists())
print("sample exists:", SAMPLE_PATH.exists())
```

## Cell 2: List Wells

```python
def well_ids(folder):
    return sorted(
        path.name.split("__horizontal_well.csv")[0]
        for path in folder.glob("*__horizontal_well.csv")
    )


train_wells = well_ids(TRAIN_DIR)
test_wells = well_ids(TEST_DIR)

print("train wells:", len(train_wells))
print("visible test wells:", len(test_wells))
print("first train wells:", train_wells[:5])
print("first test wells:", test_wells[:5])
```

## Cell 3: Inspect Sample Submission

```python
sample = pd.read_csv(SAMPLE_PATH)

print(sample.shape)
print(sample.head())
print(sample.isna().sum())
```

## Cell 4: Inspect One Train Well

```python
well = train_wells[0]
horizontal = pd.read_csv(TRAIN_DIR / f"{well}__horizontal_well.csv")
typewell = pd.read_csv(TRAIN_DIR / f"{well}__typewell.csv")

print("well:", well)
print("horizontal shape:", horizontal.shape)
print(horizontal.head())
print(horizontal.isna().mean().sort_values(ascending=False).head(20))
print("typewell shape:", typewell.shape)
print(typewell.head())
```

## Cell 5: Global Train Summary

```python
summaries = []

for well in train_wells:
    df = pd.read_csv(
        TRAIN_DIR / f"{well}__horizontal_well.csv",
        usecols=["TVT", "TVT_input", "GR"],
    )
    summaries.append({
        "well": well,
        "rows": len(df),
        "tvt_min": df["TVT"].min() if "TVT" in df else np.nan,
        "tvt_max": df["TVT"].max() if "TVT" in df else np.nan,
        "tvt_input_nan_ratio": df["TVT_input"].isna().mean() if "TVT_input" in df else np.nan,
        "gr_nan_ratio": df["GR"].isna().mean() if "GR" in df else np.nan,
    })

summary = pd.DataFrame(summaries)
print(summary.describe(include="all"))
display(summary.head())
```

## Cell 6: Constant Baseline Value

```python
train_tvt_values = []

for well in train_wells:
    df = pd.read_csv(TRAIN_DIR / f"{well}__horizontal_well.csv", usecols=["TVT"])
    train_tvt_values.append(df["TVT"])

global_median_tvt = pd.concat(train_tvt_values, ignore_index=True).median()
print("global median TVT:", global_median_tvt)
```

## Cell 7: Interpolation Baseline

```python
def parse_submission_id(row_id):
    well, row_index = row_id.rsplit("_", 1)
    return well, int(row_index)


sample = pd.read_csv(SAMPLE_PATH)
parsed = sample["id"].map(parse_submission_id)
sample["well"] = parsed.map(lambda value: value[0])
sample["row_index"] = parsed.map(lambda value: value[1])

predictions = []

for well, group in sample.groupby("well", sort=False):
    horizontal_path = TEST_DIR / f"{well}__horizontal_well.csv"

    if not horizontal_path.exists():
        predictions.extend([global_median_tvt] * len(group))
        continue

    df = pd.read_csv(horizontal_path)
    tvt_input = df["TVT_input"].copy()

    # Interpolate along row order. If MD is reliable and monotonic, try MD-based interpolation later.
    filled = tvt_input.interpolate(limit_direction="both")
    filled = filled.fillna(tvt_input.median())
    filled = filled.fillna(global_median_tvt)

    for row_index in group["row_index"]:
        if 0 <= row_index < len(filled):
            predictions.append(float(filled.iloc[row_index]))
        else:
            predictions.append(float(global_median_tvt))

submission = sample[["id"]].copy()
submission["tvt"] = predictions

print(submission.shape)
print("NaNs:", submission["tvt"].isna().sum())
display(submission.head())
```

## Cell 8: Save Submission

```python
submission.to_csv("submission.csv", index=False)

check = pd.read_csv("submission.csv")
print(check.shape)
print(check.head())
print(check.isna().sum())
```

## Submit

Save the notebook version and submit `submission.csv`.

Submission message:

```text
tvt input interpolation baseline
```
