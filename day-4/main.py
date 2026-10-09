from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest,abcd:str):
    return {
        "response": f"You said: {request.message}"
    }