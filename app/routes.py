# app/routes.py
from fastapi import APIRouter, HTTPException, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates  # Import Jinja2Templates directly here
from app.models import Item
from app.crud import create_item, get_items, update_item, delete_item
import pandas as pd
import io
from googleapiclient.discovery import build
from google.oauth2 import service_account
from typing import List

# Initialize Google Sheets API
creds = service_account.Credentials.from_service_account_file('credentials.json')
service = build('sheets', 'v4', credentials=creds)
SPREADSHEET_ID = '1oFDdIz-zg1gZ5tGVO3Mesjqn39nT_ouWiYf4l_toqCI'

def write_to_google_sheets(values):
    body = {'values': values}
    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range='Sheet1!A1',
        valueInputOption='RAW',
        body=body
    ).execute()

router = APIRouter()

# Initialize the Jinja2 templates inside the router directly
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

# The rest of the routes...

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

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
    return {"filename": file.filename, "columns": df.columns.tolist(), "data": df.head().to_dict()}

@router.post("/import-to-sheets/")
async def import_to_sheets(data: List[List[str]]):
    write_to_google_sheets(data)
    return {"status": "Data imported successfully"}

@router.post("/parse-csv/")
async def parse_csv(file: UploadFile = File(...), filter_column: str = None, filter_value: str = None):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
    
    # Apply filter if specified
    if filter_column and filter_value:
        df = df[df[filter_column] == filter_value]
    
    # Convert DataFrame to list of lists for Google Sheets
    data = df.values.tolist()
    return {"data": data}
