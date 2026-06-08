# Competition: ARC Prize 2026 - ARC-AGI-3

Kaggle: https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3

ARC Prize page: https://arcprize.org/competitions/2026/arc-agi-3

## 1. Why I am trying this

This is not a normal Kaggle tabular or image competition.

ARC-AGI-3 is an interactive reasoning benchmark where agents must explore novel environments, build useful internal models, set goals, and act without explicit instructions.

My goal is not to compete for prizes at this stage.

My goal is to understand:

- why ARC-AGI-3 is difficult
- how agent evaluation differs from static prediction
- what a valid baseline submission looks like
- how to document difficult AI experiments in public

## 2. Success Criteria

Minimum success:

- [ ] Join the competition
- [ ] Read the rules and timeline
- [ ] Run 1-2 starter or public notebooks
- [ ] Understand the submission format
- [ ] Make one valid baseline submission
- [ ] Log what I learned
- [ ] Draft a LinkedIn post about the attempt

Stretch success:

- [ ] Reproduce a public baseline locally or in Kaggle Notebooks
- [ ] Add one small modification
- [ ] Compare behavior before and after the change
- [ ] Publish a short learning note

## 3. Problem Framing

The agent interacts with ARC-AGI-3 game environments.

Unlike static tasks, the agent must:

- explore the environment
- infer rules from observations
- maintain a useful world model
- decide goals
- plan and execute actions
- adapt when feedback contradicts its assumptions

## 4. Important Constraints

- Evaluation happens through the designated Kaggle competition.
- Internet access is not available during Kaggle evaluation.
- API-based systems such as GPT or Claude cannot be relied on during evaluation.
- Prize-eligible solutions require open-source, reproducible code and methods.
- Competition code and data sharing must follow Kaggle rules.
- Team size limit is 8.
- Daily submission limit is 5.

## 5. Timeline Notes

Official ARC Prize 2026 page lists:

| Date | Event |
|---|---|
| March 25, 2026 | Competition starts |
| June 30, 2026 | ARC-AGI-3 Milestone 1 |
| September 30, 2026 | ARC-AGI-3 Milestone 2 |
| November 2, 2026 | Submissions due |
| December 4, 2026 | Results announced |

Always verify final dates on the Kaggle competition timeline before acting.

## 6. Baseline Plan

The first baseline should focus on completing the submission loop, not score optimization.

Planned steps:

1. Join the competition.
2. Open the official starter materials.
3. Run one public notebook without changes.
4. Inspect the generated submission.
5. Submit once.
6. Record what happened in `experiment_log.md`.

## 7. Experiments

| Experiment | Goal | Result | Decision |
|---|---|---|---|
| exp_001 | Run starter/public baseline | TBD | TBD |
| exp_002 | Inspect submission format | TBD | TBD |
| exp_003 | Make one small behavior change | TBD | TBD |

## 8. Learning Questions

- What does "state" mean in ARC-AGI-3?
- What observations does the agent receive?
- What actions are valid?
- How is agent performance scored?
- What makes a baseline valid?
- What fails when a naive agent is used?

## 9. Current Positioning

This is a research-observation track inside Kaggle Growth Lab.

Priority order:

1. 5-Day AI Agents Intensive
2. Kaggriculture capstone
3. ARC-AGI-3 baseline exploration
