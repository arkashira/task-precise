import argparse
import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Task:
    name: str
    description: str

class TaskPrecise:
    def __init__(self):
        self.tenants = {}
        self.api_keys = {}

    def register(self, email: str) -> str:
        if email not in self.tenants:
            self.tenants[email] = TaskPrecise()
            self.api_keys[email] = "api-key-" + email
        return self.api_keys[email]

    def run(self, file_path: str) -> Dict:
        try:
            with open(file_path, 'r') as file:
                task_data = json.load(file)
                task = Task(task_data['name'], task_data['description'])
                # Simulate task execution
                return {"task": task.name, "status": "success"}
        except FileNotFoundError:
            return {"error": "File not found"}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON"}

def main():
    parser = argparse.ArgumentParser(description='Task Precise CLI')
    subparsers = parser.add_subparsers(dest='command')

    register_parser = subparsers.add_parser('register')
    register_parser.add_argument('--email', required=True)

    run_parser = subparsers.add_parser('run')
    run_parser.add_argument('--file', required=True)

    args = parser.parse_args()

    task_precise = TaskPrecise()

    if args.command == 'register':
        api_key = task_precise.register(args.email)
        print(api_key)
    elif args.command == 'run':
        result = task_precise.run(args.file)
        print(json.dumps(result))

if __name__ == '__main__':
    main()
