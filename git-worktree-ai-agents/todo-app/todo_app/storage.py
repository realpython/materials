# todo_app/storage.py

import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks(path=DATA_FILE):
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_tasks(tasks, path=DATA_FILE):
    path.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
