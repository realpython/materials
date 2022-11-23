from iterdir import recursive_iterdir, recursive_iterdir_gen
from listdir import recursive_listdir, recursive_listdir_gen
from make_files import make_recursive_nested_dir, recursive_rmdir
from scandir import recursive_scandir, recursive_scandir_gen
from timing import timeit_multiple
from walk import get_list_from_walk, get_list_from_walk_pathlib

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
    return list(nested_dir.glob("**/*"))


def list_nested_rglob():
    return list(nested_dir.rglob("*"))


def list_nested_iterdir():
    return recursive_iterdir(nested_dir)


def list_nested_iterdir_gen():
    return list(recursive_iterdir_gen(nested_dir))


def list_nested_os_walk():
    return get_list_from_walk(nested_dir)


def list_nested_pathlib_walk():
    return get_list_from_walk_pathlib(nested_dir)


def list_nested_os_scandir():
    return recursive_scandir(nested_dir)


def list_nested_os_scandir_gen():
    return list(recursive_scandir_gen(nested_dir))


def list_nested_os_listdir():
    return recursive_listdir(nested_dir)


def list_nested_os_listdir_gen():
    return list(recursive_listdir_gen(nested_dir))


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


try:
    timeit_multiple(
        tests, name="nested directory", globals=globals(), number=TIMEIT_TIMES
    )

finally:
    recursive_rmdir(nested_dir)
