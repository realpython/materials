#!/usr/bin/env python3
"""
todo — a minimal CLI to-do manager.

Usage:
  python todo.py add "Buy groceries"
  python todo.py list
  python todo.py list --filter pending
  python todo.py list --filter done
  python todo.py done <id>
  python todo.py delete <id>
  python todo.py clear
"""

import argparse
import sys

from todo_storage import TASKS_FILE, load_tasks, make_task, save_tasks

# ── helpers ──────────────────────────────────────────────────────────────────

GREEN  = "\033[32m"
YELLOW = "\033[33m"
RED    = "\033[31m"
RESET  = "\033[0m"
DIM    = "\033[2m"


def _find_task(tasks: list, task_id: str) -> dict:
    matches = [t for t in tasks if t["id"] == task_id]
    if not matches:
        raise KeyError(f"No task found with id '{task_id}'")
    return matches[0]


def _status(task: dict) -> str:
    return f"{GREEN}x{RESET}" if task["done"] else f"{YELLOW}-{RESET}"


def _fmt(task: dict) -> str:
    title = task["title"]
    if task["done"]:
        title = f"{DIM}{title}{RESET}"
    return f"  [{_status(task)}] {task['id']}  {title}  {DIM}({task['created_at']}){RESET}"


# ── sub-commands ──────────────────────────────────────────────────────────────

def cmd_add(args):
    title = " ".join(args.title).strip()
    if not title:
        print(f"{RED}Error:{RESET} Task title cannot be empty.", file=sys.stderr)
        sys.exit(1)

    tasks = load_tasks(args.file)
    task = make_task(title)
    tasks.append(task)
    save_tasks(tasks, args.file)
    print(f"Added [{task['id']}] {task['title']}")


def cmd_list(args):
    tasks = load_tasks(args.file)

    filter_val = args.filter
    if filter_val == "done":
        visible = [t for t in tasks if t["done"]]
    elif filter_val == "pending":
        visible = [t for t in tasks if not t["done"]]
    else:
        visible = tasks

    if not visible:
        label = f" ({filter_val})" if filter_val else ""
        print(f"No tasks{label}.")
        return

    total   = len(tasks)
    done    = sum(1 for t in tasks if t["done"])
    pending = total - done
    print(f"Tasks: {GREEN}{done} done{RESET}, {YELLOW}{pending} pending{RESET}, {total} total")
    print()
    for task in visible:
        print(_fmt(task))


def cmd_done(args):
    tasks = load_tasks(args.file)
    try:
        task = _find_task(tasks, args.id)
    except KeyError as e:
        print(f"{RED}Error:{RESET} {e}", file=sys.stderr)
        sys.exit(1)

    if task["done"]:
        print(f"Task [{args.id}] is already marked as done.")
        return

    task["done"] = True
    save_tasks(tasks, args.file)
    print(f"{GREEN}x{RESET} Marked [{args.id}] as done: {task['title']}")


def cmd_delete(args):
    tasks = load_tasks(args.file)
    try:
        task = _find_task(tasks, args.id)
    except KeyError as e:
        print(f"{RED}Error:{RESET} {e}", file=sys.stderr)
        sys.exit(1)

    tasks.remove(task)
    save_tasks(tasks, args.file)
    print(f"{RED}!{RESET} Deleted [{args.id}] {task['title']}")


def cmd_clear(args):
    tasks = load_tasks(args.file)
    done_tasks = [t for t in tasks if t["done"]]
    if not done_tasks:
        print("No completed tasks to clear.")
        return
    remaining = [t for t in tasks if not t["done"]]
    save_tasks(remaining, args.file)
    print(f"Cleared {len(done_tasks)} completed task(s).")


# ── argument parser ───────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="todo",
        description="A minimal CLI to-do manager.",
    )
    parser.add_argument(
        "--file", default=TASKS_FILE, metavar="PATH",
        help=f"Path to the tasks JSON file (default: {TASKS_FILE})",
    )

    sub = parser.add_subparsers(dest="command", metavar="<command>")
    sub.required = True

    # add
    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title", nargs="+", help="Task title (words joined automatically)")
    p_add.set_defaults(func=cmd_add)

    # list
    p_list = sub.add_parser("list", help="List tasks")
    p_list.add_argument(
        "--filter", choices=["all", "done", "pending"], default="all",
        help="Filter tasks (default: all)",
    )
    p_list.set_defaults(func=cmd_list)

    # done
    p_done = sub.add_parser("done", help="Mark a task as completed")
    p_done.add_argument("id", help="Task ID")
    p_done.set_defaults(func=cmd_done)

    # delete
    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("id", help="Task ID")
    p_del.set_defaults(func=cmd_delete)

    # clear
    p_clear = sub.add_parser("clear", help="Remove all completed tasks")
    p_clear.set_defaults(func=cmd_clear)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except ValueError as e:
        # e.g. corrupt JSON file
        print(f"{RED}Error:{RESET} {e}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"{RED}Error:{RESET} Could not read/write tasks file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
