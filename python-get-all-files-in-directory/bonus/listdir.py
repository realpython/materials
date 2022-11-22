import contextlib
import os
import platform

SEPARATOR = "\\" if platform.platform() == "Windows" else "/"


def recursive_listdir(path):
    files = []
    for item in os.listdir(path):
        files.append(item)
        with contextlib.suppress(NotADirectoryError):
            files.extend(recursive_listdir(f"{path}{SEPARATOR}{item}"))
    return files


def recursive_listdir_gen(path):
    for item in os.listdir(path):
        yield item
        with contextlib.suppress(NotADirectoryError):
            yield from recursive_listdir_gen(f"{path}{SEPARATOR}{item}")
