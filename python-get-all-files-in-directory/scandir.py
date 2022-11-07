import os


def get_all_files_and_folders_scandir(path):
    files = []
    for item in os.scandir(path):
        files.append(item)
        if item.is_dir():
            files.extend(get_all_files_and_folders_scandir(item))

    return files


def get_all_files_and_folders_scandir_gen(path):
    for item in os.scandir(path):
        yield item
        if item.is_dir():
            yield from get_all_files_and_folders_scandir(item)
