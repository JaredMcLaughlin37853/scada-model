from fastapi import FastAPI, HTTPException
from src.services.checklist import generate_checklist
from src.services.validation import validate_equipment_list

app = FastAPI(title="SCADA Design Assistant", version="0.1.0")

@app.post("/checklist")
def create_checklist(payload: dict):
    """Validate incoming equipment list and return a SCADA checklist."""
    try:
        validate_equipment_list(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return generate_checklist(payload)