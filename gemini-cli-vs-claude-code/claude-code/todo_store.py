"""Task persistence layer — reads/writes tasks to a local JSON file."""

import json
import os
from datetime import datetime, timezone

TASKS_FILE = "tasks.json"


def _load_raw() -> list[dict]:
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError(
                    "Corrupted tasks file: expected a JSON array.",
                )
            return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Corrupted tasks file: {e}") from e


def _save_raw(tasks: list[dict]) -> None:
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def _next_id(tasks: list[dict]) -> int:
    return max((t["id"] for t in tasks), default=0) + 1


def load_tasks() -> list[dict]:
    """Return all tasks from disk."""
    return _load_raw()


def add_task(description: str) -> dict:
    """Create a new task and persist it. Returns the new task."""
    description = description.strip()
    if not description:
        raise ValueError("Task description cannot be empty.")
    tasks = _load_raw()
    task = {
        "id": _next_id(tasks),
        "description": description,
        "completed": False,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "completed_at": None,
    }
    tasks.append(task)
    _save_raw(tasks)
    return task


def complete_task(task_id: int) -> dict:
    """Mark a task as completed. Returns the updated task."""
    tasks = _load_raw()
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                raise ValueError(f"Task {task_id} is already completed.")
            task["completed"] = True
            task["completed_at"] = datetime.now(timezone.utc).isoformat()
            _save_raw(tasks)
            return task
    raise KeyError(f"Task {task_id} not found.")


def delete_task(task_id: int) -> dict:
    """Delete a task by ID. Returns the deleted task."""
    tasks = _load_raw()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted = tasks.pop(i)
            _save_raw(tasks)
            return deleted
    raise KeyError(f"Task {task_id} not found.")


def filter_tasks(tasks: list[dict], status: str) -> list[dict]:
    """Filter tasks by status: 'all', 'pending', or 'completed'."""
    if status == "all":
        return tasks
    if status == "pending":
        return [t for t in tasks if not t["completed"]]
    if status == "completed":
        return [t for t in tasks if t["completed"]]
    raise ValueError(
        f"Unknown status filter '{status}'. Use: all, pending, completed.",
    )
