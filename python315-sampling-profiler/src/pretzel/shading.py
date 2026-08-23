"""NumPy-powered lighting. Most of this work runs in native code."""

import numpy as np
import numpy.typing as npt

from pretzel.engine import Face, Vertex

LIGHT_DIRECTION = np.array([0.35, 0.55, -0.75])
LIGHT_DIRECTION /= np.linalg.norm(LIGHT_DIRECTION)

CRUST_COLOR = np.array([224.0, 147.0, 65.0])


def sample_ambient_light(
    pixels: npt.NDArray[np.float32], tick: float
) -> float:
    samples = pixels[::2, ::2]
    height, width = samples.shape[:2]
    rows = np.arange(height, dtype=np.float32)[:, np.newaxis]
    columns = np.arange(width, dtype=np.float32)[np.newaxis, :]
    ripple = np.sin(rows / 20.0 + tick * 1.7) * np.cos(columns / 40.0 - tick)
    lit = samples.mean(axis=2) * (0.85 + 0.15 * ripple)
    return 0.15 + 0.3 * float(lit.mean()) / 255.0


def shade_faces(
    faces: list[Face], transformed: list[Vertex], ambient: float
) -> list[list[int]]:
    vertices = np.asarray(transformed)
    corners = vertices[np.asarray(faces)]
    edges_ab = corners[:, 1] - corners[:, 0]
    edges_ac = corners[:, 2] - corners[:, 0]
    normals = np.cross(edges_ac, edges_ab)
    normals /= np.linalg.norm(normals, axis=1, keepdims=True)
    diffuse = np.clip(normals @ LIGHT_DIRECTION, 0.0, 1.0)
    intensity = np.clip(ambient + (1.0 - ambient) * diffuse, 0.0, 1.0)
    return (CRUST_COLOR * intensity[:, np.newaxis]).astype(np.uint8).tolist()
