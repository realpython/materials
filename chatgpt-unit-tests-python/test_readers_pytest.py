import json

import pytest

# Assuming JSONReader is defined in 'your_module.py'
from readers import JSONReader


@pytest.fixture
def setup_json_file(tmp_path):
    # Create a temporary JSON file
    data = {"name": "John Doe", "age": 30}
    file_path = tmp_path / "test_data.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)
    return file_path


def test_read_json_correctly(setup_json_file):
    # Test that JSONReader reads the file correctly
    reader = JSONReader(setup_json_file)
    data = reader.read()
    assert data == {
        "name": "John Doe",
        "age": 30,
    }, "Should correctly read JSON content"


def test_file_not_found():
    # Test for handling of file not found exception
    reader = JSONReader("non_existent_file.json")
    with pytest.raises(FileNotFoundError):
        reader.read()


# Additional tests can be added to cover more scenarios,
# such as reading empty files,
# files with invalid JSON content, etc.
