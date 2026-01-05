from typing import Dict
from .models import Note, NoteIn

class InMemoryStore:
    def __init__(self):
        self._db: Dict[int, Note] = {}
        self._next_id = 1

    def list(self):
        return list(self._db.values())

    def create(self, data: NoteIn) -> Note:
        note = Note(id=self._next_id, **data.model_dump())
        self._db[note.id] = note
        self._next_id += 1
        return note

    def get(self, note_id: int) -> Note | None:
        return self._db.get(note_id)

    def delete(self, note_id: int) -> bool:
        return self._db.pop(note_id, None) is not None
