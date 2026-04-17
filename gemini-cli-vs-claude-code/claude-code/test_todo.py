"""Unit tests for the to-do application."""

import json
import os

import tempfile
import unittest
from unittest.mock import patch

import todo

# Point store at a temp file for every test
import todo_store as store


class BaseTest(unittest.TestCase):
    """Set up a temporary tasks file for each test."""

    def setUp(self):
        self._tmp = tempfile.NamedTemporaryFile(
            suffix=".json",
            delete=False,
            mode="w",
        )
        self._tmp.write("[]")
        self._tmp.close()
        self._orig = store.TASKS_FILE
        store.TASKS_FILE = self._tmp.name

    def tearDown(self):
        store.TASKS_FILE = self._orig
        os.unlink(self._tmp.name)


# ── store tests ─────────────────────────────────────────────────────────────


class TestAddTask(BaseTest):
    def test_add_returns_task(self):
        task = store.add_task("Buy milk")
        self.assertEqual(task["description"], "Buy milk")
        self.assertFalse(task["completed"])
        self.assertEqual(task["id"], 1)

    def test_ids_increment(self):
        t1 = store.add_task("First")
        t2 = store.add_task("Second")
        self.assertEqual(t1["id"], 1)
        self.assertEqual(t2["id"], 2)

    def test_empty_description_raises(self):
        with self.assertRaises(ValueError):
            store.add_task("")

    def test_whitespace_only_raises(self):
        with self.assertRaises(ValueError):
            store.add_task("   ")

    def test_persists_to_disk(self):
        store.add_task("Persisted")
        with open(store.TASKS_FILE) as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["description"], "Persisted")


class TestCompleteTask(BaseTest):
    def test_complete_task(self):
        store.add_task("Write tests")
        task = store.complete_task(1)
        self.assertTrue(task["completed"])
        self.assertIsNotNone(task["completed_at"])

    def test_complete_nonexistent_raises(self):
        with self.assertRaises(KeyError):
            store.complete_task(999)

    def test_complete_already_done_raises(self):
        store.add_task("Already done")
        store.complete_task(1)
        with self.assertRaises(ValueError):
            store.complete_task(1)


class TestDeleteTask(BaseTest):
    def test_delete_task(self):
        store.add_task("To delete")
        deleted = store.delete_task(1)
        self.assertEqual(deleted["description"], "To delete")
        self.assertEqual(store.load_tasks(), [])

    def test_delete_nonexistent_raises(self):
        with self.assertRaises(KeyError):
            store.delete_task(42)

    def test_remaining_tasks_intact(self):
        store.add_task("Keep me")
        store.add_task("Delete me")
        store.delete_task(2)
        tasks = store.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Keep me")


class TestFilterTasks(BaseTest):
    def setUp(self):
        super().setUp()
        store.add_task("Pending task")
        store.add_task("Completed task")
        store.complete_task(2)
        self.tasks = store.load_tasks()

    def test_filter_all(self):
        self.assertEqual(len(store.filter_tasks(self.tasks, "all")), 2)

    def test_filter_pending(self):
        result = store.filter_tasks(self.tasks, "pending")
        self.assertEqual(len(result), 1)
        self.assertFalse(result[0]["completed"])

    def test_filter_completed(self):
        result = store.filter_tasks(self.tasks, "completed")
        self.assertEqual(len(result), 1)
        self.assertTrue(result[0]["completed"])

    def test_filter_unknown_raises(self):
        with self.assertRaises(ValueError):
            store.filter_tasks(self.tasks, "invalid")


class TestCorruptedFile(BaseTest):
    def test_corrupted_json_raises(self):
        with open(store.TASKS_FILE, "w") as f:
            f.write("not valid json{{{")
        with self.assertRaises(ValueError):
            store.load_tasks()

    def test_non_array_json_raises(self):
        with open(store.TASKS_FILE, "w") as f:
            json.dump({"key": "value"}, f)
        with self.assertRaises(ValueError):
            store.load_tasks()

    def test_missing_file_returns_empty(self):
        os.unlink(store.TASKS_FILE)
        self.assertEqual(store.load_tasks(), [])
        # restore so tearDown doesn't crash
        with open(store.TASKS_FILE, "w") as f:
            f.write("[]")


# ── CLI integration tests ───────────────────────────────────────────────────


class TestCLI(BaseTest):
    def _run(self, argv):
        """Run CLI with given argv list, return exit code."""
        with patch("sys.argv", ["todo"] + argv):
            parser = todo.build_parser()
            args = parser.parse_args()
            return args.func(args)

    def test_add_command(self):
        code = self._run(["add", "CLI task"])
        self.assertEqual(code, 0)
        self.assertEqual(len(store.load_tasks()), 1)

    def test_list_command(self):
        store.add_task("Listed task")
        code = self._run(["list"])
        self.assertEqual(code, 0)

    def test_list_pending_filter(self):
        store.add_task("Pending")
        store.add_task("Done")
        store.complete_task(2)
        code = self._run(["list", "--status", "pending"])
        self.assertEqual(code, 0)

    def test_done_command(self):
        store.add_task("Mark done")
        code = self._run(["done", "1"])
        self.assertEqual(code, 0)
        self.assertTrue(store.load_tasks()[0]["completed"])

    def test_delete_command(self):
        store.add_task("Remove me")
        code = self._run(["delete", "1"])
        self.assertEqual(code, 0)
        self.assertEqual(store.load_tasks(), [])

    def test_done_missing_id_returns_error(self):
        code = self._run(["done", "99"])
        self.assertEqual(code, 1)

    def test_delete_missing_id_returns_error(self):
        code = self._run(["delete", "99"])
        self.assertEqual(code, 1)

    def test_add_empty_returns_error(self):
        code = self._run(["add", ""])
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
