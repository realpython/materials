from importlib import resources

readers = {}


def collect():
    print("Collecting readers")
    for item in resources.contents(f"{__package__}.readers"):
        if not item.endswith(".py"):
            continue
        module_name = item.strip(".py")
        try:
            readers[module_name] = importlib.import_module(
                f".{module_name}", f"{__package__}.readers"
            ).read
        except AttributeError:
            print(f"No read() function in {item}")
            continue


def data(name, package=__package__):
    """Get data file."""
    data_path = path(name, package)
    file_type = data_path.suffix.lstrip(".")
    return readers[file_type](data_path)


def path(name, package=__package__):
    """Find the path to a data file."""
    for resource in resources.files(package).iterdir():
        if resource.stem == name:
            return resource

    raise FileNotFoundError(f"{name} not found in {package}")


collect()
