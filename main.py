from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["https://tu-dominio.vercel.app"] para restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
@app.get("/productos")
def get_products():
    return [
        {"id": 1, "name": "Producto 1", "price": 100},
        {"id": 2, "name": "Producto 2", "price": 200},
    ]

cart = []

@app.post("/carrito")
def add_to_cart(item: dict):
    product = next((p for p in get_products() if p["id"] == item["product_id"]), None)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    cart.append(product)
    return {"message": "Producto agregado", "cart": cart}

@app.get("/carrito")
def get_cart():
    return {"cart": cart}
