from storage import StorageHandler

class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['description'], data['completed'])

class TodoManager:
    def __init__(self, storage=None):
        self.storage = storage or StorageHandler()
        self.tasks = [Task.from_dict(t) for t in self.storage.load_tasks()]

    def add_task(self, description):
        """Add a new task with a unique ID."""
        new_id = 1 if not self.tasks else max(t.id for t in self.tasks) + 1
        new_task = Task(new_id, description)
        self.tasks.append(new_task)
        self.save()
        return new_task

    def list_tasks(self, filter_type='all'):
        """Return tasks based on filter: 'all', 'completed', or 'pending'."""
        if filter_type == 'completed':
            return [t for t in self.tasks if t.completed]
        elif filter_type == 'pending':
            return [t for t in self.tasks if not t.completed]
        return self.tasks

    def mark_completed(self, task_id):
        """Mark a task as completed by ID. Returns True if task exists, else False."""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self.save()
                return True
        return False

    def delete_task(self, task_id):
        """Delete a task by ID. Returns True if deleted, else False."""
        initial_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        if len(self.tasks) < initial_len:
            self.save()
            return True
        return False

    def save(self):
        """Persist current tasks to storage."""
        self.storage.save_tasks([t.to_dict() for t in self.tasks])
