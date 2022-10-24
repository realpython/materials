import pathlib


def get_all_files(path: pathlib.Path, include_folders=True):
    files = []
    for file in path.iterdir():
        if file.is_file():
            files.append(file)
        else:
            if include_folders:
                files.append(file)
            files.extend(get_all_files(file))

    return files


def get_all_files_two(path: pathlib.Path, include_folders=True):
    for item in path.iterdir():
        if item.is_file():
            yield item
        else:
            if include_folders:
                yield item
            yield from get_all_files_two(item)


if __name__ == "__main__":
    from pprint import pp

    docs = pathlib.Path("My Documents")

    print(list(docs.iterdir()))
    pp(list(get_all_files(docs)))
