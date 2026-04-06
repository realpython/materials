"""Unit tests for todo.py."""

import json
import unittest
from pathlib import Path
from unittest.mock import patch

import todo


def _make_tasks(*titles: str) -> list[dict]:
    """Helper: build an in-memory task list."""
    return [
        {
            "id": i + 1,
            "title": t,
            "completed": False,
            "created_at": "2026-03-24T10:00:00",
        }
        for i, t in enumerate(titles)
    ]


class TestStorage(unittest.TestCase):
    """Tests for _load / _save / _next_id / _find."""

    def setUp(self):
        self.path = Path("test_tasks_tmp.json")
        patcher = patch.object(todo, "STORAGE_FILE", self.path)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self._cleanup)

    def _cleanup(self):
        if self.path.exists():
            self.path.unlink()

    def test_load_returns_empty_list_when_file_missing(self):
        self.assertFalse(self.path.exists())
        self.assertEqual(todo._load(), [])

    def test_save_and_load_roundtrip(self):
        tasks = _make_tasks("Task A", "Task B")
        todo._save(tasks)
        loaded = todo._load()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0]["title"], "Task A")
        self.assertEqual(loaded[1]["title"], "Task B")

    def test_load_raises_on_corrupt_json(self):
        self.path.write_text("not-json", encoding="utf-8")
        with self.assertRaises(SystemExit) as ctx:
            todo._load()
        self.assertIn("Could not parse", str(ctx.exception))

    def test_load_raises_on_non_list_json(self):
        self.path.write_text('{"key": "value"}', encoding="utf-8")
        with self.assertRaises(SystemExit) as ctx:
            todo._load()
        self.assertIn("Corrupt", str(ctx.exception))

    def test_next_id_on_empty(self):
        self.assertEqual(todo._next_id([]), 1)

    def test_next_id_increments(self):
        tasks = _make_tasks("A", "B", "C")
        self.assertEqual(todo._next_id(tasks), 4)

    def test_find_returns_task(self):
        tasks = _make_tasks("X", "Y")
        self.assertEqual(todo._find(tasks, 2)["title"], "Y")

    def test_find_returns_none_for_missing(self):
        tasks = _make_tasks("X")
        self.assertIsNone(todo._find(tasks, 99))


class TestCmdAdd(unittest.TestCase):
    def setUp(self):
        self.path = Path("test_tasks_tmp.json")
        patcher = patch.object(todo, "STORAGE_FILE", self.path)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(lambda: self.path.exists() and self.path.unlink())

    def test_add_creates_task(self):
        todo.main(["add", "Buy milk"])
        tasks = todo._load()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Buy milk")
        self.assertFalse(tasks[0]["completed"])
        self.assertEqual(tasks[0]["id"], 1)

    def test_add_multiple_tasks_increments_ids(self):
        todo.main(["add", "Task 1"])
        todo.main(["add", "Task 2"])
        tasks = todo._load()
        self.assertEqual(tasks[0]["id"], 1)
        self.assertEqual(tasks[1]["id"], 2)

    def test_add_empty_title_raises(self):
        with self.assertRaises(SystemExit) as ctx:
            todo.main(["add", "   "])
        self.assertIn("empty", str(ctx.exception))


class TestCmdDone(unittest.TestCase):
    def setUp(self):
        self.path = Path("test_tasks_tmp.json")
        patcher = patch.object(todo, "STORAGE_FILE", self.path)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(lambda: self.path.exists() and self.path.unlink())
        todo._save(_make_tasks("Task A", "Task B"))

    def test_mark_done(self):
        todo.main(["done", "1"])
        tasks = todo._load()
        self.assertTrue(tasks[0]["completed"])
        self.assertFalse(tasks[1]["completed"])

    def test_done_invalid_id_raises(self):
        with self.assertRaises(SystemExit) as ctx:
            todo.main(["done", "99"])
        self.assertIn("No task with id 99", str(ctx.exception))

    def test_done_already_completed_is_idempotent(self):
        todo.main(["done", "1"])
        todo.main(["done", "1"])  # should not raise
        tasks = todo._load()
        self.assertTrue(tasks[0]["completed"])


class TestCmdDelete(unittest.TestCase):
    def setUp(self):
        self.path = Path("test_tasks_tmp.json")
        patcher = patch.object(todo, "STORAGE_FILE", self.path)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(lambda: self.path.exists() and self.path.unlink())
        todo._save(_make_tasks("Task A", "Task B", "Task C"))

    def test_delete_removes_task(self):
        todo.main(["delete", "2"])
        tasks = todo._load()
        self.assertEqual(len(tasks), 2)
        self.assertIsNone(todo._find(tasks, 2))

    def test_delete_invalid_id_raises(self):
        with self.assertRaises(SystemExit) as ctx:
            todo.main(["delete", "99"])
        self.assertIn("No task with id 99", str(ctx.exception))


class TestCmdList(unittest.TestCase):
    def setUp(self):
        self.path = Path("test_tasks_tmp.json")
        patcher = patch.object(todo, "STORAGE_FILE", self.path)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(lambda: self.path.exists() and self.path.unlink())

        tasks = _make_tasks("Task A", "Task B", "Task C")
        tasks[0]["completed"] = True  # Task A is done
        todo._save(tasks)

    def test_list_all(self):
        # Should not raise
        todo.main(["list"])

    def test_list_completed_filter(self, ):
        # Should not raise; only task A is completed
        todo.main(["list", "--filter", "completed"])

    def test_list_pending_filter(self):
        todo.main(["list", "--filter", "pending"])

    def test_list_empty_shows_message(self):
        todo._save([])
        with patch("builtins.print") as mock_print:
            todo.main(["list"])
        printed = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertIn("No", printed)

    def test_list_completed_filter_content(self):
        with patch("builtins.print") as mock_print:
            todo.main(["list", "--filter", "completed"])
        output = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertIn("Task A", output)
        self.assertNotIn("Task B", output)

    def test_list_pending_filter_content(self):
        with patch("builtins.print") as mock_print:
            todo.main(["list", "--filter", "pending"])
        output = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertNotIn("Task A", output)
        self.assertIn("Task B", output)
        self.assertIn("Task C", output)


if __name__ == "__main__":
    unittest.main()
