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

products = [
    {"id": 1, "name": "Producto 1", "price": 100},
    {"id": 2, "name": "Producto 2", "price": 200},
    {"id": 3, "name": "Producto 3", "price": 50}
]

# Estructura: [{id, name, price, quantity}]
cart: List[dict] = []

class CartItem(BaseModel):
    product_id: int

@app.get("/productos")
def get_products():
    return products

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
