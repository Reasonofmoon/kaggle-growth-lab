# Dataset Notes

Source: pasted Kaggle dataset description.

Important: data access requires accepting the competition rules. Do not commit competition data to GitHub.

## Directory Structure

The data is organized into:

```text
train/
test/
sample_submission.csv
AI_wellbore_geology_prediction_task_en.pptx
```

Each well is identified by an 8-character hash, for example:

```text
015fe0d2
```

## Training Files

Each training well has three associated files:

```text
{WELLNAME}__horizontal_well.csv
{WELLNAME}__typewell.csv
{WELLNAME}.png
```

### Horizontal Well File

Fields:

- `MD`: measured depth in ft
- `X`: easting coordinate in ft
- `Y`: northing coordinate in ft
- `Z`: true vertical depth below sea level in ft
- `ANCC`, `ASTNU`, `ASTNL`, `EGFDU`, `EGFDL`, `BUDA`: predicted depth of geological formations, training only
- `TVT`: manually interpreted True Vertical Thickness, training target
- `GR`: gamma ray log
- `TVT_input`: copy of `TVT` provided as feature, with NaN in evaluation zones

### Typewell File

Fields:

- `TVT`: vertical depth index / geological position
- `GR`: vertical gamma ray signature
- `Geology`: categorical formation label

### PNG

Visualization of the well path and geological cross-section.

Useful for human understanding, but should not be required for the first baseline.

## Test Files

Each test well has:

```text
{WELLNAME}__horizontal_well.csv
{WELLNAME}__typewell.csv
```

The visible `test/` folder contains only example data. During hidden rerun, Kaggle replaces it with the actual hidden test data.

## Target

Predict:

```text
tvt
```

for rows in the evaluation zone of each horizontal well.

Submission id format:

```text
{WELLNAME}_{row_index}
```

Example:

```text
015fe0d2_1654
```

## Initial Feature Ideas

Horizontal well:

- `MD`
- `X`, `Y`, `Z`
- `GR`
- `TVT_input`
- formation depth columns where available in training
- local differences and rolling statistics
- relative position within well

Typewell:

- GR signature by TVT
- nearest typewell TVT by GR similarity
- formation labels encoded from `Geology`

## Leakage Risks

- Random row splits can leak well-specific trajectory patterns.
- `TVT_input` directly copies target outside the evaluation zone.
- Hidden test differs from visible example test.
- Formation columns are training-only according to the pasted description; do not assume they exist in hidden test.

## First Questions

- How many wells are in train?
- How many rows per well?
- Which rows have missing `TVT_input`?
- Does `sample_submission.csv` cover only missing `TVT_input` rows?
- Are `TVT` and `TVT_input` identical outside evaluation zones?
- Are formation columns present in test examples?
- Is `GR` aligned between horizontal well and typewell?
