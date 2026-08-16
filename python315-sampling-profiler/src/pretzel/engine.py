"""Pure-Python 3D math: rotation, projection, culling, and sorting."""

import math
from dataclasses import dataclass

type Vertex = tuple[float, float, float]
type Face = tuple[int, int, int]
type Point = tuple[float, float]
type Matrix = tuple[
    tuple[float, float, float],
    tuple[float, float, float],
    tuple[float, float, float],
]


@dataclass
class Mesh:
    vertices: list[Vertex]
    faces: list[Face]


def rotation_matrix(pitch: float, yaw: float, roll: float) -> Matrix:
    sin_p, cos_p = math.sin(pitch), math.cos(pitch)
    sin_y, cos_y = math.sin(yaw), math.cos(yaw)
    sin_r, cos_r = math.sin(roll), math.cos(roll)
    return (
        (
            cos_y * cos_r + sin_y * sin_p * sin_r,
            cos_p * sin_r,
            -sin_y * cos_r + cos_y * sin_p * sin_r,
        ),
        (
            -cos_y * sin_r + sin_y * sin_p * cos_r,
            cos_p * cos_r,
            sin_y * sin_r + cos_y * sin_p * cos_r,
        ),
        (sin_y * cos_p, -sin_p, cos_y * cos_p),
    )


def transform_vertices(
    vertices: list[Vertex], matrix: Matrix, distance: float
) -> list[Vertex]:
    (xx, xy, xz), (yx, yy, yz), (zx, zy, zz) = matrix
    transformed = []
    for x, y, z in vertices:
        tx = xx * x + xy * y + xz * z
        ty = yx * x + yy * y + yz * z
        tz = zx * x + zy * y + zz * z + distance
        transformed.append((tx, ty, tz))
    return transformed


def project_vertices(
    transformed: list[Vertex], width: int, height: int, focal_length: float
) -> list[Point]:
    half_width, half_height = width / 2, height / 2
    projected = []
    for x, y, z in transformed:
        scale = focal_length / z
        projected.append((half_width + x * scale, half_height - y * scale))
    return projected


def cull_backfaces(faces: list[Face], projected: list[Point]) -> list[Face]:
    visible = []
    for face in faces:
        a, b, c = face
        ax, ay = projected[a]
        bx, by = projected[b]
        cx, cy = projected[c]
        if (bx - ax) * (cy - ay) - (by - ay) * (cx - ax) < 0:
            visible.append(face)
    return visible


def sort_back_to_front(
    faces: list[Face], transformed: list[Vertex]
) -> list[Face]:
    def face_depth(face: Face) -> float:
        a, b, c = face
        return transformed[a][2] + transformed[b][2] + transformed[c][2]

    return sorted(faces, key=face_depth, reverse=True)
