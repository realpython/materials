import sys
from pathlib import Path

from maze_solver.models.maze import Maze
from maze_solver.view.renderer import SVGRenderer

if __name__ == "__main__":
    if len(sys.argv) > 1:
        SVGRenderer().render(Maze.load(Path(sys.argv[1]))).preview()
    else:
        print("Usage:\n$ python preview /path/to/file.maze")
