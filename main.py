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
]

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
    cart.append(product)
    return {"message": "Producto agregado", "cart": cart}

@app.get("/carrito")
def get_cart():
    return {"cart": cart}