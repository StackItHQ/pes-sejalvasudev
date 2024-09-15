from fastapi import APIRouter, HTTPException, File, UploadFile, Request
from fastapi.responses import HTMLResponse
import pandas as pd
import io
from app.logging_config import setup_logging  # Import logging setup
from googleapiclient.discovery import build
from google.oauth2 import service_account
from typing import List

# Initialize logging
logger = setup_logging()

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
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        logger.info("CSV Data Loaded Successfully")
        logger.info(f"DataFrame head:\n{df.head()}")

        data = df.head().to_dict(orient='records')
        columns = df.columns.tolist()

        return {"filename": file.filename, "columns": columns, "data": data}
    except Exception as e:
        logger.error(f"Error processing file: {e}")
        return {"error": str(e)}

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
