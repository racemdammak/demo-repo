import json
import os
from task_manager import Task

FILE_NAME = "tasks.json"

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        data = json.load(f)
        return [Task.from_dict(task) for task in data]
