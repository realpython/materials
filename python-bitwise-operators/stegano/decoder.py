"""
Secret file decoder.
"""

from itertools import islice, takewhile
from pathlib import Path
from typing import Iterator

from .bitmap import Bitmap


class DecodingError(Exception):
    pass


def decode(bitmap: Bitmap) -> None:
    """Extract a secret file from the bitmap."""

    if bitmap.reserved_field <= 0:
        raise DecodingError("Secret file not found in the bitmap")

    iterator = secret_bytes(bitmap)

    filename = "".join(map(chr, takewhile(lambda x: x != 0, iterator)))
    with Path(filename).open(mode="wb") as file:
        file.write(bytes(islice(iterator, bitmap.reserved_field)))

    print(f"Extracted a secret file: {filename}")


def secret_bytes(bitmap) -> Iterator[int]:
    """Return an iterator over secret bytes."""
    for eight_bytes in bitmap.byte_slices:
        yield sum(
            [
                (byte & 1) << (7 - i)
                for i, byte in enumerate(bitmap[eight_bytes])
            ]
        )
