from pydantic import BaseModel

# Define a model for chatbot requests
class ChatRequest(BaseModel):
    user_message: str
