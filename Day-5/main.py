import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from groq import Groq

# Load variables from .env
load_dotenv()

app = FastAPI(title="GenAI Chat API")

# Read the Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is missing. Check your .env file."
    )

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)


# Request schema
class ChatRequest(BaseModel):
    message: str
    system_prompt: str = "You are a helpful AI assistant."

class ChatResponse(BaseModel):
    response: str


def get_llm(request:ChatRequest):
    response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            instructions=request.system_prompt,

            messages=[
                {"role": "system", "content": request.system_prompt},
                {"role": "user", "content": request.message}
            ],
            max_tokens=500,
        )

    answer = response.choices[0].message.content
    return {"response": answer}


@app.get("/")
async def home():
    return {"message": "GenAI Chat API is running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        return get_llm(request)

    except Exception as exc:
        # Print the full error in the Uvicorn terminal
        print(f"Chat API error: {type(exc).__name__}: {exc}")

        raise HTTPException(
            status_code=502,
            detail=f"Model inference failed: {str(exc)}",
        )