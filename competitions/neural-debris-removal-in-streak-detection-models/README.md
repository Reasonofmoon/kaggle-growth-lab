# Competition: Neural Debris Removal in Streak Detection Models

Kaggle: https://www.kaggle.com/competitions/neural-debris-removal-in-streak-detection-models

Part of ESA's Secure Your AI competition series.

## Current Status

Active candidate as of 2026-06-12 KST.

| Item | Value |
|---|---|
| Task | De-poison / unlearn a poisoned RetinaNet streak detection model |
| Domain | AI security, object detection, space debris imagery |
| Final submission deadline | 2026-07-22 Anywhere on Earth |
| Dataset size | 3.77 GB |
| Test images | 2,000 |
| Image format | 1024x1024 16-bit grayscale PNG |
| Submission limit | 2 submissions per 24 hours per team |
| Team size | up to 3 |

Always verify the latest timeline on Kaggle before acting.

## Decision

This is worth joining for learning and portfolio value, but it is not the easiest next win.

Recommended role in Kaggle Growth Lab:

1. Join and accept rules.
2. Run one official baseline notebook.
3. Submit one valid baseline if the notebook completes.
4. Document what was learned.
5. Do not let this block ROGII v2.

## Problem

Participants receive a poisoned RetinaNet model trained with Detectron2. The goal is to update the model so that poisoned streak behavior is removed while preserving useful clean streak detection behavior.

The clean model is hidden. Submissions are judged by how close the de-poisoned model detections are to the hidden clean model detections.

## Data

Main inputs:

- `unlearn_set/`: 20 representative poisoned training images and COCO annotations
- `poisoned_model/`: shared poisoned RetinaNet PyTorch model
- `test/`: 2,000 unlabeled test images
- `sample_submission.csv`: prediction format example

Do not commit raw data, model weights, PNG files, or generated submissions to Git unless they are tiny metadata examples.

## Metric

The metric is mean Asymmetric Confidence-Aware Detection Distance (`maCADD`).

Lower is better. Perfect score is 0.

The metric compares detection confidence and bounding-box matching between the submitted de-poisoned model and the hidden clean model. It uses IoU thresholds from 0.2 to 0.9 and asymmetric penalties to reward confidence changes in the correct unlearning direction.

## Submission Format

CSV columns:

```text
image_id,prediction_string
```

Each detection in `prediction_string` uses:

```text
confidence x y width height
```

Use a single whitespace string for no detections because Kaggle treats empty strings as null.

## Critical Rule

The test set must not be annotated manually or automatically.

Do not create hard labels, weak labels, soft labels, or pseudo-labels for test images to gain a competition advantage. Test images may be used only to generate predictions and analyze those predictions.

## Active Files

- [Dataset notes](dataset_notes.md)
- [Rules summary](rules_summary.md)
- [Baseline plan](baseline_plan.md)
- [Submission checklist](submission_checklist.md)
- [Experiment log](experiment_log.md)
- [Starter checklist](notebooks/01_join_and_baseline_checklist.md)
