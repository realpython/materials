"""Invariants that import-linter and Ruff can't express."""

import ast
from pathlib import Path

DOMAIN = Path(__file__).parent.parent / "orders" / "domain"


def _is_frozen_dataclass(node: ast.ClassDef) -> bool | None:
    """Return None if not a dataclass, else whether it is frozen."""
    for deco in node.decorator_list:
        if isinstance(deco, ast.Name) and deco.id == "dataclass":
            return False
        if (
            isinstance(deco, ast.Call)
            and getattr(deco.func, "id", None) == "dataclass"
        ):
            return any(
                kw.arg == "frozen"
                and isinstance(kw.value, ast.Constant)
                and kw.value.value is True
                for kw in deco.keywords
            )
    return None


def test_domain_dataclasses_are_frozen():
    mutable = []
    for path in sorted(DOMAIN.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if _is_frozen_dataclass(node) is False:
                    mutable.append(f"{path.name}:{node.lineno} {node.name}")
    assert not mutable, f"Domain dataclasses must be frozen: {mutable}"
