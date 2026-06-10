# Dataset Notes

Source: pasted Kaggle dataset description and competition page.

Important: as of 2026-06-10, new entrants are not allowed and cannot view the data until the competition completes.

## Files

```text
train.csv
test.csv
kaggle_evaluation/
```

Visible metadata from pasted content:

- 13 files
- 8.53 MB
- 197 columns
- file types: `py`, `csv`, `proto`

## train.csv

Historic market data stretching back decades.

Expected issue:

- extensive missing values early in history

Fields:

- `date_id`: one trading day
- `M*`: market dynamics / technical features
- `E*`: macro economic features
- `I*`: interest rate features
- `P*`: price / valuation features
- `V*`: volatility features
- `S*`: sentiment features
- `MOM*`: momentum features
- `D*`: dummy / binary features
- `forward_returns`: next-day S&P 500 return, train only
- `risk_free_rate`: federal funds rate, train only
- `market_forward_excess_returns`: target-like excess return, train only

## test.csv

Mock test set matching unseen test structure.

During the public leaderboard phase, the test set is a copy of the last 180 `date_id`s in train, so public leaderboard scores are not meaningful.

Fields:

- `date_id`
- feature columns matching train
- `is_scored`
- `lagged_forward_returns`
- `lagged_risk_free_rate`
- `lagged_market_forward_excess_returns`

## Forecasting Phase

The evaluation API serves test data timestep by timestep from the beginning of the public set to the end of the private set.

Some days served by the API are not scored.

The first `date_id` served by the API remains constant throughout the competition.

## Leakage Warnings

- Do not use future returns.
- Public leaderboard during training phase is not meaningful because public test rows are copied from historical train.
- Forecasting phase evaluates future market data collected after submission close.
- Feature engineering must be causal with respect to each served timestep.

## Study Questions After Completion

- How does `market_forward_excess_returns` differ from raw `forward_returns`?
- Which feature families have the strongest lagged signal?
- How should a forecast be converted into allocation in `[0, 2]`?
- How does volatility targeting change the optimal allocation?
- How stable are signals across market regimes?
