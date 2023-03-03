import array
import pathlib
from typing import Iterator

from maze_solver.models.border import Border
from maze_solver.models.role import Role
from maze_solver.models.square import Square
from maze_solver.persistence.file_format import FileBody, FileHeader

FORMAT_VERSION: int = 1


def dump_squares(
    width: int,
    height: int,
    squares: tuple[Square, ...],
    path: pathlib.Path,
) -> None:
    header, body = serialize(width, height, squares)
    with path.open(mode="wb") as file:
        header.write(file)
        body.write(file)


def load_squares(path: pathlib.Path) -> Iterator[Square]:
    with path.open("rb") as file:
        header = FileHeader.read(file)
        if header.format_version != FORMAT_VERSION:
            raise ValueError("Unsupported file format version")
        body = FileBody.read(header, file)
        return deserialize(header, body)


def serialize(
    width: int, height: int, squares: tuple[Square, ...]
) -> tuple[FileHeader, FileBody]:
    header = FileHeader(FORMAT_VERSION, width, height)
    body = FileBody(array.array("B", map(compress, squares)))
    return header, body


def deserialize(header: FileHeader, body: FileBody) -> Iterator[Square]:
    for index, square_value in enumerate(body.square_values):
        row, column = divmod(index, header.width)
        border, role = decompress(square_value)
        yield Square(index, row, column, border, role)


def compress(square: Square) -> int:
    return (square.role << 4) | square.border.value


def decompress(square_value: int) -> tuple[Border, Role]:
    return Border(square_value & 0xF), Role(square_value >> 4)
