from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products: List[dict] = [
    {"id": 1, "name": "Producto 1", "price": 100},
    {"id": 2, "name": "Producto 2", "price": 200},
    {"id": 3, "name": "Producto 3", "price": 50}
]

cart: List[dict] = []

class CartItem(BaseModel):
    product_id: int

class NewProduct(BaseModel):
    name: str
    price: float

@app.get("/productos")
def get_products():
    return products

@app.post("/productos")
def create_product(item: NewProduct):
    new_id = max(p["id"] for p in products) + 1 if products else 1
    product = {"id": new_id, "name": item.name, "price": item.price}
    products.append(product)
    return {"message": "Producto creado", "product": product}

@app.post("/carrito")
def add_to_cart(item: CartItem):
    product = next((p for p in products if p["id"] == item.product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    existing = next((c for c in cart if c["id"] == item.product_id), None)
    if existing:
        existing["quantity"] += 1
    else:
        cart.append({**product, "quantity": 1})
    
    return {"message": "Producto agregado", "cart": cart}

@app.get("/carrito")
def get_cart():
    return {"cart": cart}

@app.delete("/carrito/{product_id}")
def remove_from_cart(product_id: int, all: bool = False):
    existing = next((c for c in cart if c["id"] == product_id), None)
    if not existing:
        raise HTTPException(status_code=404, detail="Producto no encontrado en carrito")
    
    if all or existing["quantity"] == 1:
        cart.remove(existing)
    else:
        existing["quantity"] -= 1
    
    return {"message": "Producto eliminado", "cart": cart}
