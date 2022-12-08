import pathlib


def recursive_iterdir(path: pathlib.Path):
    items = []
    for item in path.iterdir():
        items.append(item)
        if item.is_dir():
            items.extend(recursive_iterdir(item))

    return items


def recursive_iterdir_gen(path: pathlib.Path):
    for item in path.iterdir():
        yield item
        if item.is_dir():
            yield from recursive_iterdir_gen(item)


if __name__ == "__main__":
    from pprint import pp

    docs = pathlib.Path("Desktop")

    print(list(docs.iterdir()))
    pp(list(recursive_iterdir(docs)))
