from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)


def test_get_joke():
    response = client.get("/api/v1/jokes")
    assert response.status_code == 200

def test_get_joke_chuck():
    response = client.get("/api/v1/jokes/Chuck")
    assert response.status_code == 200

def test_get_joke_dad():
    response = client.get("/api/v1/jokes/Dad")
    assert response.status_code == 200

def test_get_lcm():
    response = client.get("/api/v1/maths/lcm?numbers=2,3,4")
    assert response.text == "12"
    assert response.status_code == 200

def test_get_number_plus_one():
    response = client.get("/api/v1/maths/number-plus-one?number=2")
    assert response.text == "3"
    assert response.status_code == 200
