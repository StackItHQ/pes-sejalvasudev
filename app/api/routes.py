# app/api/routes.py
from fastapi import APIRouter, HTTPException
from app.models import Item
from app.crud import create_item, get_items, update_item, delete_item

router = APIRouter()

@router.post("/items/")
async def create_item_route(item: Item):
    item_id = await create_item(item)
    return {"item_id": str(item_id)}

@router.get("/items/")
async def get_items_route():
    items = await get_items()
    return items

@router.put("/items/{item_id}")
async def update_item_route(item_id: str, item: Item):
    updated_count = await update_item(item_id, item)
    if updated_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"updated_count": updated_count}

@router.delete("/items/{item_id}")
async def delete_item_route(item_id: str):
    deleted_count = await delete_item(item_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted_count": deleted_count}
