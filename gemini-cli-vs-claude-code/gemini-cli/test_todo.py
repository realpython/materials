# import json
import os
import unittest

from todo import TodoManager


class TestTodoManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.json"
        # Ensure a clean slate for each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.manager = TodoManager(filename=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        task = self.manager.add_task("Test task")
        self.assertEqual(task["description"], "Test task")
        self.assertEqual(task["id"], 1)
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.tasks), 1)

    def test_complete_task(self):
        self.manager.add_task("Test task")
        success = self.manager.complete_task(1)
        self.assertTrue(success)
        self.assertTrue(self.manager.tasks[0]["completed"])

    def test_complete_non_existent_task(self):
        success = self.manager.complete_task(999)
        self.assertFalse(success)

    def test_delete_task(self):
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        success = self.manager.delete_task(1)
        self.assertTrue(success)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0]["id"], 2)

    def test_list_tasks_filtering(self):
        self.manager.add_task("Pending task")
        self.manager.add_task("Completed task")
        self.manager.complete_task(2)

        all_tasks = self.manager.list_tasks()
        pending_tasks = self.manager.list_tasks(filter_status="pending")
        completed_tasks = self.manager.list_tasks(filter_status="completed")

        self.assertEqual(len(all_tasks), 2)
        self.assertEqual(len(pending_tasks), 1)
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(pending_tasks[0]["description"], "Pending task")
        self.assertEqual(completed_tasks[0]["description"], "Completed task")

    def test_persistence(self):
        self.manager.add_task("Persistent task")
        # Create a new manager instance pointing to the same file
        new_manager = TodoManager(filename=self.test_file)
        self.assertEqual(len(new_manager.tasks), 1)
        self.assertEqual(
            new_manager.tasks[0]["description"],
            "Persistent task",
        )


if __name__ == "__main__":
    unittest.main()
