"""Generate Pretzel's assets: a trefoil-knot mesh and background wallpapers.

The generated files are already checked into version control, so you only
need to run this script if you want to tweak the assets:

$ uv run make_assets.py
"""

import math
import pathlib
from typing import Final

type Vector = tuple[float, float, float]
type Face = tuple[int, int, int]
type Color = tuple[int, int, int]

ASSETS_DIR = pathlib.Path(__file__).parent / "src" / "pretzel" / "assets"

SEGMENTS: Final = 240
RING_POINTS: Final = 16
TUBE_RADIUS: Final = 0.62

WALLPAPER_SIZE: Final = 512
WALLPAPERS: Final = {
    "bakery_dawn.ppm": ((252, 210, 153), (146, 90, 118), (255, 236, 179)),
    "bakery_noon.ppm": ((214, 235, 251), (245, 232, 201), (255, 255, 224)),
    "bakery_dusk.ppm": ((94, 63, 107), (233, 156, 90), (255, 214, 138)),
}


def main() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    write_mesh(ASSETS_DIR / "pretzel.mdl")
    for name, (top, bottom, glow) in WALLPAPERS.items():
        write_wallpaper(ASSETS_DIR / name, top, bottom, glow)


def write_mesh(path: pathlib.Path) -> None:
    vertices, faces = sweep_tube()
    with path.open("w", encoding="utf-8") as file:
        file.write(f"# Trefoil-knot pretzel: {len(vertices)} vertices,")
        file.write(f" {len(faces)} faces\n")
        for x, y, z in vertices:
            file.write(f"v {x:.6f} {y:.6f} {z:.6f}\n")
        for a, b, c in faces:
            file.write(f"f {a + 1} {b + 1} {c + 1}\n")
    print(f"Wrote {path} ({len(vertices)} vertices, {len(faces)} faces)")


def write_wallpaper(
    path: pathlib.Path, top: Color, bottom: Color, glow: Color
) -> None:
    size = WALLPAPER_SIZE
    lights = [
        (size * 0.25, size * 0.3, size * 0.22),
        (size * 0.7, size * 0.55, size * 0.3),
        (size * 0.45, size * 0.8, size * 0.18),
    ]
    rows = bytearray()
    for y in range(size):
        vertical = y / (size - 1)
        base = blend(top, bottom, vertical)
        for x in range(size):
            halo = 0.0
            for cx, cy, radius in lights:
                distance = math.hypot(x - cx, y - cy)
                halo += max(0.0, 1.0 - distance / radius) ** 2
            color = blend(base, glow, min(1.0, halo))
            rows.extend(color)
    with path.open("wb") as file:
        file.write(b"P6\n%d %d\n255\n" % (size, size))
        file.write(rows)
    print(f"Wrote {path} ({size}x{size})")


def sweep_tube() -> tuple[list[Vector], list[Face]]:
    step = 2.0 * math.pi / SEGMENTS
    centers = [trace_trefoil(index * step) for index in range(SEGMENTS)]
    tangents = [
        normalize(subtract(centers[(i + 1) % SEGMENTS], centers[i - 1]))
        for i in range(SEGMENTS)
    ]
    normal = normalize(cross(tangents[0], (0.0, 0.0, 1.0)))
    vertices = []
    for center, tangent in zip(centers, tangents):
        projection = dot(normal, tangent)
        normal = normalize(
            (
                normal[0] - projection * tangent[0],
                normal[1] - projection * tangent[1],
                normal[2] - projection * tangent[2],
            )
        )
        binormal = cross(tangent, normal)
        for point in range(RING_POINTS):
            angle = 2.0 * math.pi * point / RING_POINTS
            radial = math.cos(angle), math.sin(angle)
            vertices.append(
                tuple(
                    center[axis]
                    + TUBE_RADIUS
                    * (radial[0] * normal[axis] + radial[1] * binormal[axis])
                    for axis in range(3)
                )
            )
    faces = []
    for segment in range(SEGMENTS):
        next_segment = (segment + 1) % SEGMENTS
        for point in range(RING_POINTS):
            next_point = (point + 1) % RING_POINTS
            a = segment * RING_POINTS + point
            b = segment * RING_POINTS + next_point
            c = next_segment * RING_POINTS + point
            d = next_segment * RING_POINTS + next_point
            faces.append((a, c, b))
            faces.append((b, c, d))
    return vertices, faces


def blend(low: Color, high: Color, amount: float) -> Color:
    return tuple(
        round(low[channel] + (high[channel] - low[channel]) * amount)
        for channel in range(3)
    )


def trace_trefoil(t: float) -> Vector:
    return (
        math.sin(t) + 2.0 * math.sin(2.0 * t),
        math.cos(t) - 2.0 * math.cos(2.0 * t),
        -math.sin(3.0 * t) * 1.2,
    )


def subtract(a: Vector, b: Vector) -> Vector:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def cross(a: Vector, b: Vector) -> Vector:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def dot(a: Vector, b: Vector) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def normalize(vector: Vector) -> Vector:
    length = math.sqrt(dot(vector, vector)) or 1.0
    return (vector[0] / length, vector[1] / length, vector[2] / length)


if __name__ == "__main__":
    main()
