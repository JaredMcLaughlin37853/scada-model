# SCADA Design Assistant

This repository hosts a prototype web tool that helps **SCADA engineers** generate design‑check checklists from a JSON‑based impact model.

* **Backend:** FastAPI + Pydantic  
* **Model validation:** JSON‑Schema  
* **Outputs:** Deterministic checklist JSON that can be archived or imported into other systems.

## Prerequisites
Git 2.43 +
Python 3.12.3 +
Poetry 2.1.2 +
VS Code + Python extension

Update %PATH% extensions

## Clone Repo
git clone https://github.com/JaredMcLaughlin37853/scada-model.git
cd scada-model

## Install dependencies
poetry install --with dev
poetry check #check install

## Daily Workflow (assuming WSL evironment)
wsl ~
cd ~/projects/scada-model
git pull               # keep up‑to‑date
code .                 # start coding

The interactive OpenAPI docs will be available at `http://localhost:8000/docs`.