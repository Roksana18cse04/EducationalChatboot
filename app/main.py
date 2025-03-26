from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.api.v1.endpoints.chat_routes import chat_router
from app.utils.env_loader import load_environment
#hi
# Load environment variables
load_environment()

app = FastAPI()

# Include the router with a prefix
app.include_router(chat_router, prefix="/api/v1")
# Set up templates directory

templates = Jinja2Templates(directory="templates")

# Mount static files for serving JavaScript and CSS

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Educational Chatboot"})