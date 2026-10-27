from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Bao Free API", version="1.0.0")

items = [
    {"id": 1, "name": "sample", "price": 10.0},
    {"id": 2, "name": "demo", "price": 20.0},
]

class ItemCreate(BaseModel):
    name: str
    price: float

@app.get("/")
def root():
    return {"message": "Bao API is running", "status": "ok"}

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "bao-api"}

@app.get("/api/items", response_model=List[dict])
def get_items():
    return items

@app.post("/api/items")
def create_item(item: ItemCreate):
    new_item = {"id": len(items) + 1, "name": item.name, "price": item.price}
    items.append(new_item)
    return {"message": "created", "data": new_item}
