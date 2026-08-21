import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_tasks(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json == []


def test_create_task(client):
    response = client.post(
        "/tasks",
        json={"title": "Learn CI/CD"}
    )

    assert response.status_code == 200
    assert response.json["title"] == "Learn CI/CD"
    assert response.json["done"] is False