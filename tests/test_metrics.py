import pytest
from src.metrics import MetricsExporter, GrafanaDashboard, TaskMetrics

def test_update_metrics():
    exporter = MetricsExporter()
    exporter.update_metrics("customer1", "task1", 10, 5, 0.5)
    assert len(exporter.metrics) == 1
    assert exporter.metrics[("customer1", "task1")].tasks_total == 10
    assert exporter.metrics[("customer1", "task1")].tasks_verified == 5
    assert exporter.metrics[("customer1", "task1")].verification_pass_rate == 0.5

def test_export_metrics():
    exporter = MetricsExporter()
    exporter.update_metrics("customer1", "task1", 10, 5, 0.5)
    metrics_dict = exporter.export_metrics()
    assert metrics_dict[f"tasks_total_customer1_task1"] == 10
    assert metrics_dict[f"tasks_verified_customer1_task1"] == 5
    assert metrics_dict[f"verification_pass_rate_customer1_task1"] == 0.5

def test_get_prometheus_metrics():
    exporter = MetricsExporter()
    exporter.update_metrics("customer1", "task1", 10, 5, 0.5)
    prometheus_metrics = exporter.get_prometheus_metrics()
    assert "tasks_total_customer1_task1 10" in prometheus_metrics
    assert "tasks_verified_customer1_task1 5" in prometheus_metrics
    assert "verification_pass_rate_customer1_task1 0.5" in prometheus_metrics

def test_grafana_dashboard():
    dashboard = GrafanaDashboard()
    dashboard.add_panel("Tasks Total", "tasks_total_customer1_task1")
    dashboard_config = dashboard.get_dashboard_config()
    assert len(dashboard_config["rows"]) == 1
    assert dashboard_config["rows"][0]["title"] == "Tasks Total"
    assert dashboard_config["rows"][0]["panels"][0]["title"] == "Tasks Total"

def test_get_dashboard_json():
    dashboard = GrafanaDashboard()
    dashboard.add_panel("Tasks Total", "tasks_total_customer1_task1")
    dashboard_json = dashboard.get_dashboard_json()
    assert "Tasks Total" in dashboard_json
    assert "tasks_total_customer1_task1" in dashboard_json
