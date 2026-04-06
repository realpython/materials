#!/usr/bin/env python3
"""CLI-based mini to-do application with JSON persistence."""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

STORAGE_FILE = Path("tasks.json")


# ---------------------------------------------------------------------------
# Storage
# ---------------------------------------------------------------------------

def _load() -> list[dict]:
    if not STORAGE_FILE.exists():
        return []
    try:
        with STORAGE_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise SystemExit(f"Error: Corrupt tasks file: {STORAGE_FILE} must contain a JSON array.")
        return data
    except json.JSONDecodeError as e:
        raise SystemExit(f"Error: Could not parse {STORAGE_FILE}: {e}") from e


def _save(tasks: list[dict]) -> None:
    try:
        with STORAGE_FILE.open("w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2)
    except OSError as e:
        raise SystemExit(f"Error: Could not write to {STORAGE_FILE}: {e}") from e


def _next_id(tasks: list[dict]) -> int:
    return max((t["id"] for t in tasks), default=0) + 1


def _find(tasks: list[dict], task_id: int) -> dict | None:
    return next((t for t in tasks if t["id"] == task_id), None)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_add(args: argparse.Namespace) -> None:
    title = args.title.strip()
    if not title:
        raise SystemExit("Error: Task title cannot be empty.")

    tasks = _load()
    task = {
        "id": _next_id(tasks),
        "title": title,
        "completed": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(task)
    _save(tasks)
    print(f"Added task #{task['id']}: {task['title']}")


def cmd_done(args: argparse.Namespace) -> None:
    tasks = _load()
    task = _find(tasks, args.id)
    if task is None:
        raise SystemExit(f"Error: No task with id {args.id}.")
    if task["completed"]:
        print(f"Task #{args.id} is already marked as completed.")
        return
    task["completed"] = True
    _save(tasks)
    print(f"Marked task #{args.id} as completed: {task['title']}")


def cmd_list(args: argparse.Namespace) -> None:
    tasks = _load()
    filter_by = args.filter

    if filter_by == "completed":
        filtered = [t for t in tasks if t["completed"]]
    elif filter_by == "pending":
        filtered = [t for t in tasks if not t["completed"]]
    else:
        filtered = tasks

    if not filtered:
        label = "" if filter_by == "all" else f"{filter_by} "
        print(f"No {label}tasks found.")
        return

    print(f"\n{'ID':<5} {'Status':<12} {'Created':<22} Title")
    print("-" * 65)
    for t in filtered:
        status = "done" if t["completed"] else "pending"
        created = t.get("created_at", "")[:19]
        print(f"{t['id']:<5} {status:<12} {created:<22} {t['title']}")
    print()


def cmd_delete(args: argparse.Namespace) -> None:
    tasks = _load()
    task = _find(tasks, args.id)
    if task is None:
        raise SystemExit(f"Error: No task with id {args.id}.")
    tasks.remove(task)
    _save(tasks)
    print(f"Deleted task #{args.id}: {task['title']}")


# ---------------------------------------------------------------------------
# CLI wiring
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="todo",
        description="A simple CLI to-do manager.",
    )
    sub = parser.add_subparsers(dest="command", metavar="COMMAND")
    sub.required = True

    # add
    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title", help="Task description")
    p_add.set_defaults(func=cmd_add)

    # done
    p_done = sub.add_parser("done", help="Mark a task as completed")
    p_done.add_argument("id", type=int, help="Task ID")
    p_done.set_defaults(func=cmd_done)

    # list
    p_list = sub.add_parser("list", help="List tasks")
    p_list.add_argument(
        "--filter",
        choices=["all", "completed", "pending"],
        default="all",
        help="Filter tasks (default: all)",
    )
    p_list.set_defaults(func=cmd_list)

    # delete
    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("id", type=int, help="Task ID")
    p_del.set_defaults(func=cmd_delete)

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
