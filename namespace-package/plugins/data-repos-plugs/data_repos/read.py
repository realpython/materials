from importlib import import_module, resources


def collect():
    print("Collecting readers")
    readers = {}
    for item in resources.files(f"{__package__}.readers").iterdir():
        if item.stem == "__pycache__":
            continue
        try:
            read_function = import_module(
                f"{__package__}.readers.{item.stem}"
            ).read
            if callable(read_function):
                readers[item.stem] = read_function
        except ImportError:
            continue
        except AttributeError:
            if item.is_dir():
                continue
            print(f"No read() function in {item}")
            continue

    return readers


def data(name):
    """Get data file."""
    data_path = path(name)
    file_type = data_path.suffix.lstrip(".")
    return readers[file_type](data_path)


def path(name):
    """Find the path to a data file."""
    for resource in resources.files(__package__).iterdir():
        if resource.stem == name:
            return resource

    raise FileNotFoundError(f"{name} not found in {__package__}")


readers = collect()
