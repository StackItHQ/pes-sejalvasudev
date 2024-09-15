# app/main.py
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from app.db import db
from typing import List

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Serve HTML templates
templates = Jinja2Templates(directory="app/templates")

# Example route for homepage
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.on_event("startup")
async def on_startup():
    await db.connect()

@app.on_event("shutdown")
async def on_shutdown():
    await db.close()

# Import and include routes here

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # Process the CSV file contents
    # Example: Save to a temporary location, parse the CSV, etc.
    return JSONResponse(content={"filename": file.filename, "content_type": file.content_type})
