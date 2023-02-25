import json
import pathlib


def read(file):
    return json.loads(pathlib.Path(file).read_text())
