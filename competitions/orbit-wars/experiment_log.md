# Orbit Wars Experiment Log

## exp_000_workspace_setup

Date: 2026-06-08

### Hypothesis

Orbit Wars is a good first simulation-agent track because a valid baseline can be submitted with a single `main.py`.

### Change

- Added Orbit Wars workspace
- Summarized rules
- Added submission checklist
- Added first baseline bot

### Result

| Item | Status |
|---|---|
| Competition joined | TODO |
| Rules reviewed | DONE |
| Local validation run | TODO |
| Baseline submitted | TODO |
| Validation episode passed | TODO |

### Interpretation

This is more accessible than large-model fine-tuning competitions and more direct than ARC-AGI-3. The main learning loop should be submit, inspect replay, improve strategy, and document changes.

### Decision

Proceed with a small nearest-target baseline.

---

## exp_001_nearest_target_baseline

Date:

### Hypothesis

A simple target-selection bot can pass validation and establish the submission workflow.

### Change

### Result

| Metric / Output | Value |
|---|---|
| Submission id | TBD |
| Validation status | TBD |
| Initial rating | TBD |
| First replay reviewed | TBD |

### Interpretation

### Decision

---

## exp_000_tutorial_review

Date: 2026-06-08

### Hypothesis

The official tutorial can confirm the correct observation/action interface and submission flow before making the first Orbit Wars submission.

### Change

- Reviewed tutorial mechanics
- Added tutorial review notes
- Added notebook-ready environment inspection and baseline cells

### Result

| Area | Takeaway |
|---|---|
| Environment | `make("orbit_wars", debug=True)` |
| Observation | `player`, `planets`, `fleets`, `angular_velocity` |
| Action | `[[from_planet_id, angle, num_ships], ...]` |
| First baseline | nearest target capture logic |
| Submission | `main.py` or bundled `main.py` |

### Interpretation

The tutorial baseline is useful, but it ignores sun collisions. The project baseline keeps the same simplicity while adding basic sun avoidance and defensive reserve.

### Decision

Use `notebooks/01_tutorial_and_baseline_cells.md` if submitting through a Kaggle Notebook, and use `src/main.py` if uploading a file directly.
