import re
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from functools import cached_property
from itertools import groupby
from operator import attrgetter
from typing import Iterator, Self

from pytest import Cache, Function, Item, Session

from .constants import CACHE_TASKS_KEY, STASH_REPORT_KEY
from .exceptions import RealPythonAssertionError


@dataclass(frozen=True)
class Task:
    number: int
    name: str
    url: str

    def __str__(self) -> str:
        return f"[Task {self.number}: {self.name}]({self.url})"


class TestStatus(Enum):
    PASSED = "passed"
    FAILED = "failed"
    SKIPPED = "skipped"
    TIMED_OUT = "timed_out"


@dataclass(frozen=True)
class Test:
    item: Item
    status: TestStatus
    exception: RealPythonAssertionError | None

    @cached_property
    def id(self) -> str:
        return self.item.nodeid

    @cached_property
    def function(self) -> Function | None:
        if hasattr(self.item, "function"):
            return self.item.function
        else:
            return None

    @cached_property
    def task_number(self) -> int | None:
        if self.function and hasattr(self.function, "task"):
            return self.function.task.number
        else:
            return None

    @cached_property
    def name(self) -> str:
        docstring = self.function.__doc__ if self.function else None
        full_name = self.id.split("::")[-1]
        if match := re.fullmatch(r"([^\[]+)(\[([^]]+)])?", full_name):
            function_name = match.group(1)
            params = match.group(3)
            pretty_name = (
                function_name.removeprefix("test_")
                .replace("_", " ")
                .capitalize()
            )
            if params:
                if docstring:
                    return f"{docstring} ({params})"
                else:
                    return f"{pretty_name} ({params})"
            else:
                if docstring:
                    return docstring
                else:
                    return pretty_name
        else:
            return docstring if docstring else full_name


@dataclass
class ExerciseProgress:
    cache: Cache
    root: dict

    def __post_init__(self):
        """Ensure that the "statuses" key is a defaultdict instance."""
        self.root["statuses"] = defaultdict(
            dict, self.root.get("statuses", {})
        )

    @classmethod
    def from_cache(cls, cache: Cache) -> Self:
        return cls(
            cache,
            cache.get(
                CACHE_TASKS_KEY,
                {"last_unlocked": 1, "statuses": defaultdict(dict)},
            ),
        )

    @property
    def last_unlocked(self) -> int:
        return max(1, self.root.get("last_unlocked", 1))

    @last_unlocked.setter
    def last_unlocked(self, task_number: int) -> None:
        self.root["last_unlocked"] = task_number

    def save(self) -> None:
        self.cache.set(CACHE_TASKS_KEY, self.root)

    def update(self, test: Test) -> None:
        node = self.root["statuses"][str(test.task_number)]
        match test.status:
            case TestStatus.PASSED | TestStatus.SKIPPED as status:
                node[test.id] = status.value
            case TestStatus.FAILED | TestStatus.TIMED_OUT as status:
                node[test.id] = {status.value: self.num_failures(test) + 1}

    def num_failures(self, test: Test) -> int:
        match (
            self.root.get("statuses", {})
            .get(str(test.task_number), {})
            .get(test.id)
        ):
            case None | "skipped" | "passed":
                return 0
            case {"failed": times} | {"timed_out": times}:
                return times
            case unknown:
                raise ValueError(f"Unknown cached test result: {unknown}")


@dataclass(frozen=True)
class TestRun:
    tests: tuple[Test, ...]

    @classmethod
    def from_session(cls, session: Session) -> Self:
        tests = []
        for item in session.items:
            if STASH_REPORT_KEY in item.stash:
                report = item.stash[STASH_REPORT_KEY]
                if "Failed: Timeout >" in report.longreprtext:
                    status = TestStatus.TIMED_OUT
                else:
                    status = TestStatus(report.outcome)
                if hasattr(report, "exception"):
                    exception = report.exception
                else:
                    exception = None
                tests.append(Test(item, status, exception))
        return cls(tuple(tests))

    @cached_property
    def num_passed(self) -> int:
        return sum(
            1 for test in self.tests if test.status is TestStatus.PASSED
        )

    @cached_property
    def num_tests(self) -> int:
        return len(self.tests)

    @cached_property
    def num_tasks(self) -> int:
        return len({test.task_number for test in self.tests})

    @property
    def tests_by_task(self) -> Iterator[tuple[int, Iterator[Test]]]:
        # Assume tests have been already sorted by the task number
        return groupby(self.tests, attrgetter("task_number"))

    @cached_property
    def status(self) -> TestStatus:
        statuses = {test.status for test in self.tests}
        if TestStatus.TIMED_OUT in statuses:
            return TestStatus.TIMED_OUT
        elif TestStatus.FAILED in statuses:
            return TestStatus.FAILED
        elif set(statuses) == {TestStatus.PASSED} or {
            TestStatus.PASSED,
            TestStatus.SKIPPED,
        }:
            return TestStatus.PASSED
        else:
            raise ValueError("None of the tests were executed")

    def task(self, task_number: int) -> Task:
        for test in self.tests:
            if test.task_number == task_number:
                if test.function and hasattr(test.function, "task"):
                    return test.function.task
        raise ValueError(f"invalid task number {task_number}")

    def task_status(self, task_number: int) -> TestStatus:
        statuses = {
            test.status
            for test in self.tests
            if test.task_number == task_number
        }
        if statuses:
            if TestStatus.TIMED_OUT in statuses:
                return TestStatus.TIMED_OUT
            elif TestStatus.FAILED in statuses:
                return TestStatus.FAILED
            else:
                return TestStatus.PASSED
        else:
            raise ValueError(f"invalid task number {task_number}")
