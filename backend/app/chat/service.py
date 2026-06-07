import google.generativeai as genai
from .repository import create_chat_message,get_chat_history
from app.core.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def ask_gemini_and_save(
    db,
    current_user,
    message: str
):
    prompt = f"""
    You are an interview preparation assistant.

    Explain the topic in:
    1. Simple explanation
    2. Real-world example
    3. Interview interview questions
    4. Common mistakes

    Topic:
    {message}
    """
    response = model.generate_content(prompt)


    create_chat_message(
        db,
        current_user.id,
        message,
        response.text
    )

    return {
        "response": response.text
    }

def get_user_chat_history(
    db,
    current_user
):
    return get_chat_history(
        db,
        current_user.id
    )