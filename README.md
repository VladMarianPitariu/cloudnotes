# CloudNotes

FastAPI-backed notes API with an in-memory store plus a Bootstrap GUI.

## Features
- Health check via [`app.main.health`](app/main.py).
- CRUD for notes: [`app.main.list_notes`](app/main.py), [`app.main.create_note`](app/main.py), [`app.main.get_note`](app/main.py), [`app.main.delete_note`](app/main.py).
- Static GUI served from [app/gui/index.html](app/gui/index.html) with assets [app/gui/main.js](app/gui/main.js) and [app/gui/styles.css](app/gui/styles.css).

## Running locally
````bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
`````
or via 
````bash
docker compose up -build
````
