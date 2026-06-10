# Evaluation API Notes

The competition uses a forecasting evaluation API.

The submitted notebook must define a `predict` function and start a provided inference server.

## Starter Skeleton

```python
import os

import pandas as pd
import polars as pl

import kaggle_evaluation.default_inference_server


def predict(test: pl.DataFrame) -> float:
    return 0.0


inference_server = kaggle_evaluation.default_inference_server.DefaultInferenceServer(predict)

if os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
    inference_server.serve()
else:
    inference_server.run_local_gateway(("/kaggle/input/hull-tactical-market-prediction/",))
```

## Output

`predict` returns one allocation value per timestep:

```text
0 <= allocation <= 2
```

## Time Constraints

From the pasted starter:

- `inference_server.serve()` must be called within 15 minutes when rerun on hidden test
- each prediction batch after the first must return within 5 minutes
- heavy model loading can be deferred to the first `predict` call

## Baseline Ideas After Completion

1. Constant allocation:

```python
return 1.0
```

2. Conservative no-exposure:

```python
return 0.0
```

3. Lagged excess return sign:

```text
if lagged_market_forward_excess_returns > 0: allocation > 1
else: allocation < 1
```

4. Volatility-targeted allocation:

```text
allocation = clipped(signal / recent_volatility)
```

## Main Engineering Risk

The model must be causal. At each timestep, use only:

- current feature row
- lagged target/return fields provided by the API
- state accumulated from previously served rows
- training data available at notebook startup

Do not use future rows or public/private test leakage.
