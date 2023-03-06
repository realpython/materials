# fmt: off
# flake8: noqa
from pathlib import Path

from maze_solver.models.border import Border
from maze_solver.models.maze import Maze
from maze_solver.models.role import Role
from maze_solver.models.square import Square


def main() -> None:
    build_maze().dump(Path(__file__).with_suffix(".maze"))


def build_maze() -> Maze:
    return Maze(
        squares=(
            Square(0, 0, 0, Border.EMPTY, Role.EXTERIOR),
            Square(1, 0, 1, Border.TOP | Border.LEFT),
            Square(2, 0, 2, Border.TOP | Border.BOTTOM),
            Square(3, 0, 3, Border.TOP | Border.RIGHT),
            Square(4, 0, 4, Border.BOTTOM | Border.LEFT, Role.EXTERIOR),
            Square(5, 1, 0, Border.TOP | Border.BOTTOM | Border.RIGHT, Role.EXIT),
            Square(6, 1, 1, Border.LEFT | Border.RIGHT),
            Square(7, 1, 2, Border.TOP | Border.BOTTOM | Border.LEFT | Border.RIGHT, Role.WALL),
            Square(8, 1, 3, Border.LEFT),
            Square(9, 1, 4, Border.TOP | Border.BOTTOM, Role.ENTRANCE),
            Square(10, 2, 0, Border.TOP | Border.RIGHT, Role.EXTERIOR),
            Square(11, 2, 1, Border.BOTTOM | Border.LEFT),
            Square(12, 2, 2, Border.TOP | Border.BOTTOM),
            Square(13, 2, 3, Border.BOTTOM | Border.RIGHT),
            Square(14, 2, 4, Border.TOP | Border.LEFT, Role.EXTERIOR),
        )
    )


if __name__ == '__main__':
    main()
