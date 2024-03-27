import json
import os
import tempfile
import unittest

from readers import JSONReader


class TestJSONReader(unittest.TestCase):
    def setUp(self):
        # Create a temporary file and write some JSON data to it
        self.temp_file, self.temp_file_path = tempfile.mkstemp(suffix=".json")
        self.test_data = {"name": "Test", "value": 123}
        with os.fdopen(self.temp_file, "w", encoding="utf-8") as file:
            json.dump(self.test_data, file)

    def tearDown(self):
        # Clean up by removing the temporary file
        os.remove(self.temp_file_path)

    def test_read_json(self):
        # Test reading the JSON data
        reader = JSONReader(self.temp_file_path)
        data = reader.read()
        self.assertEqual(data, self.test_data)

    def test_file_not_found(self):
        # Test file not found error handling
        reader = JSONReader("non_existent_file.json")
        with self.assertRaises(FileNotFoundError):
            _ = reader.read()


if __name__ == "__main__":
    unittest.main()
