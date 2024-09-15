# app/models.py
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    age: int
    university: str
    course: str
