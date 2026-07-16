"""Turn a mesh, a background, and a clock tick into shaded polygons."""

import math
from typing import Final

from pretzel import engine, shading
from pretzel.assets import Background
from pretzel.engine import Mesh

CAMERA_DISTANCE: Final = 7.0

type Polygon = tuple[list[float], str]


def compute_frame(
    mesh: Mesh,
    background: Background,
    tick: float,
    width: int,
    height: int,
    cache_colors: bool = False,
) -> list[Polygon]:
    matrix = engine.rotation_matrix(
        pitch=0.45 * math.sin(tick * 0.6),
        yaw=tick * 0.9,
        roll=0.1 * math.sin(tick * 0.3),
    )
    transformed = engine.transform_vertices(
        mesh.vertices, matrix, CAMERA_DISTANCE
    )
    projected = engine.project_vertices(
        transformed, width, height, focal_length=0.8 * height
    )
    visible = engine.cull_backfaces(mesh.faces, projected)
    ordered = engine.sort_back_to_front(visible, transformed)
    ambient = shading.sample_ambient_light(background.pixels, tick)
    channels = shading.shade_faces(ordered, transformed, ambient)
    polygons: list[Polygon] = []
    for face, (red, green, blue) in zip(ordered, channels):
        coordinates: list[float] = []
        for index in face:
            coordinates.extend(projected[index])
        if cache_colors:
            color = hex_color(red, green, blue)
        else:
            color = f"#{red:02x}{green:02x}{blue:02x}"
        polygons.append((coordinates, color))
    return polygons


_HEX_CACHE: dict[tuple[int, int, int], str] = {}


def hex_color(red: int, green: int, blue: int) -> str:
    key = (red, green, blue)
    color = _HEX_CACHE.get(key)
    if color is None:
        color = _HEX_CACHE[key] = f"#{red:02x}{green:02x}{blue:02x}"
    return color
