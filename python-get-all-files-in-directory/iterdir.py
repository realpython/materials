import pathlib


def get_all_files_and_folders_iterdir(path: pathlib.Path):
    files = []
    for file in path.iterdir():
        files.append(file)
        if file.is_dir():
            files.extend(get_all_files_and_folders_iterdir(file))

    return files


def get_all_files_and_folders_iterdir_gen(path: pathlib.Path):
    for item in path.iterdir():
        yield item
        if item.is_dir():
            yield from get_all_files_and_folders_iterdir_gen(item)


if __name__ == "__main__":
    from pprint import pp

    docs = pathlib.Path("My Documents")

    print(list(docs.iterdir()))
    pp(list(get_all_files_and_folders_iterdir(docs)))
