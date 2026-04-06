import argparse
import sys
from .models import TodoList
from .storage import Storage

def setup_cli(todo_list: TodoList, storage: Storage):
    parser = argparse.ArgumentParser(description="Mini To-Do CLI Application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--completed", action="store_true", help="List only completed tasks")
    list_parser.add_argument("--pending", action="store_true", help="List only pending tasks")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("index", type=int, help="Task index (1-based)")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("index", type=int, help="Task index (1-based)")

    args = parser.parse_args()

    try:
        if args.command == "add":
            todo_list.add_task(args.description)
            storage.save_tasks(todo_list)
            print(f"Added task: {args.description}")

        elif args.command == "list":
            status = "all"
            if args.completed:
                status = "completed"
            elif args.pending:
                status = "pending"
            
            # Show absolute index even when filtered
            tasks_with_index = [(idx, task) for idx, task in enumerate(todo_list.tasks, 1)]
            
            if status == "completed":
                filtered_tasks = [(idx, t) for idx, t in tasks_with_index if t.completed]
            elif status == "pending":
                filtered_tasks = [(idx, t) for idx, t in tasks_with_index if not t.completed]
            else:
                filtered_tasks = tasks_with_index

            if not filtered_tasks:
                print(f"No {status if status != 'all' else ''} tasks found.")
            else:
                for idx, task in filtered_tasks:
                    status_icon = "[x]" if task.completed else "[ ]"
                    print(f"{idx}. {status_icon} {task.description}")

        elif args.command == "complete":
            todo_list.complete_task(args.index - 1)
            storage.save_tasks(todo_list)
            print(f"Marked task {args.index} as completed.")

        elif args.command == "delete":
            todo_list.delete_task(args.index - 1)
            storage.save_tasks(todo_list)
            print(f"Deleted task {args.index}.")

        else:
            parser.print_help()

    except (ValueError, IndexError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
