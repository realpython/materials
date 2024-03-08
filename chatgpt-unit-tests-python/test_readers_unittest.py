import json
import os
import tempfile
import unittest

from readers import JSONReader


class TestJSONReader(unittest.TestCase):
    def setUp(self):
        """Set up a temporary file with sample JSON content."""
        self.temp_file = tempfile.NamedTemporaryFile(
            mode="w+", delete=False, encoding="utf-8"
        )
        self.sample_data = {"name": "Test", "age": 25}
        json.dump(self.sample_data, self.temp_file)
        self.temp_file.close()

        self.reader = JSONReader(self.temp_file.name)

    def tearDown(self):
        """Clean up by removing the temporary file."""
        os.remove(self.temp_file.name)

    def test_read(self):
        """Test reading JSON content from a temporary file."""
        result = self.reader.read()
        self.assertEqual(result, self.sample_data)


if __name__ == "__main__":
    unittest.main()
