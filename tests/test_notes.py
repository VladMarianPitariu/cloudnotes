from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_note():
    payload = {"title": "hello", "body": "world"}
    r = client.post("/notes", json=payload)
    assert r.status_code == 201
    note = r.json()
    assert note["id"] == 1
    assert note["title"] == "hello"

    r2 = client.get("/notes/1")
    assert r2.status_code == 200
    assert r2.json()["body"] == "world"

def test_list_and_delete():
    client.post("/notes", json={"title": "a", "body": "b"})
    r = client.get("/notes")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) >= 1

    r2 = client.delete("/notes/1")
    assert r2.status_code == 204

    r3 = client.get("/notes/1")
    assert r3.status_code == 404
