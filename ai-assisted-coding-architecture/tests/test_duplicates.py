"""Fail when two functions differ only in names and docstrings."""

import ast
from pathlib import Path

MIN_NODES = 40
PACKAGE = Path(__file__).parent.parent / "orders"


def normalize(func: ast.FunctionDef) -> str:
    """Dump the body with local names replaced by numbered placeholders."""
    params = [
        arg.arg for arg in ast.walk(func.args) if isinstance(arg, ast.arg)
    ]
    local = set(params) | {
        n.id
        for n in ast.walk(func)
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)
    }
    placeholders = {name: number for number, name in enumerate(params)}

    class Rename(ast.NodeTransformer):
        def visit_Name(self, node):
            if node.id in local:
                number = placeholders.setdefault(node.id, len(placeholders))
                return ast.Name(id=f"_{number}", ctx=node.ctx)
            return node

        def visit_arg(self, node):
            number = placeholders.setdefault(node.arg, len(placeholders))
            return ast.arg(arg=f"_{number}")

    body = func.body
    if ast.get_docstring(func) is not None:
        body = body[1:]
    module = ast.Module(body=body, type_ignores=[])
    return ast.dump(Rename().visit(module))


def test_no_renamed_duplicates():
    seen = {}
    for path in sorted(PACKAGE.rglob("*.py")):
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if isinstance(node, ast.FunctionDef):
                key = normalize(node)
                if key.count("(") >= MIN_NODES:
                    seen.setdefault(key, []).append(
                        f"{path.name}:{node.lineno} {node.name}"
                    )
    clones = [places for places in seen.values() if len(places) > 1]
    assert not clones, f"Same logic under different names: {clones}"
