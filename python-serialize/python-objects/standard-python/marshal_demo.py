import marshal
import sysconfig
from importlib.util import cache_from_source
from pathlib import Path


def main():
    stdlib_dir = Path(sysconfig.get_path("stdlib"))
    module_path = stdlib_dir / Path(cache_from_source("decimal.py"))
    import_pyc(module_path)
    print(Decimal(3.14))  # noqa


def import_pyc(path):
    with path.open(mode="rb") as file:
        _ = file.read(16)  # Skip the file header
        code = marshal.loads(file.read())
        exec(code, globals())


if __name__ == "__main__":
    main()
