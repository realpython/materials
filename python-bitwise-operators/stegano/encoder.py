"""
Secret file encoder.
"""

import pathlib
from typing import Iterator

from .bitmap import Bitmap


class EncodingError(Exception):
    pass


class SecretFile:
    """Convenience class for serializing secret data."""

    def __init__(self, path: pathlib.Path):
        self.path = path
        self.filename = path.name.encode("utf-8") + b"\x00"
        self.size_bytes = path.stat().st_size

    @property
    def num_secret_bytes(self) -> int:
        """Total number of bytes including the null-terminated string."""
        return len(self.filename) + self.size_bytes

    @property
    def secret_bytes(self) -> Iterator[int]:
        """Null-terminated name followed by the file content."""
        yield from self.filename
        with self.path.open(mode="rb") as file:
            yield from file.read()


def encode(bitmap: Bitmap, path: pathlib.Path) -> None:
    """Embed a secret file in the bitmap."""

    file = SecretFile(path)

    if file.num_secret_bytes > bitmap.max_bytes:
        raise EncodingError("Not enough pixels to embed a secret file")

    bitmap.reserved_field = file.size_bytes
    for secret_byte, eight_bytes in zip(file.secret_bytes, bitmap.byte_slices):
        secret_bits = [(secret_byte >> i) & 1 for i in reversed(range(8))]
        bitmap[eight_bytes] = bytes(
            [
                byte | 1 if bit else byte & ~1
                for byte, bit in zip(bitmap[eight_bytes], secret_bits)
            ]
        )

    print("Secret file was embedded in the bitmap")
