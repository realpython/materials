import hashlib
import sys
from pathlib import Path


def calculate_checksum(path: Path, chunk_size: int = 4096) -> bytes:
    checksum = hashlib.md5()
    with path.open(mode="rb") as file:
        while chunk := file.read(chunk_size):
            checksum.update(chunk)
    return checksum.digest()


if __name__ == "__main__":
    print(calculate_checksum(Path(sys.executable)))
