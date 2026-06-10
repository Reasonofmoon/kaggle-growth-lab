# Competition: Hull Tactical - Market Prediction

Kaggle: https://www.kaggle.com/competitions/hull-tactical-market-prediction

## Current Status

This is a deferred study track, not an active submission target.

As of 2026-06-10 KST:

- entry deadline has passed
- final submission deadline has passed
- new entrants are not allowed
- the data page says new entrants can view the data after the competition completes
- forecasting phase ends on 2026-06-16

Do not spend active competition time here right now.

## Why It Is Still Worth Studying

This competition is useful after completion because it teaches:

- financial time-series leakage control
- forecasting-phase evaluation
- online inference API structure
- allocation prediction instead of plain regression
- risk-adjusted evaluation
- why public leaderboard scores can be misleading in market competitions

## Problem

Predict the daily allocation to the S&P 500 using market features.

The submitted model does not output a raw return forecast directly. It outputs an allocation:

```text
0 <= allocation <= 2
```

where higher values mean more exposure and leverage up to 2x is allowed.

## Evaluation

The metric is a Sharpe-ratio variant that penalizes:

- failing to outperform the market
- taking significantly more volatility than the market

This is not a standard RMSE/accuracy competition.

## Submission Mode

Submissions must use the evaluation API.

The notebook defines:

```python
def predict(test: pl.DataFrame) -> float:
    return 0.0
```

and serves the model through:

```python
kaggle_evaluation.default_inference_server.DefaultInferenceServer(predict)
```

## Timeline

| Event | Date |
|---|---|
| Start | 2025-09-16 |
| Entry deadline | 2025-12-08 23:59 UTC |
| Team merger deadline | 2025-12-08 23:59 UTC |
| Final submission deadline | 2025-12-15 23:59 UTC |
| Forecasting phase end | 2026-06-16 |

## Decision

Do not join or submit now.

Revisit after 2026-06-16 when the competition completes and data access opens for new entrants.

Use this as a post-competition case study, not as a current Kaggle Growth Lab priority.

Current priority order remains:

1. ROGII v2 validation/modeling
2. Orbit Wars first accepted bot
3. 5-Day AI Agents setup
4. Kaggriculture capstone
5. Hull Tactical post-completion study
