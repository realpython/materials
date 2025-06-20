import random
import string
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from string import ascii_lowercase
from subprocess import run
from tempfile import TemporaryDirectory, gettempdir
from typing import Callable

import pytest


@dataclass
class FakeFile:
    content: bytes
    counts: tuple[int, ...]

    @cached_property
    def path(self) -> Path:
        return Path("-")

    def format_line(self, max_digits=None, selected=None):
        if selected is None:
            selected = 8 + 4 + 1
        numbers = [
            self.counts[i] for i in range(4) if selected & (2 ** (3 - i))
        ]
        if max_digits is None:
            max_digits = len(str(max(numbers)))
        counts = " ".join(
            filter(None, [f"{number:{max_digits}}" for number in numbers])
        )
        if self.path.name == "-":
            return f"{counts}\n".encode("utf-8")
        else:
            return f"{counts} {self.path}\n".encode("utf-8")


@dataclass
class TempFile(FakeFile):
    @cached_property
    def path(self) -> Path:
        name = "".join(random.choices(ascii_lowercase, k=10))
        return Path(gettempdir()) / name

    def __post_init__(self):
        self.path.write_bytes(self.content)

    def delete(self):
        if self.path.is_dir():
            self.path.rmdir()
        elif self.path.is_file():
            self.path.unlink(missing_ok=True)


@dataclass(frozen=True)
class Files:
    files: list[FakeFile]

    def __iter__(self):
        return iter(self.files)

    def __len__(self):
        return len(self.files)

    @cached_property
    def paths(self):
        return [str(file.path) for file in self.files]

    @cached_property
    def expected(self):
        if len(self.files) > 1:
            return self.file_lines + self.total_line
        else:
            return self.file_lines

    @cached_property
    def file_lines(self):
        return b"".join(file.format_line() for file in self.files)

    @cached_property
    def total_line(self):
        totals = [sum(file.counts[i] for file in self.files) for i in range(4)]
        md = len(str(max(totals)))
        return f"{totals[0]:{md}} {totals[1]:{md}} {totals[3]:{md}} total\n".encode(
            "utf-8"
        )


@pytest.fixture(scope="session")
def small_file():
    temp_file = TempFile(content=b"caffe\n", counts=(1, 1, 6, 6))
    try:
        yield temp_file
    finally:
        temp_file.delete()


@pytest.fixture(scope="session")
def big_file():
    temp_file = TempFile(
        content=(
            b"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\n"
            b"tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\n"
            b"quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\n"
            b"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\n"
            b"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\n"
            b"proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
        ),
        counts=(6, 69, 447, 447),
    )
    try:
        yield temp_file
    finally:
        temp_file.delete()


@pytest.fixture(scope="session")
def file1():
    temp_file = TempFile(content=b"caffe latte\n", counts=(1, 2, 12, 12))
    try:
        yield temp_file
    finally:
        temp_file.delete()


@pytest.fixture(scope="session")
def file2():
    temp_file = TempFile(
        content=b"Lorem ipsum dolor sit amet\n", counts=(1, 5, 27, 27)
    )
    try:
        yield temp_file
    finally:
        temp_file.delete()


@pytest.fixture(scope="session")
def unicode_file():
    temp_file = TempFile(
        content="Zażółć gęślą jaźń\n".encode("utf-8"), counts=(1, 3, 18, 27)
    )
    try:
        yield temp_file
    finally:
        temp_file.delete()


@pytest.fixture(scope="session")
def small_files():
    temp_files = [
        TempFile(content=b"Mocha", counts=(0, 1, 5, 5)),
        TempFile(content=b"Espresso\n", counts=(1, 1, 9, 9)),
        TempFile(content=b"Cappuccino\n", counts=(1, 1, 11, 11)),
        TempFile(content=b"Frappuccino", counts=(0, 1, 11, 11)),
        TempFile(content=b"Flat White\n", counts=(1, 2, 11, 11)),
        TempFile(content=b"Turkish Coffee", counts=(0, 2, 14, 14)),
        TempFile(content=b"Irish Coffee Drink\n", counts=(1, 3, 19, 19)),
        TempFile(content=b"Espresso con Panna", counts=(0, 3, 18, 18)),
    ]
    try:
        yield Files(temp_files)
    finally:
        for file in temp_files:
            file.delete()


@pytest.fixture(scope="session")
def medium_files(file1, file2, unicode_file):
    return Files([file1, file2, unicode_file])


@pytest.fixture(scope="session")
def wc():
    def function(*args, stdin: bytes | None = None) -> bytes:
        process = run(["wordcount", *args], capture_output=True, input=stdin)
        return process.stdout

    return function


@pytest.fixture(scope="session")
def fake_dir():
    with TemporaryDirectory(delete=False) as directory:
        path = Path(directory)
        try:
            yield path
        finally:
            path.rmdir()


@pytest.fixture(scope="function")
def random_name():
    return make_random_name()


def make_random_name(length=10):
    return "".join(random.choices(string.ascii_lowercase, k=length))


@pytest.fixture(scope="session")
def runner(wc, small_file, unicode_file, big_file, fake_dir):
    return Runner(
        wc, small_file, unicode_file, big_file, fake_dir, make_random_name()
    )


@dataclass
class Runner:
    wc: Callable
    file1: FakeFile
    file2: FakeFile
    file3: FakeFile
    fake_dir: Path
    random_name: str

    def __call__(self, *flags):
        return self.wc(
            *flags,
            str(self.file1.path),
            "-",
            str(self.file2.path),
            self.fake_dir,
            "-",
            str(self.file3.path),
            self.random_name,
            stdin=b"flat white",
        )
