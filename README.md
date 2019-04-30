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

We're using a tool called [black](https://github.com/ambv/black) on this repo to ensure consistent formatting. On CI it runs in "check" mode to ensure any new files added to the repo are following PEP 8. If you see linter warnings that say something like "would reformat some_file.py" it means black disagrees with your formatting. 

**The easiest way to resolve these errors is to just run Black locally on the code and then committing those changes, as explained below.**

To automatically re-format your code to be consistent with our code style guidelines, run [black](https://github.com/ambv/black) in the repository root folder:

```sh
$ black .
```
