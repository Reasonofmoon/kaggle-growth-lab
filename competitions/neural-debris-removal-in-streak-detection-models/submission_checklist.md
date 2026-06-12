# Submission Checklist

## Before Running

- [ ] Joined competition
- [ ] Accepted rules
- [ ] Read the test-set annotation restriction
- [ ] Opened the official/simple fine-tuning baseline notebook
- [ ] Attached competition input
- [ ] Confirmed notebook accelerator/runtime setting

## Before Submitting

- [ ] `submission.csv` exists
- [ ] Columns are `image_id,prediction_string`
- [ ] Row count is 2000
- [ ] No duplicate `image_id`
- [ ] No null `prediction_string`
- [ ] No-detection rows are represented by whitespace
- [ ] Confidence values are between 0 and 1
- [ ] Did not manually inspect and label test images
- [ ] Did not generate pseudo-labels from test images
- [ ] Did not commit raw data or model weights

## After Submitting

- [ ] Record public score
- [ ] Record notebook version
- [ ] Record runtime
- [ ] Save screenshot of successful submission
- [ ] Update `experiment_log.md`
