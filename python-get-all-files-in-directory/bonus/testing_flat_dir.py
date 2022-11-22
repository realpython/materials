import os
import pathlib

from make_files import make_dir_with_files, recursive_rmdir
from timing import timeit_multiple

TIMEIT_TIMES = 100
NUMBER_OF_FILES = 10_000

print("Building files", end="\r")
flat_dir = make_dir_with_files("flat_dir", NUMBER_OF_FILES)


def list_flat_glob_star():
    return list(flat_dir.glob("*"))


def list_flat_glob_star_star():
    return list(flat_dir.glob("**/*"))


def list_flat_rglob():
    return list(flat_dir.rglob("*"))


def list_flat_iterdir():
    return list(flat_dir.iterdir())


def list_flat_os_walk():
    _, dirs, files = next(os.walk(flat_dir))
    return [*dirs, *files]


def list_flat_pathlib_walk():
    _, dirs, files = next(pathlib.Path(flat_dir).walk())
    return [*dirs, *files]


def list_flat_os_scandir():
    return list(os.scandir(flat_dir))


def list_flat_os_listdir():
    return os.listdir(flat_dir)


tests = [
    ("glob *", "list_flat_glob_star()"),
    ("glob **/*", "list_flat_glob_star_star()"),
    ("rglob", "list_flat_rglob()"),
    ("iterdir", "list_flat_iterdir()"),
    ("os walk", "list_flat_os_walk()"),
    # Uncomment following line if testing with Python 3.12
    # ("pathlib walk", "list_flat_pathlib_walk()"),
    ("os scandir", "list_flat_os_scandir()"),
    ("os listdir", "list_flat_os_listdir()"),
]


try:
    timeit_multiple(
        tests, name="flat directory", globals=globals(), number=TIMEIT_TIMES
    )

finally:

    recursive_rmdir(flat_dir)
