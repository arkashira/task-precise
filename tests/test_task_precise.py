import json
import hashlib
from task_precise import TaskDescription, generate_code, compile_task

def test_generate_code():
    task_description = TaskDescription(
        task_id="test_task",
        description="This is a test task.",
        inputs_schema={"input1": "str", "input2": "int"}
    )
    generated_code = generate_code(task_description)
    expected_code = """
def execute_test_task(input1, input2):
    # Task logic based on the description
    result = "This is a test task."
    return result
"""
    assert generated_code.strip() == expected_code.strip()

def test_compile_task():
    task_json = {
        "task_id": "test_task",
        "description": "This is a test task.",
        "inputs_schema": {"input1": "str", "input2": "int"}
    }
    result = compile_task(task_json)
    expected_code = """
def execute_test_task(input1, input2):
    # Task logic based on the description
    result = "This is a test task."
    return result
"""
    expected_sha256 = hashlib.sha256(expected_code.strip().encode()).hexdigest()
    assert result["sha256"] == expected_sha256
    assert "artifact" in result
    assert "logs" in result

def test_main():
    import sys
    from io import StringIO
    from unittest.mock import patch
    test_input = json.dumps({
        "task_id": "test_task",
        "description": "This is a test task.",
        "inputs_schema": {"input1": "str", "input2": "int"}
    })
    expected_code = """
def execute_test_task(input1, input2):
    # Task logic based on the description
    result = "This is a test task."
    return result
"""
    expected_sha256 = hashlib.sha256(expected_code.strip().encode()).hexdigest()
    expected_output = json.dumps({
        "artifact": expected_code.strip(),
        "sha256": expected_sha256,
        "logs": "Code generated successfully"
    })
    with patch('sys.argv', ['task_precise', test_input]), patch('sys.stdout', new=StringIO()) as fake_out:
        from task_precise import main
        main()
    assert fake_out.getvalue().strip() == expected_output
