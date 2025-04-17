import json
from pathlib import Path
from jsonschema import Draft7Validator

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "models" / "scada-model.schema.json"
with SCHEMA_PATH.open() as f:
    _schema = json.load(f)
_validator = Draft7Validator(_schema)

def validate_equipment_list(data: dict):
    errors = sorted(_validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        message = "\n".join(f"{'/'.join(map(str, err.path))}: {err.message}" for err in errors)
        raise ValueError(message)
    return True