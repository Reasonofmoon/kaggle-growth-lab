# Competition: Titanic - Machine Learning from Disaster

Kaggle: https://www.kaggle.com/competitions/titanic

## Current Status

Getting Started track.

This is the first baseline competition for practicing the full Kaggle workflow.

## 1. Problem

Predict whether each passenger survived the Titanic shipwreck.

Target column:

```text
Survived
```

Prediction type:

```text
binary classification
```

## 2. Evaluation Metric

Submissions are evaluated by classification accuracy.

Higher is better.

## 3. First Baseline

Use a simple scikit-learn pipeline:

- selected tabular features
- median imputation for numeric columns
- most-frequent imputation for categorical columns
- one-hot encoding
- RandomForestClassifier

## 4. Submission Format

Expected columns:

```text
PassengerId,Survived
```

## 5. First Notebook Goal

The first notebook should:

1. Load `train.csv`, `test.csv`, and `gender_submission.csv`.
2. Inspect missing values.
3. Train a simple baseline.
4. Print local cross-validation accuracy.
5. Generate `/kaggle/working/submission.csv`.
6. Submit to Kaggle.

## 6. Active Files

- [Starter notebook cells](notebooks/01_baseline_cells.md)
- [Submission checklist](submission_checklist.md)
- [Experiment log](experiment_log.md)
