import argparse
import pathlib

from maze_solver.graphs.solver import solve_all
from maze_solver.models.maze import Maze
from maze_solver.view.renderer import SVGRenderer


def main() -> None:
    maze = Maze.load(parse_path())
    solutions = solve_all(maze)
    if solutions:
        renderer = SVGRenderer()
        for solution in solutions:
            renderer.render(maze, solution).preview()
    else:
        print("No solution found")


def parse_path() -> pathlib.Path:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=pathlib.Path)
    return parser.parse_args().path


if __name__ == "__main__":
    main()
