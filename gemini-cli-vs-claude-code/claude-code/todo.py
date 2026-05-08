#!/usr/bin/env python3
"""CLI to-do application.

Usage:
    todo.py add "Buy groceries"
    todo.py list
    todo.py list --status pending
    todo.py list --status completed
    todo.py done <id>
    todo.py delete <id>
"""

import argparse
import sys

import todo_store as store

# ── Formatting helpers ──────────────────────────────────────────────────────

CHECK = "[x]"
EMPTY = "[ ]"


def _fmt_task(task: dict) -> str:
    status = CHECK if task["completed"] else EMPTY
    suffix = (
        f"  (done {task['completed_at'][:10]})" if task["completed_at"] else ""
    )
    return f"  {task['id']:>3}  {status}  {task['description']}{suffix}"


# ── Command handlers ────────────────────────────────────────────────────────


def cmd_add(args: argparse.Namespace) -> int:
    try:
        task = store.add_task(args.description)
        print(f"Added task #{task['id']}: {task['description']}")
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_list(args: argparse.Namespace) -> int:
    try:
        tasks = store.load_tasks()
        filtered = store.filter_tasks(tasks, args.status)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if not filtered:
        label = "" if args.status == "all" else f"{args.status} "
        print(f"No {label}tasks found.")
        return 0

    label = "" if args.status == "all" else f"{args.status} "
    print(f"\n--- {label}tasks ({len(filtered)}) ---")
    for task in filtered:
        print(_fmt_task(task))
    print()
    return 0


def cmd_done(args: argparse.Namespace) -> int:
    try:
        task = store.complete_task(args.id)
        print(f"Completed task #{task['id']}: {task['description']}")
        return 0
    except (KeyError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_delete(args: argparse.Namespace) -> int:
    try:
        task = store.delete_task(args.id)
        print(f"Deleted task #{task['id']}: {task['description']}")
        return 0
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


# ── Argument parsing ────────────────────────────────────────────────────────


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="todo",
        description="A simple CLI to-do application.",
    )
    sub = parser.add_subparsers(dest="command", metavar="<command>")
    sub.required = True

    # add
    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("description", help="Task description")
    p_add.set_defaults(func=cmd_add)

    # list
    p_list = sub.add_parser("list", help="List tasks")
    p_list.add_argument(
        "--status",
        choices=["all", "pending", "completed"],
        default="all",
        help="Filter by status (default: all)",
    )
    p_list.set_defaults(func=cmd_list)

    # done
    p_done = sub.add_parser("done", help="Mark a task as completed")
    p_done.add_argument("id", type=int, help="Task ID")
    p_done.set_defaults(func=cmd_done)

    # delete
    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("id", type=int, help="Task ID")
    p_del.set_defaults(func=cmd_delete)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
