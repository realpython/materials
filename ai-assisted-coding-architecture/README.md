# AI-Assisted Coding Architecture: Keep Python Code Coherent

Sample code for the Real Python article
[AI-Assisted Coding Architecture: Keep Python Code Coherent](https://realpython.com/ai-assisted-coding-architecture/).

A small layered `orders` package, with the guardrails that keep its
architecture intact: an `AGENTS.md` file, an import-linter contract, Ruff's
`banned-api` rule, an AST-based architecture test, duplicate-code detection
with Pylint, dead-code detection with Vulture, and an architecture decision
record.

## Setup

Python 3.11 or later is required.

```console
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

## Run the checks

```console
(venv) $ lint-imports
(venv) $ ruff check . && ruff format --check .
(venv) $ pytest
(venv) $ pylint --disable=all --enable=duplicate-code orders
(venv) $ vulture
```

## License

Distributed under the MIT license.
