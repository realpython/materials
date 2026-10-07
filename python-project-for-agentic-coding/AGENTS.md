# `AGENTS.md`

## Development workflow

- This project is typed. Run mypy after adding or modifying code:
  - `uv run mypy .`
- Use Ruff for formatting and linting:
  - `uv run ruff format .`
  - `uv run ruff check .`
- Run the full test suite after modifying code:
  - `uv run pytest`
- Add or update tests when changing behavior.
- Before committing, run:
  - `uv run pre-commit run --all-files`
- Prefer small, focused functions.

## Documentation
- Update documentation when public behavior changes.
