"""Starter code for the FastAPI REST API assignment."""

from typing import Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Assignment - FastAPI REST API")


class ItemCreate(BaseModel):
    name: str
    price: float


class Item(ItemCreate):
    id: int


# In-memory database for the assignment
items_db: Dict[int, Item] = {}
next_id = 1


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/items", response_model=Item)
def create_item(payload: ItemCreate) -> Item:
    global next_id

    # TODO: create an Item with an auto-generated id, store it, and return it.
    raise NotImplementedError("Implement create_item")


@app.get("/items", response_model=List[Item])
def list_items(min_price: float | None = None) -> List[Item]:
    # TODO: return all items or filter by min_price when provided.
    raise NotImplementedError("Implement list_items")


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate) -> Item:
    # TODO: update an existing item. If item_id does not exist, raise HTTPException(404).
    raise NotImplementedError("Implement update_item")


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict:
    # TODO: delete an existing item. If item_id does not exist, raise HTTPException(404).
    raise NotImplementedError("Implement delete_item")
