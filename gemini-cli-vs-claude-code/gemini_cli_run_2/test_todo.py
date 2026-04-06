import unittest
from unittest.mock import MagicMock
from todo_manager import TodoManager, Task

class TestTodoManager(unittest.TestCase):
    def setUp(self):
        self.mock_storage = MagicMock()
        self.mock_storage.load_tasks.return_value = []
        self.manager = TodoManager(storage=self.mock_storage)

    def test_add_task(self):
        task = self.manager.add_task("Test task")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(task.description, "Test task")
        self.assertEqual(task.id, 1)
        self.mock_storage.save_tasks.assert_called()

    def test_mark_completed(self):
        self.manager.add_task("Test task")
        result = self.manager.mark_completed(1)
        self.assertTrue(result)
        self.assertTrue(self.manager.tasks[0].completed)
        self.mock_storage.save_tasks.assert_called()

    def test_mark_completed_invalid_id(self):
        result = self.manager.mark_completed(99)
        self.assertFalse(result)

    def test_delete_task(self):
        self.manager.add_task("Test task")
        result = self.manager.delete_task(1)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.tasks), 0)
        self.mock_storage.save_tasks.assert_called()

    def test_delete_task_invalid_id(self):
        result = self.manager.delete_task(99)
        self.assertFalse(result)

    def test_list_tasks_filter(self):
        self.manager.add_task("Pending task")
        task2 = self.manager.add_task("Completed task")
        self.manager.mark_completed(task2.id)

        pending_tasks = self.manager.list_tasks(filter_type='pending')
        completed_tasks = self.manager.list_tasks(filter_type='completed')
        all_tasks = self.manager.list_tasks(filter_type='all')

        self.assertEqual(len(pending_tasks), 1)
        self.assertEqual(pending_tasks[0].description, "Pending task")
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0].description, "Completed task")
        self.assertEqual(len(all_tasks), 2)

if __name__ == "__main__":
    unittest.main()
