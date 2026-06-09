# Submission Checklist

## Kaggle Setup

- [ ] Join competition
- [ ] Accept rules to access data
- [ ] Create Kaggle Notebook
- [ ] Confirm internet is disabled
- [ ] Confirm output file is named `submission.csv`

## Data Inspection

- [ ] Confirm competition data is attached under `/kaggle/input`
- [ ] If data is missing, use `Add Input` or accept rules on the competition page
- [ ] List files under `/kaggle/input/rogii-wellbore-geology-prediction`
- [ ] Count train wells
- [ ] Count visible test wells
- [ ] Read `sample_submission.csv`
- [ ] Inspect one train horizontal well
- [ ] Inspect one train typewell
- [ ] Inspect one test horizontal well
- [ ] Check missing `TVT_input` rows

## Baseline

- [ ] Generate constant baseline
- [ ] Generate `TVT_input` interpolation baseline
- [ ] Verify all sample submission ids are filled
- [ ] Verify no NaN in `submission.csv`
- [ ] Verify columns are exactly `id,tvt`

## Public Notebook / External Artifact Safety

- [ ] Do not use public solution code as my own without attribution
- [ ] Record every public notebook referenced
- [ ] Record every attached public artifact dataset
- [ ] Verify code runs with internet disabled
- [ ] Keep a simple baseline comparison before using advanced public references
- [ ] Check final submission contract: columns, row count, id order, finite numeric `tvt`

## Submit

- [ ] Save notebook version
- [ ] Confirm runtime <= 9 hours
- [ ] Confirm `submission.csv` appears in output
- [ ] Submit to competition
- [ ] Record public score

## After Submission

- [ ] Update `experiment_log.md`
- [ ] Update `submissions/README.md`
- [ ] Commit with `exp: log rogii baseline submission`
