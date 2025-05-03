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

## Ubuntu distro and install steps (you'll have to follow slightly different steps if running in a Windows env)
**from the powershell**
`wsl ~`

**from the ubuntu CLI**
```
sudo apt update && sudo apt upgrade -y  
sudo apt install build-essential python3 python3-venv python3-pip git
```  

**clone repo**
```
mkdir projects # create a directory to store your projects if you don't have one created yet  
cd projects
git clone https://github.com/JaredMcLaughlin37853/scada-model.git  
cd scada-model  
```

**install poetry**
```
curl -sSL https://install.python-poetry.org | python3 - --version 2.1.2  
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc  
source ~/.bashrc  
poetry install --with dev      # creates .venv/ (or ~/.cache/pypoetry/… depending on config) 
``` 


## Daily Workflow (assuming WSL evironment)
```
wsl ~  
cd ~/projects/scada-model  
git pull               # keep up‑to‑date  
code .                 # start coding  
```

The interactive OpenAPI docs will be available at `http://localhost:8000/docs`.