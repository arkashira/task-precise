import pytest
import json
from datetime import datetime, timedelta
from dashboard import Dashboard, TaskExecution

def test_get_metrics():
    dashboard = Dashboard()
    dashboard.add_execution(1, True)
    dashboard.add_execution(2, False)
    start_time = datetime.now() - timedelta(hours=1)
    end_time = datetime.now()
    total_tasks, successful_tasks, failure_rate = dashboard.get_metrics(start_time, end_time)
    assert total_tasks == 2
    assert successful_tasks == 1
    assert failure_rate == 0.5

def test_trigger_alert():
    dashboard = Dashboard()
    dashboard.add_execution(1, True)
    dashboard.add_execution(2, False)
    dashboard.add_execution(3, False)
    start_time = datetime.now() - timedelta(hours=1)
    end_time = datetime.now()
    assert dashboard.trigger_alert(start_time, end_time) == True

def test_export_metrics():
    dashboard = Dashboard()
    dashboard.add_execution(1, True)
    dashboard.add_execution(2, False)
    start_time = datetime.now() - timedelta(hours=1)
    end_time = datetime.now()
    metrics = dashboard.export_metrics(start_time, end_time)
    assert len(json.loads(metrics)) == 2

def test_edge_case_no_executions():
    dashboard = Dashboard()
    start_time = datetime.now() - timedelta(hours=1)
    end_time = datetime.now()
    total_tasks, successful_tasks, failure_rate = dashboard.get_metrics(start_time, end_time)
    assert total_tasks == 0
    assert successful_tasks == 0
    assert failure_rate == 0
