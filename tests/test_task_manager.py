import pytest
from src.task_manager import TaskManager, TaskSpec

def test_create_task():
    task_manager = TaskManager()
    spec = TaskSpec("test_task", "This is a test task")
    task = task_manager.create_task(spec)
    assert task.name == "test_task"
    assert task.description == "This is a test task"

def test_get_task():
    task_manager = TaskManager()
    spec = TaskSpec("test_task", "This is a test task")
    task_manager.create_task(spec)
    task = task_manager.get_task("test_task")
    assert task.name == "test_task"
    assert task.description == "This is a test task"

def test_create_task_duplicate_name():
    task_manager = TaskManager()
    spec = TaskSpec("test_task", "This is a test task")
    task_manager.create_task(spec)
    with pytest.raises(ValueError):
        task_manager.create_task(spec)

def test_get_task_not_found():
    task_manager = TaskManager()
    task = task_manager.get_task("non_existent_task")
    assert task is None
