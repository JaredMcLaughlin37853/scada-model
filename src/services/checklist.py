import json
from pathlib import Path
from datetime import datetime
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT / "models" / "scada_model_json.json"

with MODEL_PATH.open() as f:
    _MODEL = json.load(f)

def _flatten_equipment(payload):
    if isinstance(payload, dict) and 'equipment' in payload:
        return {item['id'] for item in payload['equipment']}
    return set()

def generate_checklist(payload: dict):
    equipment_present = _flatten_equipment(payload)
    checklist_items = []
    for rule in _MODEL.get("rules", []):
        triggers = rule.get("trigger", {}).get("if_equipment_present", [])
        if any(t in equipment_present for t in triggers):
            checklist_items.extend(rule.get("checklist_outputs", []))
    return {
        "metadata": {
            "id": str(uuid4()),
            "generated": datetime.utcnow().isoformat() + "Z",
            "model_version": _MODEL["metadata"]["version"],
        },
        "items": [{"text": item, "status": "pending"} for item in checklist_items],
    }