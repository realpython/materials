from dataclasses import dataclass
from typing import Self

from todolist.database import Task, TaskList


@dataclass(frozen=True)
class TaskListStatus:
    name: str
    done: tuple[str, ...]
    pending: tuple[str, ...]

    @classmethod
    def find_all(cls) -> tuple[Self, ...]:
        return tuple(
            map(cls.from_model, TaskList.select().order_by(TaskList.name))
        )

    @classmethod
    def find_one(cls, list_name: str) -> Self | None:
        if task_list := TaskList.get_or_none(TaskList.name == list_name):
            return cls.from_model(task_list)
        else:
            return None

    @classmethod
    def from_model(cls, task_list: TaskList) -> Self:
        done, pending = [], []
        for task in task_list.tasks.order_by(Task.name):
            if task.done:
                done.append(task.pretty_name)
            else:
                pending.append(task.pretty_name)
        return cls(
            str(task_list.name),
            tuple(done),
            tuple(pending),
        )

    def __len__(self) -> int:
        return len(self.done) + len(self.pending)
