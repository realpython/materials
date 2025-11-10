from collections.abc import Iterable

from rich import print
from rich.console import Console
from rich.prompt import Confirm

from todolist.cli import Callbacks, process_cli
from todolist.database import Task, TaskList
from todolist.emojis import find_matching_emojis, has_emoji_support
from todolist.exporter import export_database_to_json
from todolist.renderer import render_long, render_short
from todolist.status import TaskListStatus


def main() -> None:
    process_cli(
        Callbacks(add, remove, done, undo, rename, show, clear, lists, export)
    )


def add(list_name: str, tasks: Iterable[str]) -> None:
    """Add one or more tasks to a list"""
    task_list, _ = TaskList.get_or_create(name=list_name)
    created_tasks = []
    for task_name in tasks:
        task, created = Task.get_or_create(name=task_name, task_list=task_list)
        if created:
            created_tasks.append(task)
    if created_tasks and has_emoji_support():
        with Console().status("Choosing emoji...", spinner="arc"):
            task_names = tuple(task.name for task in created_tasks)
            emojis = find_matching_emojis(task_names)
            for task, emoji in zip(created_tasks, emojis):
                task.emoji = emoji
                task.save()
    show(list_name)


def remove(list_name: str, tasks: Iterable[str]) -> None:
    """Remove tasks from a list"""
    if task_list := TaskList.get_or_none(name=list_name):
        for task_name in tasks:
            Task.delete().where(
                (Task.name == task_name) & (Task.task_list == task_list)
            ).execute()
        show(list_name)
    else:
        print(f"List not found: {list_name!r}")


def done(list_name: str, tasks: Iterable[str]) -> None:
    """Mark tasks as completed"""
    _mark(list_name, tasks, is_done=True)


def undo(list_name: str, tasks: Iterable[str]) -> None:
    """Mark tasks as pending"""
    _mark(list_name, tasks, is_done=False)


def rename(list_name: str, old: str, new: str) -> None:
    """Rename a task on the given list"""
    if task_list := TaskList.get_or_none(TaskList.name == list_name):
        if task := Task.get_or_none(task_list=task_list, name=old):
            task.name = new
            task.save()
            show(list_name)
        else:
            print(f"Task not found: {old!r}")
    else:
        print(f"List not found: {list_name!r}")


def show(list_name: str) -> None:
    """Show the status of tasks"""
    if status := TaskListStatus.find_one(list_name):
        render_long(status)
    else:
        if list_name.lower() == "default":
            print("You're all caught up :sparkles:")
        else:
            print(f"List not found: {list_name!r}")


def clear(list_name: str) -> None:
    """Clear all tasks from a list"""
    if task_list := TaskList.get_or_none(TaskList.name == list_name):
        prompt = f"Are you sure to remove the {list_name!r} list?"
        if Confirm.ask(prompt, default=False):
            task_list.delete_instance(recursive=True)
    else:
        print(f"List not found: {list_name!r}")


def lists() -> None:
    """Display the available task lists"""
    for status in TaskListStatus.find_all():
        render_short(status)


def export() -> None:
    """Dump all task lists to JSON"""
    export_database_to_json()


def _mark(list_name: str, tasks: Iterable[str], is_done: bool) -> None:
    if task_list := TaskList.get_or_none(name=list_name):
        for task_name in tasks:
            if instance := Task.get_or_none(
                task_list=task_list, name=task_name
            ):
                instance.done = is_done
                instance.save()
            else:
                print(f"Task not found: {task_name!r}")
                break
        else:
            show(list_name)
    else:
        print(f"List not found: {list_name!r}")


if __name__ == "__main__":
    main()
