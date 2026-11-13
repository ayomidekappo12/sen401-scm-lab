"""End-to-end tests: migrate into a temporary DB, then call every endpoint."""
import pytest
from fastapi.testclient import TestClient


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("DB_PATH", str(tmp_path / "test.db"))
    from migrations import migrate
    migrate.main()
    from app.main import app
    with TestClient(app) as c:
        yield c


def test_health(client):
    assert client.get("/").json()["status"] == "ok"


def test_students_migrated_and_stats(client):
    assert len(client.get("/students").json()) == 5
    stats = client.get("/students/stats").json()
    assert stats["average"] == 71.8 and stats["highest"] == "Amaka"


def test_create_and_delete_student(client):
    new = client.post("/students", json={"name": "Zainab", "score": 88}).json()
    assert client.get(f"/students/{new['id']}").status_code == 200
    assert client.delete(f"/students/{new['id']}").status_code == 204
    assert client.get(f"/students/{new['id']}").status_code == 404


def test_invalid_student_rejected(client):
    assert client.post("/students", json={"name": "X", "score": 150}).status_code == 422


def test_items_value_and_low_stock(client):
    assert client.get("/items/stats").json()["total"] == 3_610_000
    low = [i["item_name"] for i in client.get("/items/low-stock").json()]
    assert low == ["Laptop", "Monitor", "USB Cable"]


def test_update_quantity_and_duplicate(client):
    assert client.patch("/items/5/quantity", params={"quantity": 30}).json()["value"] == 75000
    dup = {"item_name": "Mouse", "quantity": 1, "price": 1}
    assert client.post("/items", json=dup).status_code == 409
