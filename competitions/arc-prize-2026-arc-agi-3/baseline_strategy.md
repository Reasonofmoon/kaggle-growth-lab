# Baseline Strategy

This file defines a deliberately small first baseline scope.

The target is a valid submission and useful learning notes, not a competitive score.

## Baseline 1: Starter Agent Reproduction

Goal:

- run the official starter or public baseline without modification
- inspect how the agent is structured
- verify submission generation
- make one accepted Kaggle submission

What to record:

- notebook or starter source used
- package installation method
- generated files
- submission acceptance status
- score if available
- one thing that failed or confused me

Implementation note:

- Use `notebooks/01_random_baseline_kaggle_cells.md` for the first Kaggle submission attempt.
- This version samples from `latest_frame.available_actions` when possible, instead of choosing blindly from every `GameAction`.

## Baseline 2: Action-Probing Agent

Goal:

Build a simple agent that prioritizes understanding action effects.

Rough behavior:

1. Start with `RESET`.
2. Store the latest frame.
3. Try each available simple action once.
4. Compare before/after frames.
5. Track which action changes the grid.
6. Prefer actions that produce new states.
7. Stop when `WIN`, `GAME_OVER`, repeated states, or step budget is reached.

This is not expected to perform well. It is useful because ARC-AGI-3 rewards efficient completion, and this baseline will reveal how expensive naive exploration is.

## Baseline 3: Repeated-Action Sanity Check

Goal:

For each public game, test whether a simple repeated action can complete or progress through levels.

Candidate policies:

- repeat `ACTION1`
- repeat `ACTION2`
- repeat `ACTION3`
- repeat `ACTION4`
- cycle available actions

What to record:

- game id
- policy
- levels completed
- number of actions
- final state

## Frame Comparison Ideas

Simple measurements:

- count changed cells between frames
- count unique colors/states
- detect player-like moving objects
- detect whether score/level metadata changed
- detect repeated states

## First Code Sketch

This is only a planning sketch. Adapt it to the actual starter framework before using it.

```python
class ProbingAgent:
    def __init__(self, max_steps=200):
        self.max_steps = max_steps
        self.steps = 0
        self.tried_actions = set()

    def is_done(self, frames, latest_frame):
        if latest_frame.state in {"WIN", "GAME_OVER"}:
            return True
        return self.steps >= self.max_steps

    def choose_action(self, frames, latest_frame):
        self.steps += 1

        for action in latest_frame.available_actions:
            if action not in self.tried_actions:
                self.tried_actions.add(action)
                return action

        return latest_frame.available_actions[0]
```

## What This Baseline Should Teach

- how quickly action budgets disappear
- whether public games expose obvious state changes
- what metadata is available in `latest_frame`
- whether a generic exploration policy has any useful signal
- what needs to be game-specific vs general

## Candidate Escalation

After the first accepted random baseline:

1. Review `notes/baseline_candidate_review.md`.
2. Try the just-explore heuristic if the external dataset/source setup is clear.
3. Study StochasticGoose / CNN action-learning as an implementation reference, but do not copy it into this repository without license verification and clear attribution.
