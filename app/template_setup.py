# app/template_setup.py
from fastapi.templating import Jinja2Templates

# Initialize the templates object
templates = Jinja2Templates(directory="app/templates")
