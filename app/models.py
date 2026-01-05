from pydantic import BaseModel
from typing import Optional

class NoteIn(BaseModel):
    title: str
    body: str

class Note(NoteIn):
    id: int
