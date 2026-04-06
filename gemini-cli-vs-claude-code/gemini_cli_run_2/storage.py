import json
import os

class StorageHandler:
    def __init__(self, file_path='tasks.json'):
        self.file_path = file_path

    def load_tasks(self):
        """Load tasks from a JSON file. Returns an empty list if file doesn't exist."""
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            # Return empty list if the file is corrupted or can't be read.
            return []

    def save_tasks(self, tasks):
        """Save a list of tasks to a JSON file."""
        try:
            with open(self.file_path, 'w') as f:
                json.dump(tasks, f, indent=4)
        except IOError as e:
            print(f"Error saving tasks: {e}")
