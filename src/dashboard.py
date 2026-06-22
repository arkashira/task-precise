import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class TaskExecution:
    task_id: int
    success: bool
    timestamp: datetime

class Dashboard:
    def __init__(self):
        self.executions = []

    def add_execution(self, task_id: int, success: bool):
        self.executions.append(TaskExecution(task_id, success, datetime.now()))

    def get_metrics(self, start_time: datetime, end_time: datetime):
        total_tasks = 0
        successful_tasks = 0
        for execution in self.executions:
            if start_time <= execution.timestamp <= end_time:
                total_tasks += 1
                if execution.success:
                    successful_tasks += 1
        failure_rate = (total_tasks - successful_tasks) / total_tasks if total_tasks > 0 else 0
        return total_tasks, successful_tasks, failure_rate

    def trigger_alert(self, start_time: datetime, end_time: datetime):
        _, _, failure_rate = self.get_metrics(start_time, end_time)
        if failure_rate > 0.02:
            return True
        return False

    def export_metrics(self, start_time: datetime, end_time: datetime):
        metrics = []
        for execution in self.executions:
            if start_time <= execution.timestamp <= end_time:
                metrics.append({
                    'task_id': execution.task_id,
                    'success': execution.success,
                    'timestamp': execution.timestamp.isoformat()
                })
        return json.dumps(metrics)
