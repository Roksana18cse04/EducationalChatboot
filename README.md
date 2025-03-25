# FastAPI Chatbot

This project is a customizable chatbot application built using FastAPI. It provides an interactive interface for users to engage with a chatbot that can answer questions and provide information on various topics.

---

## Project Structure

```
CHATBOOTFASTAPI
├── app
│   ├── __init__.py               # Package initializer
│   ├── main.py                   # Entry point for the FastAPI application
│   ├── api                       # API-related modules
│   │   ├── __init__.py
│   │   └── endpoints.py          # API endpoint definitions
│   ├── core                      # Core application configurations
│   │   ├── __init__.py
│   │   └── config.py             # Configuration settings (e.g., environment variables)
│   ├── models                    # Data models for request/response validation
│   │   ├── __init__.py
│   │   └── request_models.py     # Pydantic models for API requests
│   ├── services                  # Business logic and service layer
│   │   ├── __init__.py
│   │   └── chatbot_service.py    # Chatbot logic and response generation
│   ├           # Main chatbot interface
│── templates                 # HTML templates for the frontend
│      └── index.html          # Custom type definitions
├── .env                          # Environment variables (API keys, secrets)
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── LICENSE                       # License information
```

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Roksana18cse04/EducationalChatboot.git
   cd ChatBootFastapi
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys and other configuration settings. Example:
   ```
   GEMINI_API_KEY=your_api_key_here
   MODEL_NAME=gemini-2.0
   ```

6. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Usage

Once the application is running, you can:
- Access the chatbot interface in your browser at `http://127.0.0.1:8000`.
- Interact with the chatbot by typing messages in the input box.
- Use the API endpoints to send and receive chatbot responses programmatically.

---

## Features

- **Interactive Chat Interface**: A user-friendly web interface for chatting with the bot.
- **Dynamic Markdown Rendering**: Bot responses are rendered beautifully using Markdown.
- **Customizable Logic**: Easily extend the chatbot's logic to handle new topics or formats.
- **FastAPI Framework**: Built with FastAPI for high performance and scalability.

---

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.