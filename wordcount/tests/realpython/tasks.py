from inspect import getmembers, isfunction
from typing import Callable

from .models import Task


def task(*, number: int, name: str, url: str) -> Callable:
    def decorator(cls: type) -> type:
        # Allow only one test class per task (single source of truth)
        if number in _registered_task_numbers:
            raise ValueError(f"duplicate task number {number}")
        _registered_task_numbers.add(number)

        # Cascade down the task to all test functions in the class:
        for test_function in _get_test_functions(cls):
            test_function.task = Task(number, name, url)

        return cls

    return decorator


def _get_test_functions(cls):
    return (
        function
        for symbol, function in getmembers(cls, isfunction)
        if symbol.startswith("test")
    )


_registered_task_numbers: set[int] = set()
