# Getting Started Competitions Roadmap

Kaggle category: https://www.kaggle.com/competitions?hostSegmentIdFilter=5&sortOption=default

## Decision

Use Getting Started competitions as the main short-term training track.

This is the right move because the current active competitions include several heavy tracks:

- ARC-AGI-3: agent reasoning benchmark
- Orbit Wars: real-time simulation bot
- ROGII: domain-specific regression
- Neural Debris Removal: Detectron2 / RetinaNet / AI security

Those are valuable, but they are not the best place to build repetition.

The goal here is to submit often, log results, and build reusable Kaggle workflow habits.

## Priority Order

| Order | Competition | Skill | Target Output |
|---:|---|---|---|
| 1 | Titanic | Basic tabular classification | First clean baseline submission |
| 2 | House Prices | Regression and feature engineering | Cross-validation + improved baseline |
| 3 | Digit Recognizer | Computer vision basics | CNN or simple neural net submission |
| 4 | Spaceship Titanic | Tabular classification upgrade | Better missing-value handling |
| 5 | NLP with Disaster Tweets | Text classification | TF-IDF / transformer baseline |
| 6 | Store Sales | Time-series forecasting | Date features + validation split |
| 7 | Connect X | Simulation agent | First simple rule-based bot |
| 8 | LLM Classification Finetuning | Preference modeling | Optional code competition track |

## Defer For Now

These can wait:

- `I'm Something of a Painter Myself`: GAN workflow is useful but not urgent
- `Petals to the Metal`: TPU-specific workflow can wait
- older archived competitions: useful for study, not current priority

## Working Rule

Do not start several Getting Started competitions at once.

For each competition:

1. Join competition.
2. Read Overview, Data, Evaluation, Rules.
3. Run one simple notebook.
4. Submit once.
5. Save score screenshot.
6. Log result in GitHub.
7. Improve once.
8. Write a short LinkedIn note only after a real submission.

## First Target: Titanic

Immediate objective:

```text
Submit one valid Titanic baseline and log the result.
```

Success criteria:

- `submission.csv` generated
- Kaggle submission succeeds
- public score recorded
- screenshot saved
- experiment log updated

After Titanic is complete, move to House Prices.
