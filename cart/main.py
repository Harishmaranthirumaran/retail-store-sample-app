"""
Cart Service — Shopping cart management API.

Author: Harishmaran Subbaiah Thirumaran
GitHub: github.com/Harishmaranthirumaran
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
import uuid

app = FastAPI(
    title="Cart Service",
    description="Shopping cart API for the retail platform",
    version="1.0.0",
)

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
CATALOG_URL = os.getenv("CATALOG_URL", "http://catalog:8080")


class CartItem(BaseModel):
    product_id: str
    quantity: int
    unit_price: float


class Cart(BaseModel):
    cart_id: str
    customer_id: str
    items: List[CartItem] = []

    @property
    def total(self) -> float:
        return sum(item.unit_price * item.quantity for item in self.items)


class AddItemRequest(BaseModel):
    product_id: str
    quantity: int
    unit_price: float


# In-memory cart store
CARTS: dict[str, Cart] = {}


@app.get("/health")
def health():
    return {"status": "healthy", "service": "cart", "environment": ENVIRONMENT}


@app.get("/ready")
def ready():
    return {"status": "ready"}


@app.post("/carts", response_model=Cart, status_code=201)
def create_cart(customer_id: str):
    cart_id = str(uuid.uuid4())
    cart = Cart(cart_id=cart_id, customer_id=customer_id)
    CARTS[cart_id] = cart
    return cart


@app.get("/carts/{cart_id}", response_model=Cart)
def get_cart(cart_id: str):
    if cart_id not in CARTS:
        raise HTTPException(status_code=404, detail="Cart not found")
    return CARTS[cart_id]


@app.post("/carts/{cart_id}/items", response_model=Cart)
def add_item(cart_id: str, item: AddItemRequest):
    if cart_id not in CARTS:
        raise HTTPException(status_code=404, detail="Cart not found")
    cart = CARTS[cart_id]
    existing = next((i for i in cart.items if i.product_id == item.product_id), None)
    if existing:
        existing.quantity += item.quantity
    else:
        cart.items.append(CartItem(
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=item.unit_price
        ))
    return cart


@app.delete("/carts/{cart_id}/items/{product_id}", response_model=Cart)
def remove_item(cart_id: str, product_id: str):
    if cart_id not in CARTS:
        raise HTTPException(status_code=404, detail="Cart not found")
    cart = CARTS[cart_id]
    cart.items = [i for i in cart.items if i.product_id != product_id]
    return cart
