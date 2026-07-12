import pytest
from fastapi.testclient import TestClient
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"
    assert r.json()["service"] == "catalog"

def test_ready():
    r = client.get("/ready")
    assert r.status_code == 200

def test_list_products():
    r = client.get("/products")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) > 0

def test_get_product():
    r = client.get("/products/P001")
    assert r.status_code == 200
    assert r.json()["id"] == "P001"

def test_product_not_found():
    r = client.get("/products/NOTEXIST")
    assert r.status_code == 404

def test_create_product():
    r = client.post("/products", json={
        "id": "T999", "name": "Test", "description": "Test product",
        "price": 9.99, "category": "test", "stock": 10
    })
    assert r.status_code == 201
    assert r.json()["id"] == "T999"
