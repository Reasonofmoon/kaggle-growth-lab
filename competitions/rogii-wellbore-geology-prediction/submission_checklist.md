# Submission Checklist

## Kaggle Setup

- [x] Join competition
- [x] Accept rules to access data
- [x] Create Kaggle Notebook
- [x] Confirm internet is disabled
- [x] Confirm output file is named `submission.csv`

## Data Inspection

- [x] Confirm competition data is attached under `/kaggle/input`
- [x] If data is missing, use `Add Input` or accept rules on the competition page
- [ ] List files under `/kaggle/input/rogii-wellbore-geology-prediction`
- [x] Count train wells
- [x] Count visible test wells
- [x] Read `sample_submission.csv`
- [x] Inspect one train horizontal well
- [x] Inspect one train typewell
- [ ] Inspect one test horizontal well
- [ ] Check missing `TVT_input` rows

## Baseline

- [ ] Generate constant baseline
- [x] Generate `TVT_input` interpolation baseline
- [x] Verify all sample submission ids are filled
- [x] Verify no NaN in `submission.csv`
- [x] Verify columns are exactly `id,tvt`

## Public Notebook / External Artifact Safety

- [ ] Do not use public solution code as my own without attribution
- [ ] Record every public notebook referenced
- [ ] Record every attached public artifact dataset
- [x] Verify code runs with internet disabled
- [ ] Keep a simple baseline comparison before using advanced public references
- [ ] Check final submission contract: columns, row count, id order, finite numeric `tvt`

## Submit

- [x] Save notebook version
- [x] Confirm runtime <= 9 hours
- [x] Confirm `submission.csv` appears in output
- [x] Submit to competition
- [x] Record public score

## After Submission

- [x] Update `experiment_log.md`
- [x] Update `submissions/README.md`
- [ ] Commit with `exp: log rogii baseline submission`
