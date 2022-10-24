import timeit

from make_files import make_dir_with_files, make_nested_dir
from iterdir import get_all_files, get_all_files_two

NUMBER_OF_FILES_IN_FLAT_DIR = 1000

NUMBER_OF_FOLDERS_IN_NESTED_DIR = 5
NUMBER_OF_FILES_IN_NESTED_DIR = 20

TIMEIT_TIMES = 1000


flat_dir = make_dir_with_files("flat_dir", NUMBER_OF_FILES_IN_FLAT_DIR)
nested_dir = make_nested_dir(
    "nested_dir",
    NUMBER_OF_FOLDERS_IN_NESTED_DIR,
    NUMBER_OF_FILES_IN_NESTED_DIR,
)


def list_flat_glob():
    list(flat_dir.glob("*"))


def list_flat_iterdir():
    list(flat_dir.iterdir())


def list_nested_glob():
    list(nested_dir.glob("**/*"))


def list_nested_iterdir():
    list(get_all_files_two(nested_dir))


print("Timing list_flat_glob")
time_list_flat_glob = timeit.timeit(
    "list_flat_glob()", globals=globals(), number=TIMEIT_TIMES
)
print("Timing list_flat_iterdir")
time_list_flat_iterdir = timeit.timeit(
    "list_flat_iterdir()", globals=globals(), number=TIMEIT_TIMES
)
print("Timing list_nested_glob")
time_list_nested_glob = timeit.timeit(
    "list_nested_glob()", globals=globals(), number=TIMEIT_TIMES
)
print("Timing list_nested_iterdir")
time_list_nested_iterdir = timeit.timeit(
    "list_nested_iterdir()", globals=globals(), number=TIMEIT_TIMES
)

print(
    f"""
    FLAT DIR
    --------
    glob    : {time_list_flat_glob:.3f}
    iterdir : {time_list_flat_iterdir:.3f}
    
    NESTED DIR
    ----------
    glob    : {time_list_nested_glob:.3f}
    iterdir : {time_list_nested_iterdir:.3f}
    """
)


def rmdir(directory):
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()
    directory.rmdir()


rmdir(flat_dir)
rmdir(nested_dir)
