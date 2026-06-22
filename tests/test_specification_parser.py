import json
from specification_parser import SpecificationParser, TaskSpecification, parse_specification
import pytest

def test_validate_complete_specification():
    spec = {
        'name': 'Test Task',
        'description': 'This is a test task',
        'variables': {
            'var1': 'value1',
            'var2': 'value2'
        }
    }
    parser = SpecificationParser(spec)
    result = parser.validate()
    assert result == {'errors': []}

def test_validate_missing_required_fields():
    spec = {
        'description': 'This is a test task',
        'variables': {
            'var1': 'value1',
            'var2': 'value2'
        }
    }
    parser = SpecificationParser(spec)
    result = parser.validate()
    assert result == {'errors': [{'field': 'name', 'message': 'Missing required field'}]}

def test_validate_ambiguous_variable_names():
    spec = {
        'name': 'Test Task',
        'description': 'This is a test task',
        'variables': {
            '': 'value1',
            'var2': 'value2'
        }
    }
    parser = SpecificationParser(spec)
    result = parser.validate()
    assert result == {'errors': [{'field': 'variables.', 'message': 'Ambiguous variable name or value'}]}

def test_parse_specification():
    spec = {
        'name': 'Test Task',
        'description': 'This is a test task',
        'variables': {
            'var1': 'value1',
            'var2': 'value2'
        }
    }
    task_spec = parse_specification(spec)
    assert task_spec.name == 'Test Task'
    assert task_spec.description == 'This is a test task'
    assert task_spec.variables == {'var1': 'value1', 'var2': 'value2'}
