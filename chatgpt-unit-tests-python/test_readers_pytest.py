import json

import pytest

from readers import JSONReader


@pytest.fixture
def temp_json_file(tmp_path):
    data = {"name": "John Doe", "age": 30, "city": "New York"}
    file_path = tmp_path / "test_data.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)
    return file_path


def test_read_json(temp_json_file):
    reader = JSONReader(temp_json_file)
    data = reader.read()
    assert data == {"name": "John Doe", "age": 30, "city": "New York"}
