import pathlib

from timing import timeit_multiple

TIMEIT_TIMES = 100


def get_all_files(path: pathlib.Path):
    for item in path.iterdir():
        if item.is_file():
            yield item
        else:
            yield from get_all_files(item)


desktop = pathlib.Path("Desktop_large")


def glob_get_files():
    list(filter(lambda item: item.is_file(), desktop.rglob("*")))


def iterdir_get_files():
    list(get_all_files(desktop))


tests = [
    ("rglob", "glob_get_files()"),
    ("iterdir", "iterdir_get_files()"),
]

timeit_multiple(
    tests,
    name="Get all Directories",
    globals=globals(),
    number=TIMEIT_TIMES,
)
