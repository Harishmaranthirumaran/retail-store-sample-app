"""
Catalog Service — Product inventory API.

Author: Harishmaran Subbaiah Thirumaran
GitHub: github.com/Harishmaranthirumaran
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI(
    title="Catalog Service",
    description="Product catalog API for the retail platform",
    version="1.0.0",
)

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    category: str
    stock: int
    image_url: Optional[str] = None


# In-memory product store (replace with RDS/DynamoDB in production)
PRODUCTS: dict[str, Product] = {
    "P001": Product(id="P001", name="Cloud T-Shirt",    description="Comfortable DevOps tee", price=24.99, category="apparel",     stock=150),
    "P002": Product(id="P002", name="Terraform Hoodie", description="Stay warm with IaC",      price=49.99, category="apparel",     stock=80),
    "P003": Product(id="P003", name="K8s Mug",          description="Ships on Kubernetes",     price=12.99, category="accessories", stock=200),
    "P004": Product(id="P004", name="SRE Handbook",     description="Site reliability guide",  price=34.99, category="books",      stock=60),
    "P005": Product(id="P005", name="Docker Sticker",   description="For your laptop",         price=4.99,  category="accessories", stock=500),
}


@app.get("/health")
def health():
    return {"status": "healthy", "service": "catalog", "environment": ENVIRONMENT}


@app.get("/ready")
def ready():
    return {"status": "ready"}


@app.get("/products", response_model=List[Product])
def list_products(category: Optional[str] = None):
    products = list(PRODUCTS.values())
    if category:
        products = [p for p in products if p.category == category]
    return products


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    if product_id not in PRODUCTS:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    return PRODUCTS[product_id]


@app.post("/products", response_model=Product, status_code=201)
def create_product(product: Product):
    if product.id in PRODUCTS:
        raise HTTPException(status_code=409, detail="Product already exists")
    PRODUCTS[product.id] = product
    return product
