import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class TaskSpecification:
    name: str
    description: str
    variables: Dict[str, str]

class SpecificationParser:
    def __init__(self, spec: Dict):
        self.spec = spec

    def validate(self) -> Dict:
        errors = []
        if 'name' not in self.spec:
            errors.append({'field': 'name', 'message': 'Missing required field'})
        if 'description' not in self.spec:
            errors.append({'field': 'description', 'message': 'Missing required field'})
        if 'variables' not in self.spec:
            errors.append({'field': 'variables', 'message': 'Missing required field'})
        for variable, value in self.spec.get('variables', {}).items():
            if not variable or not value:
                errors.append({'field': f'variables.{variable}', 'message': 'Ambiguous variable name or value'})
        return {'errors': errors}

def parse_specification(spec: Dict) -> TaskSpecification:
    return TaskSpecification(
        name=spec['name'],
        description=spec['description'],
        variables=spec['variables']
    )
