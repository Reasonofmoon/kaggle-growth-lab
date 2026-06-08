import json
from datetime import datetime
from pathlib import Path


def log_experiment(path, experiment):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        **experiment,
        "logged_at": datetime.now().isoformat(timespec="seconds"),
    }

    if path.exists():
        with path.open("r", encoding="utf-8") as file:
            logs = json.load(file)
    else:
        logs = []

    logs.append(entry)

    with path.open("w", encoding="utf-8") as file:
        json.dump(logs, file, indent=2, ensure_ascii=False)

    return entry
