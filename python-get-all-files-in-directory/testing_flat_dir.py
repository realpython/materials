import os
import pathlib
import timeit

from make_files import make_dir_with_files, recursive_rmdir

TIMEIT_TIMES = 100
NUMBER_OF_FILES = 10_000

print("Building files", end="\r")
flat_dir = make_dir_with_files("flat_dir", NUMBER_OF_FILES)


def list_flat_glob():
    list(flat_dir.glob("*"))


def list_flat_rglob():
    list(flat_dir.rglob("*"))


def list_flat_iterdir():
    list(flat_dir.iterdir())


def list_flat_os_walk():
    _, dirs, files = next(os.walk(flat_dir))
    [*dirs, *files]


def list_flat_pathlib_walk():
    _, dirs, files = next(pathlib.Path(flat_dir).walk())
    [*dirs, *files]


def list_flat_os_scandir():
    list(os.scandir(flat_dir))


def list_flat_os_listdir():
    os.listdir(flat_dir)


tests = [
    ("glob", "list_flat_glob()"),
    ("rglob", "list_flat_rglob()"),
    ("iterdir", "list_flat_iterdir()"),
    ("os walk", "list_flat_os_walk()"),
    # Uncomment following line if testing with Python 3.12
    # ("pathlib walk", "list_flat_pathlib_walk()"),
    ("os scandir", "list_flat_os_scandir()"),
    ("os listdir", "list_flat_os_listdir()"),
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

    print("\nRESULTS FOR FLAT DIR:\n")
    print(
        "\n".join(
            [time[0] for time in sorted(times, key=lambda item: item[1])]
        ),
        end="\n\n",
    )

finally:

    recursive_rmdir(flat_dir)
