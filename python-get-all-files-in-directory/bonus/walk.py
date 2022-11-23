import os
import pathlib
import platform


def get_list_from_walk(path):
    files_and_folders = []

    separator = "\\" if platform.platform() == "Windows" else "/"

    for root, dirs, files in os.walk(path):
        files_and_folders.extend(
            [
                *[f"{root}{separator}{dir}" for dir in dirs],
                *[f"{root}{separator}{file}" for file in files],
            ]
        )

    return files_and_folders


def get_list_from_walk_pathlib(path):
    """Only available from Python 3.12.0a1"""
    files_and_folders = []

    for root, dirs, files in pathlib.Path(path).walk():
        files_and_folders.extend(
            [
                *[root / dir for dir in dirs],
                *[root / file for file in files],
            ]
        )

    return files_and_folders
