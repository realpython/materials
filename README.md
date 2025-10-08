# Real Python Materials

Bonus materials, exercises, and example projects for Real Python's [Python tutorials](https://realpython.com).

Build Status:
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/realpython/materials/linters.yml?branch=master)](https://github.com/realpython/materials/actions)

## Got a Question?

The best way to get support for Real Python courses, articles, and code in this repository is to join one of our [weekly Office Hours calls](https://realpython.com/office-hours/) or to ask your question in the [RP Community Chat](https://realpython.com/community/).

Due to time constraints, we cannot provide 1:1 support via GitHub. See you on Slack or on the next Office Hours call 🙂

## Adding Source Code & Sample Projects to This Repo (RP Contributors)

### Running Code Style Checks

We use [Ruff](https://realpython.com/ruff-python/) to ensure a consistent code style and formatting for all of our sample code in this repository.

Run the following commands to validate your code against the linters:

```sh
$ ruff format --check
$ ruff check
```

Make sure you're using the exact Ruff version specified in [`requirements.txt`](https://github.com/realpython/materials/blob/master/requirements.txt).

### Running Python Code Formatter

Ruff can automatically ensure a consistent code formatting in this repository. On CI, it runs in "check" mode to ensure any new files added to the repo follow [PEP 8](https://realpython.com/python-pep8/). If you see linter warnings that say something like "would reformat some_file.py", then it means that Ruff disagrees with your formatting.

The easiest way to resolve these errors is to run Ruff locally on the code and then commit those changes, as explained below.

To automatically reformat your code to be consistent with our code style guidelines, run [Ruff](https://pypi.org/project/ruff/) in the repository root folder:

```sh
$ ruff format
$ ruff check --fix
```
