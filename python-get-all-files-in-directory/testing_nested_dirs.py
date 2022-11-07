import os
import timeit

from iterdir import (
    get_all_files_and_folders_iterdir,
    get_all_files_and_folders_iterdir_gen,
)
from listdir import (
    get_all_files_and_folders_listdir,
    get_all_files_and_folders_listdir_gen,
)
from make_files import make_recursive_nested_dir, rmdir
from scandir import (
    get_all_files_and_folders_scandir,
    get_all_files_and_folders_scandir_gen,
)
from walk import (
    get_all_files_and_folders_walk,
    get_all_files_and_folders_walk_pathlib,
)


TIMEIT_TIMES = 100
LEVEL_OF_NESTING = 5
FOLDERS_PER_LEVEL = 3
FILES_PER_FOLDER = 3

print("Building files")
nested_dir = make_recursive_nested_dir(
    "nested_dir",
    levels=LEVEL_OF_NESTING,
    number_of_folders_per_level=FOLDERS_PER_LEVEL,
    number_of_files_per_folder=FILES_PER_FOLDER,
)


def list_nested_glob():
    list(nested_dir.glob("**/*"))


def list_nested_iterdir():
    get_all_files_and_folders_iterdir(nested_dir)


def list_nested_iterdir_gen():
    list(get_all_files_and_folders_iterdir_gen(nested_dir))


def list_nested_os_walk():
    get_all_files_and_folders_walk(nested_dir)


def list_nested_pathlib_walk():
    get_all_files_and_folders_walk_pathlib(nested_dir)


def list_nested_os_scandir():
    get_all_files_and_folders_scandir(nested_dir)


def list_nested_os_scandir_gen():
    list(get_all_files_and_folders_scandir_gen(nested_dir))


def list_nested_os_listdir():
    get_all_files_and_folders_listdir(nested_dir)


def list_nested_os_listdir_gen():
    list(get_all_files_and_folders_listdir_gen(nested_dir))


tests = [
    ("glob", "list_nested_glob()"),
    ("iterdir", "list_nested_iterdir()"),
    ("iterdir_gen", "list_nested_iterdir_gen()"),
    ("os.walk", "list_nested_os_walk()"),
    ("pathlib walk", "list_nested_pathlib_walk()"),
    ("os.scandir", "list_nested_os_scandir()"),
    ("os.scandir_gen", "list_nested_os_scandir_gen()"),
    ("os.listdir", "list_nested_os_listdir()"),
    ("os.listdir_gen", "list_nested_os_listdir_gen()"),
]

times = []

try:
    for test in tests:
        print(f"Timing {test[1]}")
        time = timeit.timeit(test[1], globals=globals(), number=TIMEIT_TIMES)
        times.append((f"{test[0]:15}: {time:.3f} seconds", time))

    print("\nRESULTS:\n")
    print(
        "\n".join(
            [time[0] for time in sorted(times, key=lambda item: item[1])]
        )
    )

finally:

    rmdir(nested_dir)
