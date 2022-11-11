import timeit
import pathlib

from make_files import (
    make_nested_dir,
    recursive_rmdir,
    make_recursive_nested_dir,
)

NUMBER_OF_FILES_IN_FLAT_DIR = 1000
NUMBER_OF_FOLDERS_IN_NESTED_DIR = 4
NUMBER_OF_FILES_IN_NESTED_DIR = 4

TIMEIT_TIMES = 100


def get_all_files(path: pathlib.Path):
    for item in path.iterdir():
        if not item.is_dir():
            yield item
        else:
            yield from get_all_files(item)


# nested_dir = make_nested_dir(
#     "nested_dir",
#     NUMBER_OF_FOLDERS_IN_NESTED_DIR,
#     NUMBER_OF_FILES_IN_NESTED_DIR,
# )

nested_dir = make_recursive_nested_dir(
    "nested_dir",
    4,
    NUMBER_OF_FOLDERS_IN_NESTED_DIR,
    NUMBER_OF_FILES_IN_NESTED_DIR,
)


def list_nested_glob():
    list(filter(lambda item: not item.is_dir(), nested_dir.glob("**/*")))


def list_nested_rglob():
    list(filter(lambda item: not item.is_dir(), nested_dir.rglob("*")))


def list_nested_iterdir():
    list(get_all_files(nested_dir))


print("Timing list_nested_glob")
time_list_nested_glob = timeit.timeit(
    "list_nested_glob()", globals=globals(), number=TIMEIT_TIMES
)

print("Timing list_nested_rglob")
time_list_nested_rglob = timeit.timeit(
    "list_nested_rglob()", globals=globals(), number=TIMEIT_TIMES
)

print("Timing list_nested_iterdir")
time_list_nested_iterdir = timeit.timeit(
    "list_nested_iterdir()", globals=globals(), number=TIMEIT_TIMES
)

print(
    f"""
NESTED DIR
glob    : {time_list_nested_glob:.3f} seconds
rglob   : {time_list_nested_glob:.3f} seconds
iterdir : {time_list_nested_iterdir:.3f} seconds
"""
)

recursive_rmdir(nested_dir)
