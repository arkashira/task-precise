import json
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from socketserver import ThreadingMixIn

@dataclass
class TaskSpec:
    name: str
    description: str

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def create_task(self, spec):
        if spec.name in self.tasks:
            raise ValueError("Task with this name already exists")
        self.tasks[spec.name] = spec
        return spec

    def get_task(self, name):
        return self.tasks.get(name)

class RequestHandler(BaseHTTPRequestHandler):
    task_manager = TaskManager()

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
            <html>
                <body>
                    <h1>Task Manager</h1>
                    <form action="/create_task" method="post">
                        <label for="name">Name:</label>
                        <input type="text" id="name" name="name"><br><br>
                        <label for="description">Description:</label>
                        <input type="text" id="description" name="description"><br><br>
                        <input type="submit" value="Create Task">
                    </form>
                </body>
            </html>
            """)
        elif self.path.startswith("/task/"):
            name = self.path.split("/")[-1]
            task = self.task_manager.get_task(name)
            if task:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f"Task {task.name}: {task.description}".encode())
            else:
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Task not found")

    def do_POST(self):
        if self.path == "/create_task":
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            data = parse_qs(body.decode())
            name = data.get("name", [None])[0]
            description = data.get("description", [None])[0]
            if name and description:
                try:
                    spec = TaskSpec(name, description)
                    self.task_manager.create_task(spec)
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(f"Task {name} created".encode())
                except ValueError as e:
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(str(e).encode())
            else:
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Invalid request")

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def run_server():
    server_address = ("", 8000)
    httpd = ThreadedHTTPServer(server_address, RequestHandler)
    print("Server running on port 8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
