from fastapi import FastAPI, HTTPException
from .models import Note, NoteIn
from .storage import InMemoryStore

app = FastAPI(title="CloudNotes")
store = InMemoryStore()

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
