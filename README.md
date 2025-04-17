# SCADA Design Assistant

This repository hosts a prototype web tool that helps **SCADA engineers** generate design‑check checklists from a JSON‑based impact model.

* **Backend:** FastAPI + Pydantic  
* **Model validation:** JSON‑Schema  
* **Outputs:** Deterministic checklist JSON that can be archived or imported into other systems.

## Quick start

```bash
# (inside a virtualenv or poetry shell)
uvicorn src.app.main:app --reload
```

The interactive OpenAPI docs will be available at `http://localhost:8000/docs`.