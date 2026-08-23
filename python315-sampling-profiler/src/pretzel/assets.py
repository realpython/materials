"""Load Pretzel's model and background assets from disk."""

from dataclasses import dataclass
from importlib.resources import files
from typing import BinaryIO

import numpy as np
import numpy.typing as npt

from pretzel.engine import Face, Mesh, Vertex

ASSETS_DIR = files("pretzel") / "assets"


@dataclass
class Background:
    name: str
    path: str
    pixels: npt.NDArray[np.float32]


def load_mesh(name: str) -> Mesh:
    vertices: list[Vertex] = []
    faces: list[Face] = []
    with open(asset_path(name), encoding="utf-8") as file:
        for line in file:
            kind, _, rest = line.partition(" ")
            if kind == "v":
                x, y, z = rest.split()
                vertices.append((float(x), float(y), float(z)))
            elif kind == "f":
                a, b, c = rest.split()
                faces.append((int(a) - 1, int(b) - 1, int(c) - 1))
    return Mesh(vertices, faces)


def load_background(name: str, fast: bool = False) -> Background:
    path = asset_path(name)
    decode = decode_ppm if fast else decode_ppm_pixel_by_pixel
    return Background(name=name, path=path, pixels=decode(path))


def decode_ppm_pixel_by_pixel(path: str) -> npt.NDArray[np.float32]:
    with open(path, "rb") as file:
        width, height = read_ppm_header(file)
        rows = []
        for _ in range(height):
            row = []
            for _ in range(width):
                pixel = []
                for _ in range(3):
                    value = file.read(1)[0]
                    pixel.append(to_linear(value))
                row.append(pixel)
            rows.append(row)
    return np.array(rows, dtype=np.float32)


def decode_ppm(path: str) -> npt.NDArray[np.float32]:
    with open(path, "rb") as file:
        width, height = read_ppm_header(file)
        data = file.read(width * height * 3)
    pixels = np.frombuffer(data, dtype=np.uint8)
    pixels = pixels.reshape(height, width, 3).astype(np.float32)
    return 255.0 * (pixels / 255.0) ** 2.2


def read_ppm_header(file: BinaryIO) -> tuple[int, int]:
    magic = file.readline().strip()
    if magic != b"P6":
        raise ValueError(f"{file.name} is not a binary PPM file")
    width, height = map(int, file.readline().split())
    file.readline()
    return width, height


def to_linear(value: int) -> float:
    return 255.0 * (value / 255.0) ** 2.2


def asset_path(name: str) -> str:
    return str(ASSETS_DIR / name)
