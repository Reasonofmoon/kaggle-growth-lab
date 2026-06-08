# Orbit Wars Tutorial Review

Date: 2026-06-08

This note summarizes the official Orbit Wars tutorial pasted into the project.

## What the Tutorial Confirms

Orbit Wars can be approached with a simple bot first.

The tutorial demonstrates:

- installing `kaggle-environments>=1.28.0`
- creating the environment with `make("orbit_wars", debug=True)`
- inspecting observations
- converting raw planet rows into `Planet` named tuples
- writing a nearest-target baseline
- testing against `random`
- writing a `main.py`
- submitting through the Kaggle UI

## Observation Fields

The tutorial confirms these key fields:

- `player`: current player id
- `planets`: list of `[id, owner, x, y, radius, ships, production]`
- `fleets`: list of `[id, owner, x, y, angle, from_planet_id, ships]`
- `angular_velocity`: inner planet rotation speed

## Action Format

The agent returns a list of moves:

```python
[[from_planet_id, angle_in_radians, num_ships], ...]
```

Return `[]` to take no action.

## Tutorial Baseline

The tutorial baseline is `nearest_planet_sniper`.

Strategy:

1. Find my planets.
2. Find planets not owned by me.
3. For each owned planet, choose the nearest target.
4. If enough ships are available, send `target.ships + 1`.

## Tutorial-Listed Weaknesses

The tutorial explicitly calls out these weaknesses:

- no travel-time modeling
- multiple planets may target the same target
- sun collisions are ignored
- ships may remain idle on planets with no nearby targets

## Project Baseline Difference

Our first baseline in `src/main.py` keeps the same spirit but adds small safety improvements:

- function is named `agent(obs)`, which is the expected submission entry point
- avoids paths crossing near the sun
- prefers targets using production and distance
- keeps a small defensive reserve
- sends only enough ships plus a small margin

This is still a baseline, not a strong bot.

## Practical Decision

Use the tutorial for:

- learning the environment
- local testing
- understanding submission UI

Use `competitions/orbit-wars/src/main.py` for the first submitted bot.
