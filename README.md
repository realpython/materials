# Real Python Materials

Bonus materials, exercises, and example projects for our [Python tutorials](https://realpython.com).

Build Status: [![CircleCI](https://circleci.com/gh/realpython/materials.svg?style=svg)](https://circleci.com/gh/realpython/materials)

## Running Code Style Checks

We use [flake8](http://flake8.pycqa.org/en/latest/) and [black](https://github.com/ambv/black) to ensure a consistent code style for all of our sample code in this repository.

Run the following commands to validate your code against the linters:

```sh
$ flake8
$ black --check .
```

## Running Python Code Formatter

To automatically re-format your code to be consistent with our code style guidelines, run [black](https://github.com/ambv/black) in the repository root folder:

```sh
$ black .
```
