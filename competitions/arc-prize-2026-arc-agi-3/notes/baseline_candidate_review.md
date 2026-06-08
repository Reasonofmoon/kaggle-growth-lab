# Baseline Candidate Review

Date: 2026-06-08

This note reviews the Kaggle notebook snippets collected before the first ARC-AGI-3 submission.

## Recommendation

Submit in this order:

1. Random baseline using the official `ARC-AGI-3-Agents` framework
2. Just-explore heuristic baseline
3. StochasticGoose / CNN action-learning agent

The first goal is an accepted submission, not leaderboard performance.

## Candidate 1: Random Baseline

### What it does

- Installs `arc-agi` from Kaggle competition wheels
- Writes a `MyAgent` class
- Copies `ARC-AGI-3-Agents` into `/kaggle/working`
- Registers `myagent` in a trimmed `agents/__init__.py`
- Writes `.env` to route calls through the Kaggle gateway
- Runs `python main.py --agent myagent`
- Writes a dummy `submission.parquet` outside competition rerun mode

### Strengths

- Minimal
- Uses official competition files
- Best candidate for first accepted submission
- Easy to debug

### Weaknesses

- Random action choice is not a reasoning strategy
- Pure random can waste action budget quickly
- The pasted version may choose unavailable actions unless masked

### Decision

Use this first, but prefer a slightly safer version that samples from `latest_frame.available_actions` when available.

## Candidate 2: Just-Explore Heuristic

Source observed in pasted snippet:

- Kaggle dataset path: `/kaggle/input/datasets/inversion/arc-agi-3-just-explore/arc-agi-3-just-explore`
- Upstream project found: https://github.com/dolphin-in-a-coma/arc-agi-3-just-explore

### What it does

- Copies a separate `arc-agi-3-just-explore` project into `/kaggle/working`
- Registers `HeuristicAgent`
- Runs `python main.py --agent heuristicagent`

### Strengths

- More meaningful than random
- Exploration-first logic matches the competition problem
- Publicly listed as MIT licensed in the upstream repository search result

### Weaknesses

- Requires adding an external Kaggle dataset or code bundle
- More moving parts than the official starter baseline
- Must attribute the source clearly if used

### Decision

Use after random baseline is accepted.

## Candidate 3: StochasticGoose / CNN Action-Learning Agent

Source observed in pasted snippet:

- https://github.com/DriesSmit/ARC3-solution
- Authors noted in snippet: Dries Smit and Jack Cole, Tufa Labs

### What it does

- Uses a CNN to predict which actions are likely to cause frame changes
- Tracks experience between frames
- Trains online during gameplay
- Handles `available_actions` coming from the gateway as raw integers
- Includes compatibility changes from `score` to `levels_completed`

### Strengths

- Much more interesting as an agent design study
- Directly targets action-effect learning
- Good material for a GitHub/LinkedIn explanation

### Weaknesses

- Large and complex
- More likely to hit runtime, memory, or package issues
- Uses third-party code that must be attributed and license-checked before reuse
- Not suitable as the first submission path

### Decision

Do not use as first submission.

Study it after submitting the random baseline and reviewing the just-explore heuristic.

## Practical Notes

- `pip` dependency conflict warnings about `pillow`, `gym`, or profiling packages appeared in the pasted logs. The install still completed.
- The notebook should use Kaggle's `KAGGLE_IS_COMPETITION_RERUN` guard.
- In rerun mode, wait for `http://gateway:8001/api/games`.
- In non-rerun mode, write a dummy `submission.parquet` so the notebook can be saved.
- There are conflicting dummy submission examples in public snippets. Before relying on one, verify the current starter notebook's expected output format.
