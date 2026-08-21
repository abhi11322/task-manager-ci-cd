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

    assert response.status_code == 201
    assert response.json["title"] == "Learn CI/CD"
    assert response.json["done"] is False

def test_create_task_without_title(client):
    response = client.post(
        "/tasks",
        json={"description": "This should fail"}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Title is required"

def test_complete_task(client):
    create_response = client.post(
        "/tasks",
        json={"title": "Learn CI/CD"}
    )

    task_id = create_response.json["id"]

    response = client.put(
        f"/tasks/{task_id}/complete"
    )

    assert response.status_code == 200
    assert response.json["done"] is True

def test_delete_task(client):
    create_response = client.post(
        "/tasks",
        json={"title": "Task to delete"}
    )

    task_id = create_response.json["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json["message"] == "Task deleted"
    
def test_delete_nonexistent_task(client):
    response = client.delete("/tasks/999")

    assert response.status_code == 404
    assert response.json["error"] == "Task not found"