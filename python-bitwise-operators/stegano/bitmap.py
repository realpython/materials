"""
Bitmap read/write operations.
"""

import pathlib
from dataclasses import dataclass
from itertools import islice
from mmap import mmap, ACCESS_WRITE
from struct import pack, unpack
from typing import Any, Union, Iterator


class Bitmap:
    """High-level interface to a bitmap file."""

    def __init__(self, path: pathlib.Path) -> None:
        self._file = path.open(mode="r+b")
        self._file_bytes = mmap(self._file.fileno(), 0, access=ACCESS_WRITE)
        self._header = Header.from_bytes(self._file_bytes[:50])

    def __enter__(self) -> "Bitmap":
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self._file_bytes.close()
        self._file.close()

    def __getattr__(self, name: str) -> Any:
        return getattr(self._header, name)

    def __getitem__(self, offset: Union[int, slice]) -> Union[int, bytes]:
        return self._file_bytes[offset]

    def __setitem__(
        self, offset: Union[int, slice], value: Union[int, bytes]
    ) -> None:
        self._file_bytes[offset] = value

    @property
    def max_bytes(self) -> int:
        """The maximum number of bytes the bitmap can hide."""
        return self.width * self.height * 3

    @property
    def byte_offsets(self) -> Iterator[int]:
        """Return an iterator over byte offsets (skip the padding)."""

        start_index = self.pixels_offset
        end_index = self.pixels_offset + self.pixel_size_bytes
        scanline_bytes = self.pixel_size_bytes // self.height

        for scanline in range(start_index, end_index, scanline_bytes):
            yield from range(scanline, scanline + self.width * 3)

    @property
    def byte_slices(self) -> Iterator[slice]:
        """Generator iterator of 8-byte long slices."""
        for byte_index in islice(self.byte_offsets, 0, self.max_bytes, 8):
            yield slice(byte_index, byte_index + 8)

    @property
    def reserved_field(self) -> int:
        """Return a little-endian 32-bit unsigned integer."""
        return unsigned_int(self._file_bytes, 0x06)

    @reserved_field.setter
    def reserved_field(self, value: int) -> None:
        """Store a little-endian 32-bit unsigned integer."""
        self._file_bytes.seek(0x06)
        self._file_bytes.write(pack("<I", value))


@dataclass
class Header:
    """Bitmap metadata from the file header."""

    signature: bytes
    file_size_bytes: int
    pixel_size_bytes: int
    pixels_offset: int
    width: int
    height: int
    bit_depth: int
    compressed: bool
    has_palette: bool

    def __post_init__(self):
        assert self.signature == b"BM", "Unknown file signature"
        assert not self.compressed, "Compression unsupported"
        assert not self.has_palette, "Color palette unsupported"
        assert self.bit_depth == 24, "Only 24-bit depth supported"

    @staticmethod
    def from_bytes(data: bytes) -> "Header":
        """Factory method to deserialize the header from bytes."""
        return Header(
            signature=data[0x00:2],
            file_size_bytes=unsigned_int(data, 0x02),
            pixels_offset=unsigned_int(data, 0x0A),
            width=unsigned_int(data, 0x12),
            height=unsigned_int(data, 0x16),
            bit_depth=unsigned_short(data, 0x1C),
            compressed=unsigned_int(data, 0x1E) != 0,
            has_palette=unsigned_int(data, 0x2E) != 0,
            pixel_size_bytes=unsigned_int(data, 0x22),
        )


def unsigned_int(data: Union[bytes, mmap], offset: int) -> int:
    """Read a little-endian 32-bit unsigned integer."""
    return unpack("<I", data[offset : offset + 4])[0]


def unsigned_short(data: Union[bytes, mmap], offset: int) -> int:
    """Read a little-endian 16-bit unsigned integer."""
    return unpack("<H", data[offset : offset + 2])[0]
