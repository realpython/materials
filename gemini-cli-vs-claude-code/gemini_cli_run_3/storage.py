import json
import os
from .models import TodoList, Task

class Storage:
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = file_path

    def load_tasks(self, todo_list: TodoList):
        if not os.path.exists(self.file_path):
            return
        
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                todo_list.tasks = [Task.from_dict(t) for t in data]
        except (json.JSONDecodeError, KeyError):
            # In case of malformed JSON, start fresh
            todo_list.tasks = []

    def save_tasks(self, todo_list: TodoList):
        with open(self.file_path, "w") as f:
            data = [t.to_dict() for t in todo_list.tasks]
            json.dump(data, f, indent=4)
