from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from .models import Note, NoteIn
from .storage import InMemoryStore
from .db import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="CloudNotes", lifespan=lifespan)

store = InMemoryStore()

# Serve static GUI assets
STATIC_DIR = Path(__file__).parent / "gui"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/notes", response_model=list[Note])
def list_notes():
    return store.list()

@app.post("/notes", response_model=Note, status_code=201)
def create_note(note: NoteIn):
    return store.create(note)

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    note = store.get(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Not found")
    return note

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    if not store.delete(note_id):
        raise HTTPException(status_code=404, detail="Not found")

# Serve the GUI
@app.get("/", response_class=FileResponse)
def ui():
    return FileResponse(STATIC_DIR / "index.html")

@app.post("/ui/new")
def ui_create_note(title: str = Form(...), body: str = Form(...)):
    store.create(NoteIn(title=title, body=body))
    return RedirectResponse(url="/", status_code=303)
