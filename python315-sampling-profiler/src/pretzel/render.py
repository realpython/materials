"""Turn a mesh, a background, and a clock tick into shaded polygons."""

import math

from pretzel import engine, shading

CAMERA_DISTANCE = 7.0


def compute_frame(mesh, background, tick, width, height, cache_colors=False):
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
    polygons = []
    for face, (red, green, blue) in zip(ordered, channels):
        coordinates = []
        for index in face:
            coordinates.extend(projected[index])
        polygons.append(
            (
                coordinates,
                hex_color(red, green, blue)
                if cache_colors
                else f"#{red:02x}{green:02x}{blue:02x}",
            )
        )
    return polygons


_HEX_CACHE = {}


def hex_color(red, green, blue):
    key = (red, green, blue)
    color = _HEX_CACHE.get(key)
    if color is None:
        color = _HEX_CACHE[key] = f"#{red:02x}{green:02x}{blue:02x}"
    return color
