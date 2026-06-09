# Validation Notes

## Main Risk

Random row-level validation is likely misleading.

Rows within a well share:

- trajectory
- local geology
- nearby TVT continuity
- similar GR patterns
- same typewell reference

If rows from the same well appear in both train and validation, validation can look much better than actual hidden test performance.

## Preferred Validation

Use well-level group validation:

```text
train wells -> model training
held-out wells -> validation
```

For each held-out well, simulate the evaluation zone by masking `TVT_input` in contiguous segments if the competition's actual evaluation-zone pattern is clear.

## Metrics

Use RMSE:

```python
from sklearn.metrics import mean_squared_error

rmse = mean_squared_error(y_true, y_pred) ** 0.5
```

## Baselines to Beat

1. Global median TVT
2. Per-well median `TVT_input`
3. Interpolated `TVT_input`
4. Simple tabular model with well-level validation
