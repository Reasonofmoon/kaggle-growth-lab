# Submission Checklist

## Kaggle Setup

- [ ] Join the competition
- [ ] Accept rules
- [ ] Confirm timeline on Kaggle
- [ ] Confirm local or notebook environment has `kaggle-environments>=1.28.0`

## Local Validation

- [ ] Place submission code at `main.py`
- [ ] Confirm `agent(obs)` exists
- [ ] Run tutorial environment inspection cells
- [ ] Run against `random`
- [ ] Run self-play against `main.py`
- [ ] Confirm no timeout or exception
- [ ] Inspect final rewards/status

Suggested local command:

```bash
python -c "from kaggle_environments import make; env = make('orbit_wars', debug=True); env.run(['competitions/orbit-wars/src/main.py', 'random']); print([(i, s.reward, s.status) for i, s in enumerate(env.steps[-1])])"
```

## First Submission

- [ ] Submit `main.py`
- [ ] Message: `nearest target baseline v1`
- [ ] Confirm validation episode passes
- [ ] Record submission id
- [ ] Wait for initial episodes
- [ ] Download or inspect replay/logs

Kaggle CLI:

```bash
kaggle competitions submit orbit-wars -f competitions/orbit-wars/src/main.py -m "nearest target baseline v1"
```

## After Submission

- [ ] Update `experiment_log.md`
- [ ] Update `submissions/README.md`
- [ ] Add replay notes under `notes/`
- [ ] Commit with `exp: log orbit wars baseline submission`

## Next Experiments

- [ ] Avoid sun-crossing paths more carefully
- [ ] Prefer production per distance
- [ ] Reserve defensive ships
- [ ] Predict orbiting planet positions
- [ ] Add enemy fleet threat response
