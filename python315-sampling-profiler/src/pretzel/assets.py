"""Load Pretzel's model and background assets from disk."""

from importlib.resources import files
from types import SimpleNamespace

import numpy as np

from pretzel.engine import Mesh

ASSETS_DIR = files("pretzel") / "assets"


def asset_path(name):
    return str(ASSETS_DIR / name)


def load_mesh(name):
    vertices, faces = [], []
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


def load_background(name, fast=False):
    path = asset_path(name)
    decode = decode_ppm if fast else decode_ppm_pixel_by_pixel
    return SimpleNamespace(name=name, path=path, pixels=decode(path))


def decode_ppm_pixel_by_pixel(path):
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


def to_linear(value):
    return 255.0 * (value / 255.0) ** 2.2


def decode_ppm(path):
    with open(path, "rb") as file:
        width, height = read_ppm_header(file)
        data = file.read(width * height * 3)
    pixels = np.frombuffer(data, dtype=np.uint8)
    pixels = pixels.reshape(height, width, 3).astype(np.float32)
    return 255.0 * (pixels / 255.0) ** 2.2


def read_ppm_header(file):
    magic = file.readline().strip()
    if magic != b"P6":
        raise ValueError(f"{file.name} is not a binary PPM file")
    width, height = map(int, file.readline().split())
    file.readline()
    return width, height
