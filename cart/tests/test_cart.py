import pytest
from fastapi.testclient import TestClient
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["service"] == "cart"

def test_ready():
    r = client.get("/ready")
    assert r.status_code == 200

def test_create_cart():
    r = client.post("/carts", params={"customer_id": "user123"})
    assert r.status_code == 201
    data = r.json()
    assert "cart_id" in data
    assert data["customer_id"] == "user123"
    assert data["items"] == []

def test_get_cart():
    create = client.post("/carts", params={"customer_id": "user456"})
    cart_id = create.json()["cart_id"]
    r = client.get(f"/carts/{cart_id}")
    assert r.status_code == 200
    assert r.json()["cart_id"] == cart_id

def test_add_item():
    create = client.post("/carts", params={"customer_id": "user789"})
    cart_id = create.json()["cart_id"]
    r = client.post(f"/carts/{cart_id}/items", json={
        "product_id": "P001", "quantity": 2, "unit_price": 24.99
    })
    assert r.status_code == 200
    assert len(r.json()["items"]) == 1

def test_cart_not_found():
    r = client.get("/carts/nonexistent-id")
    assert r.status_code == 404
