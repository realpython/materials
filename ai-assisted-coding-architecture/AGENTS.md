# Orders service: instructions for coding agents

## Layout

- `orders/domain/`: pure business rules. No I/O, no framework imports.
- `orders/services/`: use cases. Depend on `domain` and on the `Protocol`
  classes in `services/ports.py`, never on `adapters`.
- `orders/adapters/`: databases and network. May import `services` and
  `domain`.

## Invariants

1. Imports point inward only: adapters -> services -> domain.
2. Domain dataclasses are frozen.
3. Absolute imports only (`from orders.domain.models import Order`).
4. Use `datetime.now(UTC)`, never `datetime.utcnow()`.
5. Use `pathlib.Path`, not `os.path`.
6. Before writing a helper, search `orders/` for an existing one.

## Checks that must pass before you finish

Run each of these from the project root:

- `lint-imports`
- `ruff check . && ruff format --check .`
- `pytest`
- `pylint --disable=all --enable=duplicate-code orders`
- `vulture`

Decisions live in `docs/adr/`. Read the accepted ADRs before changing a
boundary, and propose a new ADR instead of editing an accepted one.
