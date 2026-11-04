# AI Engineering Skills: Prompt, Context, Harness, Loop

This folder contains the sample project for the Real Python tutorial [AI Engineering Skills: Prompt, Context, Harness, Loop](https://realpython.com/ai-engineering-layers/).

It's a small Flask checkout API backed by SQLite, plus `loop.py`, a script that hands the failing tests to Claude Code one test at a time. The app is **broken on purpose**: it has four bugs and five failing tests for the agent to fix.

- `app/api.py`: The `POST /checkout` endpoint, which logs every error to `app.log` and returns a 500 status code
- `app/db.py`: The SQLite schema and item prices
- `tests/test_checkout.py`: The five tests
- `loop.py`: The loop that runs `pytest` and calls `claude -p` until the tests pass or it gives up after `MAX_RUNS` runs

## Installation

You need Python 3.12 or later. Create and activate a virtual environment, then install the pinned requirements:

```sh
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

This installs `flask==3.1.3` and `pytest==9.1.1`.

## Run the Tests

From this folder, run:

```sh
(venv) $ python -m pytest -q
...
FAILED tests/test_checkout.py::test_checkout_creates_order - assert 500 == 201
FAILED tests/test_checkout.py::test_checkout_totals_the_quantity - KeyError: ...
FAILED tests/test_checkout.py::test_unknown_item_is_rejected - assert 500 == 400
FAILED tests/test_checkout.py::test_orders_endpoint_lists_orders - assert 404...
FAILED tests/test_checkout.py::test_order_ids_increment - KeyError: 'id'
5 failed in 0.45s
(venv) $ tail -1 app.log
sqlite3.OperationalError: table orders has no column named created_at
```

## Run the Loop

Running `loop.py` needs [Claude Code](https://code.claude.com/docs/en/overview) installed and logged in, with `claude` on your `PATH`. The flags were verified with Claude Code 2.1.308. The script lets the agent edit files under `app/`, so work on a copy of this folder:

```sh
(venv) $ python loop.py
```

Each run prints how many tests fail and which one it hands over, and the script ends with `All tests pass after N agent run(s).` or `Gave up after 5 runs.` A real agent may fix more than one bug per run, so the number of runs varies from one try to the next.
