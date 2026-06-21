import json
from task_precise import TaskPrecise, Task
import pytest

def test_register():
    task_precise = TaskPrecise()
    email = "test@example.com"
    api_key = task_precise.register(email)
    assert api_key == "api-key-" + email

def test_register_duplicate():
    task_precise = TaskPrecise()
    email = "test@example.com"
    task_precise.register(email)
    api_key = task_precise.register(email)
    assert api_key == "api-key-" + email

def test_run_valid_file():
    task_precise = TaskPrecise()
    task_data = {"name": "Test Task", "description": "Test task description"}
    with open("test_task.json", "w") as file:
        json.dump(task_data, file)
    result = task_precise.run("test_task.json")
    assert result == {"task": "Test Task", "status": "success"}

def test_run_invalid_file():
    task_precise = TaskPrecise()
    result = task_precise.run("non_existent_file.json")
    assert result == {"error": "File not found"}

def test_run_invalid_json():
    task_precise = TaskPrecise()
    with open("test_task.json", "w") as file:
        file.write("Invalid JSON")
    result = task_precise.run("test_task.json")
    assert result == {"error": "Invalid JSON"}

def test_task_creation():
    task = Task("Test Task", "Test task description")
    assert task.name == "Test Task"
    assert task.description == "Test task description"
