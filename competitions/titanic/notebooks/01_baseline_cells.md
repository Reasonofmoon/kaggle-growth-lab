# Titanic Baseline Kaggle Notebook Cells

Copy these cells into a Kaggle notebook after joining the competition.

## Cell 1: Load Data

```python
from pathlib import Path

import pandas as pd

DATA_DIR_CANDIDATES = [
    Path("/kaggle/input/titanic"),
    Path("/kaggle/input/competitions/titanic"),
]

DATA_DIR = next((p for p in DATA_DIR_CANDIDATES if p.exists()), None)
if DATA_DIR is None:
    raise FileNotFoundError("Attach Titanic competition data first.")

train = pd.read_csv(DATA_DIR / "train.csv")
test = pd.read_csv(DATA_DIR / "test.csv")
sample = pd.read_csv(DATA_DIR / "gender_submission.csv")

print("train:", train.shape)
print("test:", test.shape)
print("sample:", sample.shape)
display(train.head())
display(train.isna().sum().sort_values(ascending=False))
```

## Cell 2: Train Baseline

```python
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

FEATURES = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
TARGET = "Survived"

X = train[FEATURES]
y = train[TARGET]

numeric_features = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
categorical_features = ["Sex", "Embarked"]

preprocess = ColumnTransformer(
    transformers=[
        ("num", SimpleImputer(strategy="median"), numeric_features),
        (
            "cat",
            Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore")),
                ]
            ),
            categorical_features,
        ),
    ]
)

model = Pipeline(
    steps=[
        ("preprocess", preprocess),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=300,
                min_samples_leaf=2,
                random_state=42,
                n_jobs=-1,
            ),
        ),
    ]
)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")

print("CV scores:", scores)
print("Mean CV accuracy:", scores.mean())
print("Std:", scores.std())
```

## Cell 3: Create Submission

```python
model.fit(X, y)
preds = model.predict(test[FEATURES])

submission = pd.DataFrame(
    {
        "PassengerId": test["PassengerId"],
        "Survived": preds.astype(int),
    }
)

print(submission.shape)
display(submission.head())
print(submission.isna().sum())
print(submission["Survived"].value_counts().sort_index())

submission.to_csv("/kaggle/working/submission.csv", index=False)
```

## Cell 4: Final Check

```python
check = pd.read_csv("/kaggle/working/submission.csv")
assert list(check.columns) == ["PassengerId", "Survived"]
assert len(check) == len(test)
assert check.isna().sum().sum() == 0
assert set(check["Survived"].unique()).issubset({0, 1})
print("submission.csv is ready")
```
