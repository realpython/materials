from dataclasses import dataclass

from maze_solver.models.border import Border
from maze_solver.models.role import Role


@dataclass(frozen=True)
class Square:
    index: int
    row: int
    column: int
    border: Border
    role: Role = Role.NONE
