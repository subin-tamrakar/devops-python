from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Calculator API"}

def test_add():
    response = client.get("/add?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 15.0}

def test_sub():
    response = client.get("/sub?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_mul():
    response = client.get("/mul?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 50.0}

def test_div():
    response = client.get("/div?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}

def test_div_by_zero():
    response = client.get("/div?a=10&b=0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero"}
