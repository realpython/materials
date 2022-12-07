# Advent of Code: Solving Your Puzzles With Python

This repository holds the code for the Real Python [Advent of Code: Solving Your Puzzles With Python](https://realpython.com/python-advent-of-code/) tutorial.

## Dependencies

[Pytest](https://realpython.com/pytest-python-testing/) is used for testing. You should first create a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

You can then install `pytest` with `pip`:

```console
(venv) $ python -m pip install pytest
```

The [aoc_grid.py](aoc_grid.py) example uses [Colorama](https://pypi.org/project/colorama/) and [NumPy](https://realpython.com/numpy-tutorial/). To run that example, you should also install those packages into your environment:

```console
(venv) $ python -m pip install colorama numpy
```

The puzzle solutions only use Python's standard library. Note that the solution to [Day 5, 2021](solutions/2021/05_hydrothermal_venture/) uses [structural pattern matching](https://realpython.com/python310-new-features/#structural-pattern-matching) which is only available in [Python 3.10](https://realpython.com/python310-new-features/) and later.

## Author

- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
