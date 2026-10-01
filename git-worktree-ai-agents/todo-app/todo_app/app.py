# todo_app/app.py

from textual.app import App, ComposeResult
from textual.widgets import Footer, Input, Label, ListItem, ListView

from todo_app.storage import load_tasks, save_tasks


def build_item(task):
    marker = "[x]" if task["done"] else "[ ]"
    item = ListItem(Label(f"{marker} {task['text']}", markup=False))
    item.set_class(task["done"], "done")
    return item


class TodoApp(App):
    CSS_PATH = "app.tcss"
    BINDINGS = [
        ("space", "toggle", "Toggle"),
        ("d", "delete", "Delete"),
        ("q", "quit", "Quit"),
    ]

    def __init__(self):
        super().__init__()
        self.tasks = load_tasks()

    def compose(self) -> ComposeResult:
        yield Label("todo", id="title")
        yield Input(placeholder="Add a task, then press Enter", id="new-task")
        yield ListView(*(build_item(task) for task in self.tasks), id="tasks")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#tasks", ListView).index = 0
        self.query_one("#new-task", Input).focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if not text:
            return
        task = {"text": text, "done": False}
        self.tasks.append(task)
        list_view = self.query_one("#tasks", ListView)
        list_view.append(build_item(task))
        if list_view.index is None:
            list_view.index = 0
        event.input.clear()
        save_tasks(self.tasks)

    def action_toggle(self) -> None:
        list_view = self.query_one("#tasks", ListView)
        item = list_view.highlighted_child
        if item is None:
            return
        task = self.tasks[list_view.index]
        task["done"] = not task["done"]
        marker = "[x]" if task["done"] else "[ ]"
        item.query_one(Label).update(f"{marker} {task['text']}")
        item.set_class(task["done"], "done")
        save_tasks(self.tasks)

    def action_delete(self) -> None:
        list_view = self.query_one("#tasks", ListView)
        index = list_view.index
        if index is None:
            return
        del self.tasks[index]
        list_view.pop(index)
        save_tasks(self.tasks)


def main():
    TodoApp().run()


if __name__ == "__main__":
    main()
