import contextlib
import os
import platform

SEPARATOR = "\\" if platform.platform() == "Windows" else "/"


def get_all_files_and_folders_listdir(path):
    files = []
    for item in os.listdir(path):
        files.append(item)
        with contextlib.suppress(NotADirectoryError):
            files.extend(
                get_all_files_and_folders_listdir(f"{path}{SEPARATOR}{item}")
            )
    return files


def get_all_files_and_folders_listdir_gen(path):
    for item in os.listdir(path):
        yield item
        with contextlib.suppress(NotADirectoryError):
            yield from get_all_files_and_folders_listdir_gen(
                f"{path}{SEPARATOR}{item}"
            )
