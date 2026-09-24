# How to Get Started With Jev in Python

Sample code for the Real Python tutorial [How to Get Started With Jev in Python](https://realpython.com/jev-python/).

## Setup

Create a `.env` file with your OpenRouter API key (see `.env.example`), then run the scripts with uv:

```console
$ uv run plain_python.py
$ uv run --env-file .env jev_noul.py
$ uv run --env-file .env jev_desk.py
```

uv reads `pyproject.toml` and installs `typesafe-sdk` on the first run. If you prefer pip, install the pinned dependency from `requirements.txt` instead.
