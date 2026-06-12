# Baseline Plan

## Goal

Create one valid Kaggle submission without violating the test-set annotation rule.

This first run is for pipeline verification, not leaderboard optimization.

## Phase 0: Join and Environment Check

1. Join the competition.
2. Accept the rules.
3. Open the Code tab.
4. Find the official/simple fine-tuning baseline notebook.
5. Copy and edit the notebook.
6. Confirm the competition input is attached.

## Phase 1: Run Official Baseline

Use the official simple fine-tuning baseline first.

Expected method from the competition overview:

- load poisoned RetinaNet model
- use the public unlearn set
- fine-tune with empty annotations
- run about 20 epochs
- learning rate around `0.0001`
- batch size around `4`
- generate `submission.csv`

Do not change the method until the unmodified baseline runs end to end.

## Phase 2: Submission Sanity Checks

Before submitting, verify:

- file exists: `submission.csv`
- columns are exactly `image_id,prediction_string`
- row count is 2000
- image IDs cover `0..1999`
- every prediction string is a string
- no-detection rows use whitespace, not null
- confidence values are between 0 and 1
- bounding boxes are within image scale where possible

## Phase 3: First Submission

Submit the official baseline output.

Recommended description:

```text
Official simple fine-tuning baseline on unlearn set.
```

Record:

- notebook name
- version
- runtime
- public score
- whether the submission succeeded
- any errors

## Phase 4: First Improvement Ideas

Only after one successful baseline:

1. Try threshold tuning on validation-like outputs from unlearn/reference predictions.
2. Compare poisoned model predictions vs fine-tuned model predictions on unlearn images.
3. Test smaller learning rates.
4. Test freezing more backbone layers.
5. Test confidence calibration without creating test labels.

Avoid anything that turns test images into labels.

## Stop Criteria

Pause this track if:

- Detectron2 setup takes more than one focused session
- GPU/runtime repeatedly fails
- it blocks ROGII v2 progress

This is a strong portfolio topic but a heavier engineering lift than ROGII.
