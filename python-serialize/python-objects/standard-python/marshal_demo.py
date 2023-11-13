import marshal
import sysconfig
from pathlib import Path


def main():
    py_version = sysconfig.get_python_version().replace(".", "")
    cache_dir = Path(sysconfig.get_path("stdlib")) / "__pycache__"
    module_path = cache_dir / f"decimal.cpython-{py_version}.pyc"
    import_pyc(module_path)
    print(Decimal(3.14))  # noqa


def import_pyc(path):
    with path.open(mode="rb") as file:
        _ = file.read(16)  # Skip the file header
        code = marshal.loads(file.read())
        exec(code, globals())


if __name__ == "__main__":
    main()
