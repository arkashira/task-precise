import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class TaskMetrics:
    customer_id: str
    task_type: str
    tasks_total: int
    tasks_verified: int
    verification_pass_rate: float

class MetricsExporter:
    def __init__(self):
        self.metrics = {}

    def update_metrics(self, customer_id: str, task_type: str, tasks_total: int, tasks_verified: int, verification_pass_rate: float):
        self.metrics[(customer_id, task_type)] = TaskMetrics(customer_id, task_type, tasks_total, tasks_verified, verification_pass_rate)

    def export_metrics(self) -> Dict:
        metrics_dict = {}
        for key, metric in self.metrics.items():
            metrics_dict[f"tasks_total_{key[0]}_{key[1]}"] = metric.tasks_total
            metrics_dict[f"tasks_verified_{key[0]}_{key[1]}"] = metric.tasks_verified
            metrics_dict[f"verification_pass_rate_{key[0]}_{key[1]}"] = metric.verification_pass_rate
        return metrics_dict

    def get_prometheus_metrics(self) -> str:
        metrics_dict = self.export_metrics()
        prometheus_metrics = ""
        for key, value in metrics_dict.items():
            prometheus_metrics += f"{key} {value}\n"
        return prometheus_metrics

class GrafanaDashboard:
    def __init__(self):
        self.panels = []

    def add_panel(self, title: str, metric: str):
        self.panels.append((title, metric))

    def get_dashboard_config(self) -> Dict:
        dashboard_config = {
            "rows": []
        }
        for panel in self.panels:
            row = {
                "title": panel[0],
                "panels": [
                    {
                        "id": 1,
                        "title": panel[0],
                        "type": "graph",
                        "span": 12,
                        "targets": [
                            {
                                "expr": panel[1],
                                "legendFormat": "{{job}}",
                                "refId": "A"
                            }
                        ]
                    }
                ]
            }
            dashboard_config["rows"].append(row)
        return dashboard_config

    def get_dashboard_json(self) -> str:
        dashboard_config = self.get_dashboard_config()
        return json.dumps(dashboard_config)
