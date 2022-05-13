# Documenting Your Python Project with MkDocs

This folder contains the source code and an example documentation built with [MkDocs](https://www.mkdocs.org), using the [Material for MkDocs](https://github.com/squidfunk/mkdocs-material) theme and the [mkdocstrings](https://mkdocstrings.github.io) plugin for docstring code discovery.

The code used is intentionally kept very basic and represents an unnecessary reproduction of fundamental math operations. This is done to keep the focus on _documenting_ a Python project, rather than the code itself.

You should be able to follow the same process and use the same concepts for your own Python project with more interesting code.

## Setup

To view the documentation project, navigate to `source_code` and install the dependencies into a new virtual environment:

**Linux, macOS:**

```bash
$ cd source_code
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

**Windows:**

```powershell
PS> cd source_code
PS> python -m venv venv
PS> venv\bin\Activate.ps1
(venv) PS> python -m pip install -r requirements.txt
```

Once you're set up and you've installed the dependencies, you can serve the project:

```bash
(venv) $ python -m mkdocs serve
```

Navigate to your localhost at port `8000` to view the generated documentation.

## Notes

Part of the documentation is auto-generate from docstrings in `source_code/calculator/`. The `mkdocstrings` package can render docstrings from both `__init__.py` package-level docstrings, as well as file and function docstrings from `calculations.py`.

You can find the relevant notation in `docs/index.md` and `docs/reference.md`.

The rest of the documentation is written in Markdown and split up across several files in the `docs/` directory.

In this project you can see that you can create project documentation that is partly auto-generated from your docstrings, interweaved with explanatory text and best-practice project documentation structure.
