import uuid

class Task:
    def __init__(self, title, description, due_date, priority, completed=False, task_id=None):
        self.id = task_id if task_id is not None else str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }
