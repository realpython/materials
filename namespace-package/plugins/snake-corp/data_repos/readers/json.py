import json
import pathlib


def read(file):
    """Read JSON file from a path."""
    return json.loads(pathlib.Path(file).read_text(encoding="utf-8"))
