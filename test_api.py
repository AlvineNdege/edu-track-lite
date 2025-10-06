import pytest # pyright: ignore[reportMissingImports]
from fastapi.testclient import TestClient # pyright: ignore[reportMissingImports]
from main import app # pyright: ignore[reportAttributeAccessIssue]
from datetime import date

client = TestClient(app)


def test_crud_user_and_course_and_enroll_flow():
    # create user
    resp = client.post("/users/", json={"name": "Alice", "email": "alice@example.com"})
    assert resp.status_code == 201
    u = resp.json()
    assert u["name"] == "Alice"
    user_id = u["id"]

    # create course
    resp = client.post("/courses/", json={"title": "Python Basics", "description": "Learn Python"})
    assert resp.status_code == 201
    c = resp.json()
    assert c["title"] == "Python Basics"
    course_id = c["id"]

    # enroll
    resp = client.post("/enrollments/", json={"user_id": user_id, "course_id": course_id})
    assert resp.status_code == 201
    e = resp.json()
    assert e["user_id"] == user_id
    enrollment_id = e["id"]

    # mark complete
    resp = client.post(f"/enrollments/{enrollment_id}/complete")
    assert resp.status_code == 200
    e2 = resp.json()
    assert e2["completed"] is True

    # view enrollments for user
    resp = client.get(f"/enrollments/user/{user_id}")
    assert resp.status_code == 200
    arr = resp.json()
    assert isinstance(arr, list)
    assert any(en["id"] == enrollment_id for en in arr)

    # close course
    resp = client.post(f"/courses/{course_id}/close")
    assert resp.status_code == 200
    c2 = resp.json()
    assert c2["is_open"] is False

    # attempting to enroll again should fail
    resp = client.post("/users/", json={"name": "Bob", "email": "bob@example.com"})
    user2 = resp.json()
    resp = client.post("/enrollments/", json={"user_id": user2["id"], "course_id": course_id})
    assert resp.status_code == 400