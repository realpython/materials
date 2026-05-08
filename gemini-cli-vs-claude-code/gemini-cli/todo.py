import argparse
import json
import os
import sys


class TodoManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tasks: {e}", file=sys.stderr)
            return []

    def save_tasks(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.tasks, f, indent=4)
        except IOError as e:
            print(f"Error saving tasks: {e}", file=sys.stderr)

    def add_task(self, description):
        task_id = 1
        if self.tasks:
            task_id = max(task["id"] for task in self.tasks) + 1

        new_task = {
            "id": task_id,
            "description": description,
            "completed": False,
        }
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                return True
        return False

    def list_tasks(self, filter_status=None):
        if filter_status == "completed":
            return [t for t in self.tasks if t["completed"]]
        elif filter_status == "pending":
            return [t for t in self.tasks if not t["completed"]]
        return self.tasks

    def delete_task(self, task_id):
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        if len(self.tasks) < initial_count:
            self.save_tasks()
            return True
        return False


def main():
    parser = argparse.ArgumentParser(description="CLI To-Do Application")
    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
    )

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")

    # Complete command
    complete_parser = subparsers.add_parser(
        "complete",
        help="Mark a task as completed",
    )
    complete_parser.add_argument(
        "id",
        type=int,
        help="ID of the task to complete",
    )

    # List command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--filter",
        choices=["all", "completed", "pending"],
        default="all",
        help="Filter tasks by status",
    )

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument(
        "id",
        type=int,
        help="ID of the task to delete",
    )

    args = parser.parse_args()
    manager = TodoManager()

    if args.command == "add":
        task = manager.add_task(args.description)
        print(f"Added task: [{task['id']}] {task['description']}")

    elif args.command == "complete":
        if manager.complete_task(args.id):
            print(f"Marked task {args.id} as completed.")
        else:
            print(f"Error: Task {args.id} not found.", file=sys.stderr)

    elif args.command == "list":
        filter_status = args.filter if args.filter != "all" else None
        tasks = manager.list_tasks(filter_status)
        if not tasks:
            print("No tasks found.")
        else:
            print(f"{'ID':<5} {'Status':<10} {'Description'}")
            print("-" * 30)
            for task in tasks:
                status = "Done" if task["completed"] else "Pending"
                print(f"{task['id']:<5} {status:<10} {task['description']}")

    elif args.command == "delete":
        if manager.delete_task(args.id):
            print(f"Deleted task {args.id}.")
        else:
            print(f"Error: Task {args.id} not found.", file=sys.stderr)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
