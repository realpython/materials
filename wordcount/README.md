# Learn by Doing: Build a Clone of the Unix `wc` Shell Command

This folder contains supporting materials for the [wordcount coding challenge](https://realpython.com/courses/wordcount/) on Real Python.

## How to Get Started?

### Cloud Environment

If you'd like to solve this challenge with a minimal setup required, then click the button below to launch a pre-configured environment in the cloud:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/realpython/materials?quickstart=1&devcontainer_path=.devcontainer%2Fwordcount%2Fdevcontainer.json)

Alternatively, follow the steps below to set up the environment on your local machine.

### Local Computer

Use the [downloader tool](https://realpython.github.io/gh-download/?url=https%3A%2F%2Fgithub.com%2Frealpython%2Fmaterials%2Ftree%2Fmaster%2Fwordcount) to get the project files or clone the entire [`realpython/materials`](https://github.com/realpython/materials) repository from GitHub and change your directory to `materials/wordcount/`:

```sh
$ git clone https://github.com/realpython/materials.git
$ cd materials/wordcount/
```

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), and then install the project in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html):

```sh
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt -e .
```

Make sure to include the period at the end of the command!

## How to Get Feedback?

To display instructions for your current task:

```sh
(venv) $ pytest --task
```

To track your progress and reveal the acceptance criteria:

```sh
(venv) $ pytest
```
