# app/crud.py
from app.db import db
from app.models import Item
from typing import List

async def create_item(item: Item):
    result = await db.db['items'].insert_one(item.dict())
    return result.inserted_id

async def get_items() -> List[Item]:
    items = await db.db['items'].find().to_list(length=100)
    return [Item(**item) for item in items]

async def update_item(item_id: str, item: Item):
    result = await db.db['items'].update_one({"_id": item_id}, {"$set": item.dict()})
    return result.modified_count

async def delete_item(item_id: str):
    result = await db.db['items'].delete_one({"_id": item_id})
    return result.deleted_count
