# How to Sort Unicode Strings Alphabetically in Python

This folder contains sample code for the Real Python tutorial [How to Sort Unicode Strings Alphabetically in Python](https://realpython.com/python-sort-unicode-strings/).

## Usage

You can either open the HTML file with the rendered Jupyter notebook or use a Jupyter server to view and interact with the notebook directly.

## Installation

Create and activate a new virtual environment:

```shell
$ python3 -m venv venv/
$ source venv/bin/activate
```

Install the necessary requirements into your virtual environment:

```shell
(venv) $ python -m pip install -r requirements.txt
```

In case of problems, you can try installing these dependencies manually:

- [JupyterLab](https://pypi.org/project/jupyterlab/)
- [natsort](https://pypi.org/project/natsort/)
- [PyICU](https://pypi.org/project/PyICU/)
- [pyuca](https://pypi.org/project/pyuca/)
- [Unidecode](https://pypi.org/project/Unidecode/)

**Note:** PyICU requires a C++ compiler and a few third-party libraries to install correctly. Check the official [README](https://gitlab.pyicu.org/main/pyicu/-/blob/48f4f527a344787346e8c10c68859679435e0cb4/README.md) file for more details if needed.

Open the notebook in Jupyter Lab:

```shell
(venv) python -m jupyter lab python-sort-unicode-strings.ipynb
```
