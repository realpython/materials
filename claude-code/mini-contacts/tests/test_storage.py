import tempfile
import unittest
from pathlib import Path

from mini_contacts import storage


class StorageTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp_path = Path(tmp.name)

    def test_round_trip(self):
        path = self.tmp_path / "contacts.csv"
        storage.add_contact(str(path), "Alice", "alice@example.com", "555-1234")
        expected = {
            "name": "Alice",
            "email": "alice@example.com",
            "phone": "555-1234",
        }
        self.assertEqual(storage.read_contacts(str(path)), [expected])

    def test_header_written_once(self):
        path = self.tmp_path / "contacts.csv"
        storage.add_contact(str(path), "Alice", "alice@example.com", "555-1234")
        storage.add_contact(str(path), "Bob", "bob@example.com", "555-5678")
        self.assertEqual(path.read_text().count("name,email,phone"), 1)

    def test_read_missing_file_returns_empty(self):
        missing = self.tmp_path / "missing.csv"
        self.assertEqual(storage.read_contacts(str(missing)), [])

    def test_short_row_filled_with_blanks(self):
        path = self.tmp_path / "contacts.csv"
        path.write_text("name,email,phone\nAlice,alice@example.com\n")
        contacts = storage.read_contacts(str(path))
        self.assertEqual(contacts[0]["phone"], "")

    def test_add_blank_field_raises(self):
        with self.assertRaises(ValueError):
            storage.add_contact(str(self.tmp_path / "c.csv"), "Alice", "", "555-1234")
