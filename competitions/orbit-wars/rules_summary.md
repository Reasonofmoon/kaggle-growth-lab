# Orbit Wars Rules Summary

This is a practical summary for participation planning.

Official Kaggle rules should be checked before joining and submitting.

## Core Facts

- Competition: Orbit Wars
- Sponsor: Google LLC
- URL: https://www.kaggle.com/competitions/orbit-wars
- Total prizes: $50,000
- Prize distribution: 1st through 10th each receive $5,000
- Winner license type: CC-BY 4.0
- Competition data terms: Apache 2.0

## Team and Submission Limits

- Maximum team size: 5
- Maximum submissions per day: 5
- Up to 2 final submissions may be selected for judging
- You may only use one Kaggle account

## Simulation-Specific Notes

- There is no private leaderboard in simulation competitions.
- Submissions are scored through repeated episodes.
- Replays may be publicly available and downloadable.
- Actions taken by submitted agents may be visible in replays.
- During evaluation, the submission may not pull external information in or send information out.

## Evaluation

Each submitted bot plays episodes against other bots with similar skill ratings.

Kaggle first runs a validation episode where the bot plays against copies of itself. If the validation episode fails, the submission is marked as `Error` and logs can be downloaded.

Skill rating:

- initialized at `mu = 600`
- updated based on wins, losses, and draws
- score margin does not affect rating updates
- uncertainty decreases over time as more episodes are played

Only the best scoring bot is shown on the leaderboard, but individual submissions can be tracked on the submissions page.

## Data and Code Sharing

- Do not privately share competition code/data outside the team.
- Public code sharing is allowed when made available to all participants through Kaggle forums/notebooks and compatible with rules.
- Keep competition data out of GitHub.
- Open-source code must use an OSI-approved license that allows commercial use.

## Winner Obligations

Winners may need to provide:

- public forum write-up
- detailed methodology
- reproducible code repository
- explanation of architecture, preprocessing, training details, hyperparameters, and related setup

## Personal Boundary

I will treat Orbit Wars as a bot-building and replay-analysis learning track.

I will:

- submit simple, original baseline code first
- keep external data/tools minimal
- document strategy changes
- record validation/replay findings

I will not:

- use multiple accounts
- privately share competition code outside a team
- rely on external network calls during evaluation
- upload restricted competition artifacts to GitHub
