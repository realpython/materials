import marshal
from datetime import datetime, timezone
from importlib.util import MAGIC_NUMBER
from pathlib import Path
from pprint import pp
from py_compile import PycInvalidationMode
from sys import argv
from types import SimpleNamespace


def main(path):
    metadata, code = load_pyc(path)
    pp(vars(metadata))
    if metadata.magic_number == MAGIC_NUMBER:
        exec(code, globals())
    else:
        print("Bytecode incompatible with this interpreter")


def load_pyc(path):
    with Path(path).open(mode="rb") as file:
        return (
            parse_header(file.read(16)),
            marshal.loads(file.read()),
        )


def parse_header(header):
    metadata = SimpleNamespace()
    metadata.magic_number = header[0:4]
    metadata.magic_int = int.from_bytes(header[0:4][:2], "little")
    metadata.python_version = f"3.{(metadata.magic_int - 2900) // 50}"
    metadata.bit_field = int.from_bytes(header[4:8], "little")
    metadata.pyc_type = {
        0: PycInvalidationMode.TIMESTAMP,
        1: PycInvalidationMode.UNCHECKED_HASH,
        3: PycInvalidationMode.CHECKED_HASH,
    }.get(metadata.bit_field)
    if metadata.pyc_type is PycInvalidationMode.TIMESTAMP:
        metadata.timestamp = datetime.fromtimestamp(
            int.from_bytes(header[8:12], "little"),
            timezone.utc,
        )
        metadata.file_size = int.from_bytes(header[12:16], "little")
    else:
        metadata.hash_value = header[8:16]
    return metadata


if __name__ == "__main__":
    main(argv[1])
