import os


def recursive_scandir(path):
    files = []
    for item in os.scandir(path):
        files.append(item)
        if item.is_dir():
            files.extend(recursive_scandir(item))

    return files


def recursive_scandir_gen(path):
    for item in os.scandir(path):
        yield item
        if item.is_dir():
            yield from recursive_scandir(item)
