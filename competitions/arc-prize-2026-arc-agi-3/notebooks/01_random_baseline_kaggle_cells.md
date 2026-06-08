# 01 Random Baseline Kaggle Cells

These cells are intended to be copied into a Kaggle Notebook for the ARC Prize 2026 - ARC-AGI-3 competition.

Goal:

- get one accepted submission
- verify the rerun/gateway flow
- inspect submission mechanics before optimizing agent behavior

## Cell 1: Install Offline Wheels

```python
import subprocess
import sys

subprocess.check_call([
    sys.executable,
    "-m",
    "pip",
    "install",
    "--no-index",
    "--find-links",
    "/kaggle/input/competitions/arc-prize-2026-arc-agi-3/arc_agi_3_wheels",
    "arc-agi",
    "python-dotenv",
])
```

## Cell 2: Write Random Agent

```python
%%writefile /kaggle/working/my_agent.py
import random
import time
from typing import Any

from agents.agent import Agent
from arcengine import FrameData, GameAction, GameState


def _state_name(state: GameState) -> str:
    return getattr(state, "name", str(state))


def _action_id(action: Any) -> int | None:
    if isinstance(action, int):
        return action

    value = getattr(action, "value", None)
    if isinstance(value, int):
        return value

    name = getattr(action, "name", None)
    if isinstance(name, str) and name.startswith("ACTION"):
        try:
            return int(name.replace("ACTION", ""))
        except ValueError:
            return None

    if isinstance(value, str) and value.startswith("ACTION"):
        try:
            return int(value.replace("ACTION", ""))
        except ValueError:
            return None

    return None


def _game_action_from_id(action_id: int) -> GameAction | None:
    return getattr(GameAction, f"ACTION{action_id}", None)


def _available_game_actions(latest_frame: FrameData) -> list[GameAction]:
    raw_actions = getattr(latest_frame, "available_actions", None)

    if not raw_actions:
        raw_actions = [1, 2, 3, 4, 5, 6]

    actions = []
    for raw_action in raw_actions:
        action_id = _action_id(raw_action)
        if action_id is None:
            continue

        action = _game_action_from_id(action_id)
        if action is not None:
            actions.append(action)

    return actions or [GameAction.ACTION1]


class MyAgent(Agent):
    """Availability-aware random baseline.

    This is still a random agent. The only improvement over pure random is
    that it tries to sample from actions exposed by the current frame.
    """

    MAX_ACTIONS = float("inf")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        seed = int(time.time() * 1_000_000) + hash(self.game_id) % 1_000_000
        self.rng = random.Random(seed)

    def is_done(self, frames: list[FrameData], latest_frame: FrameData) -> bool:
        return latest_frame.state is GameState.WIN

    def choose_action(self, frames: list[FrameData], latest_frame: FrameData) -> GameAction:
        if _state_name(latest_frame.state) in {"NOT_PLAYED", "NOT_STARTED", "GAME_OVER"}:
            action = GameAction.RESET
            action.reasoning = "Reset because the game is not active."
            return action

        action = self.rng.choice(_available_game_actions(latest_frame))

        if action.is_simple():
            action.reasoning = f"Random available simple action: {action.value}"
        elif action.is_complex():
            action.set_data({
                "x": self.rng.randint(0, 63),
                "y": self.rng.randint(0, 63),
            })
            action.reasoning = {
                "policy": "random_available_action",
                "action": f"{action.value}",
            }

        return action
```

## Cell 3: Run Agent During Competition Rerun

```python
import os
import shutil
import subprocess

if os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
    subprocess.check_call([
        "curl",
        "--fail",
        "--retry",
        "999",
        "--retry-all-errors",
        "--retry-delay",
        "5",
        "--retry-max-time",
        "600",
        "http://gateway:8001/api/games",
    ])

    source_repo = "/kaggle/input/competitions/arc-prize-2026-arc-agi-3/ARC-AGI-3-Agents"
    working_repo = "/kaggle/working/ARC-AGI-3-Agents"

    if os.path.exists(working_repo):
        shutil.rmtree(working_repo)

    shutil.copytree(source_repo, working_repo)
    shutil.copyfile(
        "/kaggle/working/my_agent.py",
        os.path.join(working_repo, "agents/templates/my_agent.py"),
    )

    with open(os.path.join(working_repo, "agents/__init__.py"), "w", encoding="utf-8") as file:
        file.write("""from typing import Type
from dotenv import load_dotenv
from .agent import Agent, Playback
from .swarm import Swarm
from .templates.random_agent import Random
from .templates.my_agent import MyAgent

load_dotenv()

AVAILABLE_AGENTS: dict[str, Type[Agent]] = {
    "random": Random,
    "myagent": MyAgent,
}
""")

    with open(os.path.join(working_repo, ".env"), "w", encoding="utf-8") as file:
        file.write("""SCHEME=http
HOST=gateway
PORT=8001
ARC_API_KEY=test-key-123
ARC_BASE_URL=http://gateway:8001/
OPERATION_MODE=online
ENVIRONMENTS_DIR=
RECORDINGS_DIR=/kaggle/working/server_recording
""")

    subprocess.check_call(
        ["python", "main.py", "--agent", "myagent"],
        cwd=working_repo,
        env={**os.environ, "MPLBACKEND": "agg"},
    )
```

## Cell 4: Dummy Submission Outside Rerun Mode

```python
import os

if not os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
    import pandas as pd

    submission = pd.DataFrame(
        data=[["1_0", "1", True, 1]],
        columns=["row_id", "game_id", "end_of_game", "score"],
    )
    submission.to_parquet("/kaggle/working/submission.parquet", index=False)
    display(submission.head())
```

## After Running

Record the result in:

- `../experiment_log.md`
- `../submissions/README.md`
- `../notes/public_notebook_review.md`

If the dummy submission schema fails, copy the exact schema from the current official starter notebook and update this file.
