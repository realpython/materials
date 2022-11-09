import timeit

from iterdir import (
    recursive_iterdir,
    recursive_iterdir_gen,
)
from listdir import (
    recursive_listdir,
    recursive_listdir_gen,
)
from make_files import make_recursive_nested_dir, recursive_rmdir
from scandir import (
    recursive_scandir,
    recursive_scandir_gen,
)
from walk import (
    get_list_from_walk,
    get_list_from_walk_pathlib,
)

TIMEIT_TIMES = 100
LEVEL_OF_NESTING = 5
FOLDERS_PER_LEVEL = 3
FILES_PER_FOLDER = 3

print("Building files", end="\r")
nested_dir = make_recursive_nested_dir(
    "nested_dir",
    levels=LEVEL_OF_NESTING,
    number_of_folders_per_level=FOLDERS_PER_LEVEL,
    number_of_files_per_folder=FILES_PER_FOLDER,
)


def list_nested_glob():
    list(nested_dir.glob("**/*"))


def list_nested_rglob():
    list(nested_dir.rglob("*"))


def list_nested_iterdir():
    recursive_iterdir(nested_dir)


def list_nested_iterdir_gen():
    list(recursive_iterdir_gen(nested_dir))


def list_nested_os_walk():
    get_list_from_walk(nested_dir)


def list_nested_pathlib_walk():
    get_list_from_walk_pathlib(nested_dir)


def list_nested_os_scandir():
    recursive_scandir(nested_dir)


def list_nested_os_scandir_gen():
    list(recursive_scandir_gen(nested_dir))


def list_nested_os_listdir():
    recursive_listdir(nested_dir)


def list_nested_os_listdir_gen():
    list(recursive_listdir_gen(nested_dir))


tests = [
    ("glob", "list_nested_glob()"),
    ("rglob", "list_nested_rglob()"),
    ("iterdir", "list_nested_iterdir()"),
    ("iterdir_gen", "list_nested_iterdir_gen()"),
    ("os walk", "list_nested_os_walk()"),
    # Uncomment following line if testing with Python 3.12
    # ("pathlib walk", "list_nested_pathlib_walk()"),
    ("os scandir", "list_nested_os_scandir()"),
    ("os scandir_gen", "list_nested_os_scandir_gen()"),
    ("os listdir", "list_nested_os_listdir()"),
    ("os listdir_gen", "list_nested_os_listdir_gen()"),
]

times = []

try:
    for test in tests:
        print(
            f"Timing {test[1]}",
            end=f"{30 * ' '}\r",  # Clear previous characters and reset cursor
        )
        time = timeit.timeit(test[1], globals=globals(), number=TIMEIT_TIMES)
        times.append((f"{test[0]:15}: {time:.3f} seconds", time))

    print("Done!", end=f"{30 * ' '}\n")

    print("\nRESULTS FOR NESTED DIR:\n")
    print(
        "\n".join(
            [time[0] for time in sorted(times, key=lambda item: item[1])]
        ),
        end="\n\n",
    )

finally:

    recursive_rmdir(nested_dir)
