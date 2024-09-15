# app/db.py
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from typing import Optional

class Database:
    client: Optional[AsyncIOMotorClient] = None

    @classmethod
    async def connect(cls):
        cls.client = AsyncIOMotorClient('mongodb://localhost:27017')
        cls.db = cls.client['superjoinProj']  # Use your database name

    @classmethod
    async def close(cls):
        cls.client.close()

db = Database()
