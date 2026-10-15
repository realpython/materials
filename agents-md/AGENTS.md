## Project Domain

This is a REST API for browsing and managing a collection of cars.
Each car is a complete record with a unique, server-assigned `id`
and the fields `make`, `model`, `year`, `horsepower`, `engine_cc`,
and `transmission`.

The `engine_cc` field can be `0` for fully electric cars. Every
car you return or store must include all fields.

## Project Setup and Management

- Python version: 3.14. Don't use newer syntax.
- Dependency management: `uv` and `pyproject.toml`. Never use `pip`
  or a `requirements.txt` file.
- Add a dependency with `uv add <package>`. Never use `uv pip`
  for dependencies.
- Run the app with `uv run fastapi dev main.py`.
- Branch from `main` as `feature/<name>` and use Conventional Commits.
- Stage changes for review. Don't commit to `main` or push without
  being asked.

## Coding Conventions

- Type-hint public functions and methods, including their return types.
- Use `pathlib` for path management. Don't use `os.path`.
- Prefer f-strings over `str.format()` or `%` formatting.
- Follow EAFP: handle exceptions rather than checking conditions up front.
- Write Google-style docstrings for every public function and method.
- Validate request bodies with Pydantic models.
- Embrace idiomatic Python like comprehensions, generators, and decorators.

## Project Structure

- The project is flat: `main.py` holds the app and `cars.json` holds
  the data.
- The `main.py` file is the only module to edit when adding features.
- Put tests in `tests/test_main.py`.
- Don't create new packages or new files without being asked.

## Quality Gates

A task is done only when all of these pass:

- `uv run ruff format` leaves the code unchanged.
- `uv run ruff check` reports no errors.
- `uv run mypy main.py` reports no errors.
- `uv run pytest` passes, with a test added for every new endpoint.

## Constraints

- Ask before adding any external dependency.
- Preserve the signature and response shape of existing endpoints.
- Don't use blocking I/O inside `async` functions.
- Keep existing tests intact, and fix the code to make them pass.
- Declare a task done only after the gates pass and docstrings are
  updated.

## Ignore

Treat everything in `.gitignore` as off-limits to read or edit. On top of
that, never open:

- Secrets and `.env` files
- Large data files unrelated to the current task
- Vendored or generated code
