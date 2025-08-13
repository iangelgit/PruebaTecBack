# Prueba Técnica: API y Carrito de Compras

Construir una API básica que gestione productos y un carrito de compras, junto con un frontend que consuma esta API para permitir agregar y visualizar productos en el carrito.

El **backend** (FastAPI) maneja productos y carrito, mientras que el **frontend** (React + TypeScript) permite interactuar con él.

## Tecnologías
- **Backend:** Python, FastAPI  
- **Frontend:** React, TypeScript  
- **Herramientas:** pip, npm

## Cómo ejecutar el proyecto

### Backend
1. Abrir la carpeta del backend.  
2. Instalar dependencias:  
   ```bash
   pip install -r requirements.txt
   ````

3. Activar el entorno virtual (si aplica):

   ```bash
   .venv\Scripts\activate
   ```
4. Ejecutar el servidor:

   ```bash
   uvicorn main:app --reload
   ```

   El backend estará en `http://localhost:8000`.

### Frontend

1. Abrir la carpeta del frontend.
2. Instalar dependencias:

   ```bash
   npm install
   ```
3. Ejecutar la aplicación:

   ```bash
   npm run dev
   ```

   El frontend estará en `http://localhost:5173`.

---

## Endpoints del Backend

| Método | Ruta                   | Descripción                                       | Body / Query                                                |
| ------ | ---------------------- | ------------------------------------------------- | ----------------------------------------------------------- |
| GET    | /productos             | Devuelve la lista de productos                    | -                                                           |
| POST   | /productos             | Agrega un nuevo producto                          | `{ "name": "Producto X", "price": 100 }`                    |
| GET    | /carrito               | Devuelve los productos en el carrito con cantidad | -                                                           |
| POST   | /carrito               | Agrega una unidad de un producto                  | `{ "product_id": 1 }`                                       |
| DELETE | /carrito/{product\_id} | Elimina un producto del carrito                   | Query opcional: `all=true` para eliminar todas las unidades |
