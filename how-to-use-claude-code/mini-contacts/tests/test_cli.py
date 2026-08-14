import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from mini_contacts.cli import main


class CLITests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp_path = Path(tmp.name)

    def run_cli(self, *argv):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            main(list(argv))
        return stdout.getvalue()

    def test_add_then_list(self):
        path = str(self.tmp_path / "contacts.csv")
        self.run_cli(
            "--path",
            path,
            "add",
            "--name",
            "Alice",
            "--email",
            "alice@example.com",
            "--phone",
            "555-1234",
        )
        out = self.run_cli("--path", path, "list")
        self.assertIn("Alice", out)
        self.assertIn("alice@example.com", out)

    def test_list_empty(self):
        out = self.run_cli("--path", str(self.tmp_path / "empty.csv"), "list")
        self.assertIn("No contacts found.", out)

    def test_list_short_row_exits_cleanly(self):
        path = self.tmp_path / "contacts.csv"
        path.write_text("name,email,phone\nAlice,alice@example.com\n")
        out = self.run_cli("--path", str(path), "list")
        self.assertIn("Alice", out)
