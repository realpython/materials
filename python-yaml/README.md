# YAML: The Missing Battery in Python

Python scripts and sample data for the [YAML: The Missing Battery in Python](https://realpython.com/mandelbrot-set-python) tutorial on Real Python.

## Installation

This code requires the following libraries:

- PyYAML
- FastAPI
- uvicorn

To install them, activate your [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), and type the following command:

```shell
(venv) $ python -m pip install -r requirements.txt
```

Additionally, you can install optional dependencies that were mentioned in the tutorial:

```shell
(venv) $ python -m pip install yamllint yq shyaml
```

## Usage

Print a sample YAML document with syntax highlighting:

```console
$ cat data.yaml | python colorize.py
```

Print a static HTML preview of a sample YAML document:

```console
$ cat data.yaml | python yaml2html.py
```

Print an interactive HTML preview of a sample YAML document:

```console
$ cat data.yaml | python tree.py
```

Start an interactive demo of a YAML formatter at <http://localhost:8000/>:

```console
$ cd formatter/
$ uvicorn server:app
```
