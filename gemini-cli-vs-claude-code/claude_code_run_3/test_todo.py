"""Unit tests for the to-do CLI application."""

import argparse
import json
import os
import tempfile
import unittest
from unittest.mock import patch

from todo_storage import load_tasks, make_task, save_tasks
from todo import cmd_add, cmd_clear, cmd_delete, cmd_done, cmd_list


# ── helpers ───────────────────────────────────────────────────────────────────

def _args(**kwargs) -> argparse.Namespace:
    """Build a minimal Namespace for command handlers."""
    defaults = {"file": None}  # file is always set in tests via tmp_file
    defaults.update(kwargs)
    return argparse.Namespace(**defaults)


class TmpFileMixin(unittest.TestCase):
    """Creates a fresh temp JSON file before each test and removes it after."""

    def setUp(self):
        fd, self.tmp_file = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        os.remove(self.tmp_file)  # start with no file (tests creation from scratch)

    def tearDown(self):
        if os.path.exists(self.tmp_file):
            os.remove(self.tmp_file)


# ── storage layer tests ───────────────────────────────────────────────────────

class TestStorage(TmpFileMixin):

    def test_load_missing_file_returns_empty(self):
        tasks = load_tasks(self.tmp_file)
        self.assertEqual(tasks, [])

    def test_save_and_reload(self):
        task = make_task("Hello world")
        save_tasks([task], self.tmp_file)
        loaded = load_tasks(self.tmp_file)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["title"], "Hello world")
        self.assertFalse(loaded[0]["done"])

    def test_make_task_strips_whitespace(self):
        task = make_task("  trim me  ")
        self.assertEqual(task["title"], "trim me")

    def test_make_task_has_required_keys(self):
        task = make_task("x")
        for key in ("id", "title", "done", "created_at"):
            self.assertIn(key, task)

    def test_load_corrupt_json_raises(self):
        with open(self.tmp_file, "w") as f:
            f.write("{not valid json}")
        with self.assertRaises(ValueError):
            load_tasks(self.tmp_file)

    def test_load_wrong_type_raises(self):
        with open(self.tmp_file, "w") as f:
            json.dump({"oops": "a dict"}, f)
        with self.assertRaises(ValueError):
            load_tasks(self.tmp_file)


# ── add command ───────────────────────────────────────────────────────────────

class TestCmdAdd(TmpFileMixin):

    def test_add_creates_task(self):
        args = _args(title=["Buy", "milk"], file=self.tmp_file)
        cmd_add(args)
        tasks = load_tasks(self.tmp_file)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Buy milk")

    def test_add_multiple_tasks(self):
        for title in ["Task A", "Task B", "Task C"]:
            cmd_add(_args(title=[title], file=self.tmp_file))
        tasks = load_tasks(self.tmp_file)
        self.assertEqual(len(tasks), 3)

    def test_add_empty_title_exits(self):
        args = _args(title=["   "], file=self.tmp_file)
        with self.assertRaises(SystemExit):
            cmd_add(args)

    def test_add_new_task_is_pending(self):
        cmd_add(_args(title=["Check this"], file=self.tmp_file))
        tasks = load_tasks(self.tmp_file)
        self.assertFalse(tasks[0]["done"])


# ── done command ──────────────────────────────────────────────────────────────

class TestCmdDone(TmpFileMixin):

    def _seed(self, *titles):
        tasks = [make_task(t) for t in titles]
        save_tasks(tasks, self.tmp_file)
        return tasks

    def test_mark_done(self):
        tasks = self._seed("Read book")
        task_id = tasks[0]["id"]
        cmd_done(_args(id=task_id, file=self.tmp_file))
        loaded = load_tasks(self.tmp_file)
        self.assertTrue(loaded[0]["done"])

    def test_mark_done_invalid_id_exits(self):
        self._seed("Read book")
        with self.assertRaises(SystemExit):
            cmd_done(_args(id="no-such", file=self.tmp_file))

    def test_mark_already_done_is_idempotent(self):
        tasks = self._seed("Read book")
        tid = tasks[0]["id"]
        cmd_done(_args(id=tid, file=self.tmp_file))
        cmd_done(_args(id=tid, file=self.tmp_file))  # second call — should not crash
        loaded = load_tasks(self.tmp_file)
        self.assertTrue(loaded[0]["done"])


# ── delete command ────────────────────────────────────────────────────────────

class TestCmdDelete(TmpFileMixin):

    def test_delete_removes_task(self):
        task = make_task("Temp task")
        save_tasks([task], self.tmp_file)
        cmd_delete(_args(id=task["id"], file=self.tmp_file))
        tasks = load_tasks(self.tmp_file)
        self.assertEqual(tasks, [])

    def test_delete_nonexistent_exits(self):
        save_tasks([], self.tmp_file)
        with self.assertRaises(SystemExit):
            cmd_delete(_args(id="ghost", file=self.tmp_file))

    def test_delete_leaves_others_intact(self):
        a, b = make_task("Keep"), make_task("Remove")
        save_tasks([a, b], self.tmp_file)
        cmd_delete(_args(id=b["id"], file=self.tmp_file))
        tasks = load_tasks(self.tmp_file)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["id"], a["id"])


# ── list command ──────────────────────────────────────────────────────────────

class TestCmdList(TmpFileMixin):

    def _seed_mixed(self):
        tasks = [make_task("Pending A"), make_task("Done B"), make_task("Pending C")]
        tasks[1]["done"] = True
        save_tasks(tasks, self.tmp_file)
        return tasks

    def test_list_all(self):
        self._seed_mixed()
        with patch("builtins.print") as mock_print:
            cmd_list(_args(filter="all", file=self.tmp_file))
        output = " ".join(str(c) for call in mock_print.call_args_list for c in call[0])
        self.assertIn("Done B", output)
        self.assertIn("Pending A", output)

    def test_list_filter_done(self):
        self._seed_mixed()
        with patch("builtins.print") as mock_print:
            cmd_list(_args(filter="done", file=self.tmp_file))
        output = " ".join(str(c) for call in mock_print.call_args_list for c in call[0])
        self.assertIn("Done B", output)
        self.assertNotIn("Pending A", output)

    def test_list_filter_pending(self):
        self._seed_mixed()
        with patch("builtins.print") as mock_print:
            cmd_list(_args(filter="pending", file=self.tmp_file))
        output = " ".join(str(c) for call in mock_print.call_args_list for c in call[0])
        self.assertIn("Pending A", output)
        self.assertNotIn("Done B", output)

    def test_list_empty(self):
        with patch("builtins.print") as mock_print:
            cmd_list(_args(filter="all", file=self.tmp_file))
        output = " ".join(str(c) for call in mock_print.call_args_list for c in call[0])
        self.assertIn("No tasks", output)


# ── clear command ─────────────────────────────────────────────────────────────

class TestCmdClear(TmpFileMixin):

    def test_clear_removes_done_tasks(self):
        tasks = [make_task("Keep"), make_task("Remove")]
        tasks[1]["done"] = True
        save_tasks(tasks, self.tmp_file)
        cmd_clear(_args(file=self.tmp_file))
        remaining = load_tasks(self.tmp_file)
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0]["title"], "Keep")

    def test_clear_no_done_tasks(self):
        save_tasks([make_task("Still here")], self.tmp_file)
        with patch("builtins.print") as mock_print:
            cmd_clear(_args(file=self.tmp_file))
        output = " ".join(str(c) for call in mock_print.call_args_list for c in call[0])
        self.assertIn("No completed", output)

    def test_clear_empty_list(self):
        # should not crash on an empty list
        cmd_clear(_args(file=self.tmp_file))


if __name__ == "__main__":
    unittest.main(verbosity=2)
