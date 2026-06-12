# Kaggle Notebook Starter Checklist

## Step 1: Join

1. Open the competition page.
2. Click `Join Competition`.
3. Read and accept the rules.
4. Confirm the Data tab is accessible.

## Step 2: Open Baseline

1. Open the `Code` tab.
2. Find the official/simple fine-tuning baseline notebook.
3. Click `Copy & Edit`.
4. Confirm competition input is attached.

## Step 3: Run Without Edits

Run the baseline notebook without changes first.

Do not tune parameters before confirming:

- model loads
- training/fine-tuning starts
- inference runs
- `submission.csv` is generated

## Step 4: Validate Submission File

Add or run checks equivalent to:

```python
import pandas as pd

sub = pd.read_csv("/kaggle/working/submission.csv")
print(sub.shape)
print(sub.head())
print(sub.columns.tolist())
print(sub.isna().sum())
print(sub["image_id"].nunique())
```

Expected:

```text
shape: (2000, 2)
columns: ['image_id', 'prediction_string']
unique image_id: 2000
```

## Step 5: Submit

Submit only after the file checks pass.

Suggested description:

```text
Official simple fine-tuning baseline on unlearn set.
```
