from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from app.db import db
from app.routes import router
from app.logging_config import setup_logging  # Import logging setup

# Configure logging
logger = setup_logging()

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Serve HTML templates
templates = Jinja2Templates(directory="app/templates")

# Include the routes
app.include_router(router)

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.on_event("startup")
async def on_startup():
    await db.connect()
    logger.info("Database connected")

@app.on_event("shutdown")
async def on_shutdown():
    await db.close()
    logger.info("Database connection closed")
