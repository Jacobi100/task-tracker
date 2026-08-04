import json
import os
import sys
from datetime import datetime

from storage import load_tasks save_tasks

TASK_FILE = "tasks.json"
VALID_STATUSES = {"todo", "in-progress", "done"}


def get_next_id(tasks):
    """Get the next unique task ID."""
    if not tasks:
        return 1
    return max(task.get("id", 0) for task in tasks) + 1


def add_task(description):
    """Add a new task with the default status 'todo'."""
    if not description.strip():
        print("Error: Description cannot be empty.")
        return

    tasks = load_tasks()
    now = datetime.now().isoformat()
    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")


def update_task(task_id, description):
    """Update the description of an existing task."""
    if not description.strip():
        print("Error: Description cannot be empty.")
        return

    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Error: Task with ID {task_id} not found.")


def delete_task(task_id):
    """Remove a task from the list by ID."""
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task["id"] != task_id]

    if len(filtered_tasks) == len(tasks):
        print(f"Error: Task with ID {task_id} not found.")
        return

    save_tasks(filtered_tasks)
    print(f"Task {task_id} deleted successfully.")


def change_status(task_id, status):
    """Change a task's status to a valid value."""
    if status not in VALID_STATUSES:
        print("Error: Invalid status. Use todo, in-progress, or done.")
        return

    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return

    print(f"Error: Task with ID {task_id} not found.")


def list_tasks(status_filter=None):
    """Display tasks, optionally filtered by status."""
    tasks = load_tasks()

    if status_filter:
        if status_filter not in VALID_STATUSES:
            print("Error: Invalid status filter. Use todo, in-progress, or done.")
            return
        tasks = [task for task in tasks if task["status"] == status_filter]

    if not tasks:
        print("No tasks found.")
        return

    print(f"{'ID':<5} | {'Status':<12} | {'Description'}")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:<5} | {task['status']:<12} | {task['description']}")




