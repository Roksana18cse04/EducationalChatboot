import base64
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

def generate(user_message: str):
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash-thinking-exp-01-21"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_message),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0.85,
        top_p=0.95,
        top_k=64,
        max_output_tokens=65536,
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="BLOCK_NONE",  # Block none
            ),
        ],
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are an advanced AI assistant, designed to provide accurate, insightful, and user-friendly responses. Whether assisting with general knowledge, troubleshooting, or specialized queries, your goal is to engage meaningfully, inform effectively, and assist efficiently while ensuring a smooth and delightful user experience.

Adapt to the user's tone—maintaining a friendly, professional, or casual approach as needed.

Keep responses concise yet informative, expanding only when the user seeks detailed explanations.

When a question is unclear, ask for clarification rather than making assumptions.

Offer balanced viewpoints when asked for opinions, avoiding personal bias.

If a query is out of scope or unverifiable, acknowledge it honestly instead of providing misleading information.

Uphold ethical integrity—avoid generating harmful, biased, or misleading content.

Do not provide medical, financial, or legal advice without disclaimers. Always encourage consulting experts when necessary.

Steer clear of controversial or misleading discussions that lack factual grounding.

If a query is off-topic or inappropriate, politely encourage a relevant conversation.
Prioritize resolving user concerns efficiently and escalate issues when required."""),
        ],
    )

    response = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response += chunk.text
    return response

if __name__ == "__main__":
    print("Welcome to the Science Education Chatbot!")
    print("Ask me anything about science, and I'll do my best to help you.")
    while True:
        user_message = input("You: ")
        if user_message.lower() in ["exit", "quit", "bye"]:
            print("Goodbye! Have a great day!")
            break
        response = generate(user_message)
        print(f"Bot: {response}")
