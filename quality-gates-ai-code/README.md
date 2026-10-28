# How to Set Up Quality Gates for AI Code in Python

This folder contains the sample project for the Real Python tutorial [How to Set Up Quality Gates for AI Code in Python](https://realpython.com/quality-gates-ai-code/).

## Contents

- `pyproject.toml` and `uv.lock`: the pinned gate tools and their settings
- `.pre-commit-config.yaml`: the local pre-commit hooks
- `.github/workflows/ci.yml`: the GitHub Actions workflow with the `gates` and `diff-check` jobs
- `.github/CODEOWNERS`: code-owner review for the gate-defining files
- `scripts/agent_diff_check.py`: the agent diff sanity check
- `src/demo/ai_module.py` and `tests/test_ai_module.py`: the fixed module and its five tests
- `examples/ai_module_flawed.py` and `examples/test_ai_module_flawed.py`: the agent's flawed module and its two tests

The `examples/` folder holds deliberately broken code, so `pyproject.toml` excludes it from Ruff and pytest.

## Setup

You need [uv](https://docs.astral.sh/uv/) 0.13.3 and Git:

```console
$ uv sync --locked
$ uv run pytest
```

To reproduce the flawed state from the tutorial, copy the files from `examples/` over `src/demo/ai_module.py` and `tests/test_ai_module.py`.

Replace `@your-username` in `.github/CODEOWNERS` with your GitHub user or team before you push.
