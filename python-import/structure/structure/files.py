# structure/files.py


def unique_path(directory, name_pattern):
    """Find a path name that does not already exist"""
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            return path


def add_empty_file(path):
    """Create an empty file at the given path"""
    print(f"Create file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()
