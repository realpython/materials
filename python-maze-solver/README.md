# Build a Maze Solver in Python Using Graphs

This is the code for the Real Python tutorial [Build a Maze Solver in Python Using Graphs](https://realpython.com/python-maze-solver/).

## Installation

The code requires Python 3.10 or later and depends on the NetworkX library. You can install the project into an active virtual environment by issuing the following command from the project root folder:

```sh
(venv) $ python -m pip install .
```

For development, consider installing the code in editable mode:

```sh
(venv) $ python -m pip install --editable .
```

## Running

To run the maze solver, use the `solve` command and provide the path to a maze file:

```sh
$ solve /path/to/labyrinth.maze
```

Alternatively, you can use the more explicit yet equivalent command:

```sh
$ python -m maze_solver /path/to/labyrinth.maze
```

If the command succeeds, then you should see either a rendered solution in your default web browser or a relevant error message in the console.
