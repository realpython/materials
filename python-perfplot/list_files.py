import os
import pathlib
import shutil

import perfplot


def make_dir_with_files(dir_name, number_of_files):
    flat_dir = pathlib.Path(dir_name)

    if flat_dir.exists():
        shutil.rmtree(flat_dir)

    flat_dir.mkdir(exist_ok=True)

    for file_number in range(number_of_files):
        pathlib.Path(flat_dir / pathlib.Path(f"{file_number}.txt")).touch()
    return flat_dir


def glob_star(dir):
    return list(dir.glob("*"))


def glob_star_star(dir):
    return list(dir.glob("**/*"))


def rglob_star(dir):
    return list(dir.rglob("*"))


def iterdir_(dir):
    return list(dir.iterdir())


def os_walk(dir):
    _, dirs, files = next(os.walk(dir))
    return [*dirs, *files]


def os_scandir(dir):
    return list(os.scandir(dir))


def os_listdir(dir):
    return os.listdir(dir)


perfplot.show(
    setup=lambda n: make_dir_with_files(
        "temp",
        number_of_files=n,
    ),
    kernels=[
        glob_star,
        glob_star_star,
        rglob_star,
        iterdir_,
        os_walk,
        os_scandir,
        os_listdir,
    ],
    n_range=[2**n for n in range(13)],
    equality_check=None,
)
