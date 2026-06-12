# Dataset Notes

## Files

The competition data contains 2023 files and is about 3.77 GB.

Expected high-level structure:

```text
unlearn_set/
poisoned_model/
test/
sample_submission.csv
```

## Unlearn Set

The unlearn set contains a representative subset of 20 poisoned images from the poisoned model training data.

Properties:

- 1024x1024 PNG
- 16-bit grayscale
- contains poisoned streaks
- poisoned streaks are annotated in `annotations_coco.json`

Use this set for de-poisoning / unlearning experiments.

## Poisoned Model

The shared model is a RetinaNet PyTorch model trained with Detectron2.

The official baseline notebook should be used first to verify:

- Detectron2 import/setup
- model loading
- inference on test images
- submission CSV generation

## Test Set

The test set contains 2,000 images.

Properties:

- 1024x1024 PNG
- 16-bit grayscale
- annotations are not provided

Rule boundary:

- allowed: generate predictions with the de-poisoned model
- allowed: analyze predictions to assess the de-poisoning method
- not allowed: manually or automatically annotate the test set
- not allowed: create hard, weak, soft, or pseudo labels from the test set for advantage

## Sample Submission

`sample_submission.csv` contains predictions from the poisoned model in the correct format.

Columns:

```text
image_id,prediction_string
```

`prediction_string` format:

```text
confidence x y width height
```

Multiple detections are concatenated with spaces.

No detection should be represented by a whitespace string, not an empty string.

## Local Data Policy

Do not commit:

- PNG images
- `.pth` model weights
- raw Kaggle input
- generated full submissions

Commit only:

- notes
- notebooks/cells
- small metadata summaries
- experiment logs
