from fastapi import APIRouter
from app.models.requist_models import ChatRequest
from app.services.chatbot_service import generate

chat_router = APIRouter()

@chat_router.post("/chat")
def chat(request: ChatRequest):
    response = generate(request.user_message)
    return {"response": response}