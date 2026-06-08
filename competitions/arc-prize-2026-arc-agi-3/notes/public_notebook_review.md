# Public Notebook Review

Use this file to review 1-2 starter or public notebooks before making the first submission.

## Notebook 1

Link: official starter / random baseline

### What it does

Installs offline wheels, copies the official `ARC-AGI-3-Agents` repository, registers a custom `MyAgent`, writes `.env` for the gateway, and runs `main.py --agent myagent`.

### Submission format notes

The pasted examples write `submission.parquet` in non-rerun mode. One version uses `row_id`, `game_id`, `end_of_game`, and `score`; another public snippet uses `task_id` and `output`. Verify the current official starter notebook before relying on the dummy schema.

### What I learned

The submission flow is more important than agent quality for the first attempt.

### What I should not blindly copy

Do not choose from all `GameAction` values if `latest_frame.available_actions` is available.

## Notebook 2

Link: just-explore heuristic / StochasticGoose references

### What it does

Explores stronger public approaches. The just-explore agent uses heuristic exploration. StochasticGoose uses a CNN-based action-learning loop to predict which actions change frames.

### Submission format notes

Both require more care around external code, dependencies, attribution, and runtime behavior.

### What I learned

ARC-AGI-3 baselines are less about supervised learning and more about exploration policy, action-effect modeling, and efficient state discovery.

### What I should not blindly copy

Do not copy third-party code into this repository or submit it as my own work without checking license, attribution, and competition sharing rules.
