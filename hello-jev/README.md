# Hello Jev: Getting Started With Jev in Python

This folder provides the code examples for *Get Started With Jev in Python*,
a video on the [Real Python YouTube channel](https://www.youtube.com/@realpython).

Both scripts run the same train-station info desk. The desk asks a visitor
whether they lost something and then points them at the lost-and-found counter
or asks what else it can help with. The difference is how the answer is read:

- **`plain_python.py`** handles the input by hand. It only accepts an uppercase
  `Y` or `N`, so anything else sends the visitor back around the loop.
- **`jev_noul.py`** replaces that branching with a single `Noul` question. Jev
  scores how affirmative the answer is on a scale from `0` to `1`, so the script
  compares thresholds instead of strings and understands replies like
  `yeah, I've lost something`.

## Setup

Install [uv](https://docs.astral.sh/uv/), then create the virtual environment.
Because `pyproject.toml` pins `requires-python = ">=3.14"`, uv downloads
CPython 3.14 for you if you don't have it yet:

```sh
$ uv sync
```

`jev_noul.py` reaches Jev through [OpenRouter](https://openrouter.ai/), which
lets you try the model without opening an account with TypeSafe AI. Grab an
OpenRouter API key, then create a `.env` file next to the scripts and add it:

```dotenv
OPENROUTER_API_KEY=<YOUR-OPENROUTER-KEY>
```

Keep `.env` out of version control. An API key belongs in your environment, not
in your repository.

## Running the Examples

Start with the plain script to see where hand-written input handling gives up:

```sh
$ uv run plain_python.py
Did you lose something? (Y/N)
```

Only an uppercase `Y` or `N` gets you past the prompt. Try `yes` or `y` and the
script asks again.

Now run the Jev version. The `--env-file` flag tells uv to load your API key
from `.env` before it starts the script:

```sh
$ uv run --env-file .env jev_noul.py
Did you lose something?
```

Answer in your own words. `jev_noul.py` treats a Noul above `0.8` as a yes and
below `0.2` as a no, and asks again for anything in between.

## Where to Go Next

`Noul` is one of three Jev primitives. `Score` rates something on a scale, and
`Choice` picks from a list of options. The
[TypeSafe SDK on PyPI](https://pypi.org/project/typesafe-sdk/) documents all
three, and the TypeSafe AI blog explains the idea behind them in
[Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev).
