import hashlib
import json
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class TaskDescription:
    task_id: str
    description: str
    inputs_schema: Dict[str, Any]

def generate_code(task_description: TaskDescription) -> str:
    code_template = f"""
def execute_{task_description.task_id}({', '.join(task_description.inputs_schema.keys())}):
    # Task logic based on the description
    result = "{task_description.description}"
    return result
"""
    return code_template

def compile_task(task_json: Dict[str, Any]) -> Dict[str, Any]:
    task_description = TaskDescription(**task_json)
    generated_code = generate_code(task_description)
    # Remove leading and trailing whitespace before calculating the hash
    stripped_code = generated_code.strip()
    sha256_hash = hashlib.sha256(stripped_code.encode()).hexdigest()
    execution_logs = "Code generated successfully"
    return {
        "artifact": stripped_code,
        "sha256": sha256_hash,
        "logs": execution_logs
    }

def main():
    import argparse
    import sys
    parser = argparse.ArgumentParser(description="Compile a task description into executable code.")
    parser.add_argument("json_payload", type=str, help="JSON payload containing task description")
    args = parser.parse_args()
    try:
        task_json = json.loads(args.json_payload)
        result = compile_task(task_json)
        print(json.dumps(result))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
