"""Persistence layer for the to-do app — reads/writes tasks to a JSON file."""

import json
import os
import uuid
from datetime import datetime
from typing import List, Optional


TASKS_FILE = "tasks.json"


def _load_raw(filepath: str) -> list:
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Corrupt tasks file '{filepath}': {e}") from e
    if not isinstance(data, list):
        raise ValueError(f"Expected a list in '{filepath}', got {type(data).__name__}")
    return data


def _save_raw(filepath: str, tasks: list) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def load_tasks(filepath: str = TASKS_FILE) -> List[dict]:
    return _load_raw(filepath)


def save_tasks(tasks: List[dict], filepath: str = TASKS_FILE) -> None:
    _save_raw(filepath, tasks)


def make_task(title: str) -> dict:
    return {
        "id": str(uuid.uuid4())[:8],
        "title": title.strip(),
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
