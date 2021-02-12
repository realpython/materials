"""
Secret file eraser.
"""

from itertools import islice
from random import random

from .bitmap import Bitmap


def erase(bitmap: Bitmap) -> None:
    """Scramble a previously hidden data."""
    if bitmap.reserved_field > 0:
        for byte_offset in islice(bitmap.byte_offsets, bitmap.reserved_field):
            bitmap[byte_offset] = randomize_lsb(bitmap[byte_offset])
        bitmap.reserved_field = 0
        print("Erased a secret file from the bitmap")
    else:
        print("Secret file not found in the bitmap")


def randomize_lsb(value: int) -> int:
    """Set a random bit on the least-significant position."""
    return value & ~1 if random() < 0.5 else value | 1
