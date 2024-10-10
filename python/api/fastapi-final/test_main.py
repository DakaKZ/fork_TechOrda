import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sum1n():
    response = client.get("/sum1n/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

def test_fibo():
    response = client.get("/fibo?n=5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_reverse():
    response = client.post("/reverse", headers={"string": "hello"})
    assert response.status_code == 200
    assert response.json() == {"result": "olleh"}

def test_add_to_list():
    response = client.put("/list", json={"element": "Apple"})
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple"]}

def test_get_list():
    response = client.get("/list")
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple"]}

def test_calculator_valid():
    response = client.post("/calculator", json={"expr": "1,+,1"})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_calculator_invalid():
    response = client.post("/calculator", json={"expr": "1,invalid,1"})
    assert response.status_code == 400
