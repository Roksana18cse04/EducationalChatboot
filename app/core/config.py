import os
from app.utils.env_loader import load_environment

# Load environment variables
load_environment()
# Application settings
APP_NAME = "ChatBot FastAPI"
APP_VERSION = "1.0.0"

# Environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.0-flash-thinking-exp-01-21"