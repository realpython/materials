import argparse
from todo_manager import TodoManager

def main():
    manager = TodoManager()
    parser = argparse.ArgumentParser(description="Mini To-Do CLI Application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--filter", choices=["all", "completed", "pending"], default="all", help="Filter tasks")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("id", type=int, help="Task ID")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        task = manager.add_task(args.description)
        print(f"Task added: [{task.id}] {task.description}")

    elif args.command == "list":
        tasks = manager.list_tasks(args.filter)
        if not tasks:
            print(f"No {args.filter} tasks found.")
        else:
            print(f"{args.filter.capitalize()} Tasks:")
            for task in tasks:
                status = "[x]" if task.completed else "[ ]"
                print(f"{task.id:3}: {status} {task.description}")

    elif args.command == "complete":
        if manager.mark_completed(args.id):
            print(f"Task {args.id} marked as completed.")
        else:
            print(f"Error: Task {args.id} not found.")

    elif args.command == "delete":
        if manager.delete_task(args.id):
            print(f"Task {args.id} deleted.")
        else:
            print(f"Error: Task {args.id} not found.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
