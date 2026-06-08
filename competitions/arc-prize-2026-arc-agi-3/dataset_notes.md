# Dataset Notes

Source:

- Kaggle dataset description pasted into this project
- Official docs: https://docs.arcprize.org/
- ARC Prize page: https://arcprize.org/competitions/2026/arc-agi-3

## Benchmark Type

ARC-AGI-3 is an interactive reasoning benchmark.

It is designed to evaluate whether an AI agent can generalize in novel, unseen environments. The focus is not static prediction. The focus is:

- exploration
- memory
- goal acquisition
- alignment
- percept-plan-action behavior

## Games / Environments

Each game is a handcrafted interactive environment.

The agent must:

- observe the current frame
- decide which action to take
- observe the resulting frame
- infer what changed
- continue until the game reaches `WIN`, `GAME_OVER`, or the agent decides to stop

Each game can contain multiple levels of increasing difficulty.

## Frames

The agent receives frames as JSON objects containing the current game state and metadata.

Frame grid facts:

- maximum size: 64x64
- cell values: integers 0-15
- values represent colors/states
- coordinate system: `(0, 0)` is the top-left cell
- multiple frames may be returned when the environment advances internally before settling

Game states:

- `NOT_FINISHED`
- `WIN`
- `GAME_OVER`
- docs also mention `NOT_STARTED` for sessions that require reset after ending

## Actions

Agents interact with environments using up to 7 actions.

| Action | Meaning |
|---|---|
| `RESET` | Start or restart the game |
| `ACTION1` - `ACTION5` | Simple actions |
| `ACTION6` | Complex action requiring `(x, y)` coordinates |
| `ACTION7` | Additional simple action |

Important:

- Every game defines its own available actions.
- The meaning of each action varies by game.
- The agent must infer action meaning through exploration.

## Public vs Private Games

Public games are available for development and practice.

The Kaggle dataset includes:

- `environment_files/`: public game files
- `ARC-AGI-3-Agents/`: local copy of the agent framework
- `arc_agi_3_wheels/`: package wheels for installing ARC-AGI tooling

Competition evaluation uses a separate private set of 110 games.

Based on the pasted dataset description:

- half are used for the Public Leaderboard score
- half are used for the Private Leaderboard score
- the agent has never seen these games

## Scoring

Agents are scored on:

1. Completion: how many levels the agent completes in each game
2. Efficiency: how many actions the agent takes compared with a human baseline

Per-level score:

```text
raw_score = min(human_actions / agent_actions, 1.0)
level_score = raw_score ** 2
```

Per-game score:

```text
weighted average of level scores, weighted by 1-indexed level index
```

Total score:

```text
average of all individual game scores
```

Final output is a score from 0% to 100%.

## Agent Architecture

The ARC-AGI-3-Agents framework expects an agent to implement two core methods:

```python
is_done(frames, latest_frame)
choose_action(frames, latest_frame)
```

Working interpretation:

- `is_done`: decide whether the agent should stop playing
- `choose_action`: choose the next action based on current and historical frames

A `Swarm` can orchestrate multiple agent instances across available games in parallel.

## Agent Lifecycle

Expected lifecycle:

1. Get the list of available games from the API or local environment files.
2. Open a scorecard to track performance.
3. For each game, call `RESET`.
4. Take actions based on the agent strategy.
5. Stop when done or when the game ends.
6. Close the scorecard after all games are complete.

## First Learning Targets

Before optimizing, I need to understand:

- what one frame looks like
- how available actions are exposed
- how `ACTION6` coordinates are represented
- what a valid submission includes
- how the starter agent is packaged
- how many steps a naive baseline wastes
