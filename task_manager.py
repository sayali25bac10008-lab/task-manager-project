from task import Task
from storage import load_tasks, save_tasks

class TaskManager:

    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title, description, due_date, priority):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task.to_dict())
        save_tasks(self.tasks)
        print("\nTask added successfully!\n")

    def view_all_tasks(self):
        if not self.tasks:
            print("\nNo tasks found!\n")
            return
        for task in self.tasks:
            self.display_task(task)

    def view_pending_tasks(self):
        pending = [t for t in self.tasks if not t["completed"]]
        if not pending:
            print("\nNo pending tasks.\n")
            return
        for task in pending:
            self.display_task(task)

    def view_completed_tasks(self):
        completed = [t for t in self.tasks if t["completed"]]
        if not completed:
            print("\nNo completed tasks.\n")
            return
        for task in completed:
            self.display_task(task)

    def view_by_priority(self, priority):
        filtered = [t for t in self.tasks if t["priority"].lower() == priority.lower()]
        if not filtered:
            print("\nNo tasks with this priority.\n")
            return
        for task in filtered:
            self.display_task(task)

    def edit_task(self, task_id, title=None, description=None, due_date=None, priority=None):
        for task in self.tasks:
            if task["id"] == task_id:
                if title: task["title"] = title
                if description: task["description"] = description
                if due_date: task["due_date"] = due_date
                if priority: task["priority"] = priority
                save_tasks(self.tasks)
                print("\nTask updated successfully!\n")
                return
        print("\nTask not found.\n")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                save_tasks(self.tasks)
                print("\nTask deleted successfully!\n")
                return
        print("\nTask not found.\n")

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks(self.tasks)
                print("\nTask marked as completed!\n")
                return
        print("\nTask not found.\n")

    def display_task(self, task):
        print(f"""
ID: {task['id']}
Title: {task['title']}
Description: {task['description']}
Due Date: {task['due_date']}
Priority: {task['priority']}
Completed: {"Yes" if task['completed'] else "No"}
----------------------------------------
        """)
