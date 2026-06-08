# Competition: Orbit Wars

Kaggle: https://www.kaggle.com/competitions/orbit-wars

Orbit Wars is a Kaggle simulation competition where agents play a real-time strategy game in continuous 2D space.

## 1. Goal

Build and submit an AI bot that plays Orbit Wars.

My first goal is not leaderboard optimization. My first goal is:

- understand the environment
- submit a valid `main.py`
- review validation episodes and logs
- improve strategy one step at a time

## 2. Why This Fits Kaggle Growth Lab

Orbit Wars is a good bridge between standard Kaggle competitions and agentic AI work.

It involves:

- environment observation
- action selection
- multi-agent competition
- geometry and simulation reasoning
- replay/log analysis
- iterative bot improvement

Unlike Nemotron, this does not require large-model fine-tuning. Unlike ARC-AGI-3, the submission structure is more direct.

## 3. Game Summary

Players start with one home planet and send fleets to capture neutral or enemy planets.

Important mechanics:

- board is a 100x100 continuous space
- sun is centered at `(50, 50)` with radius `10`
- planets may be static or orbiting
- fleets travel in straight lines
- fleets crossing the sun are destroyed
- game lasts 500 turns unless players are eliminated earlier
- winner is the player with the highest total ships on planets and in fleets

## 4. Observation and Action

Agent input:

```python
obs
```

Key fields:

- `player`: current player id
- `planets`: `[id, owner, x, y, radius, ships, production]`
- `fleets`: `[id, owner, x, y, angle, from_planet_id, ships]`
- `angular_velocity`: orbiting planet rotation speed
- `initial_planets`: initial planet positions
- `comets`: comet path data
- `comet_planet_ids`: comet planet ids
- `remainingOverageTime`: remaining extra time budget

Agent output:

```python
[[from_planet_id, direction_angle, num_ships], ...]
```

Return `[]` to do nothing.

## 5. First Baseline

Use `src/main.py`.

Strategy:

- find owned planets
- find planets not owned by me
- skip targets that are too expensive
- avoid firing through the sun
- send only a fraction of ships
- prefer nearby high-production targets

This should be treated as `v1`, not a strong bot.

## 6. Timeline

Based on the pasted competition text:

| Event | UTC Date | KST Planning Date |
|---|---|---|
| Start | 2026-04-16 | 2026-04-16 |
| Entry deadline | 2026-06-16 23:59 UTC | 2026-06-17 08:59 KST |
| Team merger deadline | 2026-06-16 23:59 UTC | 2026-06-17 08:59 KST |
| Final submission deadline | 2026-06-23 23:59 UTC | 2026-06-24 08:59 KST |
| Final evaluation period | 2026-06-24 to approximately 2026-07-08 | 2026-06-24 to approximately 2026-07-08 |

Always verify the latest timeline on Kaggle before acting.

## 7. Success Criteria

Minimum:

- [ ] Join competition
- [ ] Read rules
- [ ] Run local validation against `random`
- [ ] Submit `src/main.py`
- [ ] Pass validation episode
- [ ] Download or inspect first replay/log
- [ ] Record first result in `experiment_log.md`

Stretch:

- [ ] Improve target selection
- [ ] Avoid sun collisions more reliably
- [ ] Account for orbiting planet movement
- [ ] Add defensive behavior
- [ ] Compare versions using replay notes

## 8. Active Files

- [Rules summary](rules_summary.md)
- [Submission checklist](submission_checklist.md)
- [Experiment log](experiment_log.md)
- [Baseline bot](src/main.py)
