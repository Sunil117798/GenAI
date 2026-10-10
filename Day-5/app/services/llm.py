
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Read the Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is missing. Check your .env file."
    )

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

async def generate_chat_response(message: str, system_prompt: str = "You are a helpful AI assistant."):
    response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            max_tokens=500,
        )

    answer = response.choices[0].message.content
    return answer

async def summarize_text(text: str) -> str:

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "Summarize the provided text clearly and concisely."},
            {"role": "user", "content": text}
        ],
        max_tokens=150,
    )

    return response.choices[0].message.content