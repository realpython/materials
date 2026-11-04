# Hardening AI-Generated Python Code With Bandit and Ruff

Sample code for the Real Python guide on hardening AI-generated Python with Bandit and Ruff.

- `insecure/helpers.py`: realistic "AI-generated" helpers with typical security issues
- `fixed/helpers.py`: the same helpers after fixes
- `pyproject.toml`: Bandit and Ruff settings (`bandit -c pyproject.toml`)
- `.pre-commit-config.yaml`: pre-commit hooks for Ruff and Bandit
- `.github/workflows/security.yml`: GitHub Actions workflow for your own repository

## Setup

Requires Python 3.11 or later.

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

## Run

```sh
(venv) $ bandit -r insecure
(venv) $ ruff check --select S insecure
(venv) $ bandit -r fixed -c pyproject.toml
(venv) $ ruff check fixed
```

The `pyproject.toml` here has one extra line that the guide's file doesn't: `extend-exclude = ["insecure"]`. It keeps the `realpython/materials` lint from failing on the deliberately insecure module. Remove that line to see the `ruff-check` pre-commit hook fail on `insecure/helpers.py`, as in Step 4.

The workflow in `.github/workflows/` runs only after you copy it into your own repository.
