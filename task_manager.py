from datetime import datetime

class Task:
    def __init__(self, title, priority="Medium"):
        self.title = title
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["title"], data["priority"])
        task.completed = data["completed"]
        task.created_at = data["created_at"]
        return task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority):
        task = Task(title, priority)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for i, task in enumerate(self.tasks, 1):
            status = "✔" if task.completed else "✘"
            print(f"{i}. [{status}] {task.title} (Priority: {task.priority})")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
