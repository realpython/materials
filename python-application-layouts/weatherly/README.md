# weatherly

A small weather report CLI in a flat layout. The `weatherly` command comes
from the `[project.scripts]` table in `pyproject.toml`, and `__main__.py`
enables `python -m weatherly`.

**Note:** This example doesn't call any real weather API. The only provider,
`weatherly/sources/fake.py`, returns canned data so that the CLI runs offline
and without API keys.

## Installation

```console
$ python -m pip install -e ".[dev]"
```

## Usage

```console
$ weatherly lisbon --days 2
Forecast for Lisbon:
  Monday: Sunny, 12°C to 21°C
  Tuesday: Partly cloudy, 11°C to 19°C
```

Thanks to the flat layout, you can also run the package from the project
root without installing it:

```console
$ python -m weatherly lisbon --days 2
```

## Running the Tests

```console
$ python -m pytest
```
