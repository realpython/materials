from typing import List, Dict, Any

class Task:
    def __init__(self, description: str, completed: bool = False):
        self.description = description
        self.completed = completed

    def to_dict(self) -> Dict[str, Any]:
        return {
            "description": self.description,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        return cls(data["description"], data["completed"])

class TodoList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, description: str):
        if not description:
            raise ValueError("Task description cannot be empty.")
        self.tasks.append(Task(description))

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            raise IndexError("Task index out of range.")

    def delete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            raise IndexError("Task index out of range.")

    def list_tasks(self, status: str = "all") -> List[Task]:
        if status == "completed":
            return [t for t in self.tasks if t.completed]
        elif status == "pending":
            return [t for t in self.tasks if not t.completed]
        return self.tasks
