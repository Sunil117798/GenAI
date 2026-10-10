from pydantic import BaseModel

# chat request and response schemas
class ChatRequest(BaseModel):
    message: str
    system_prompt: str = "You are a helpful AI assistant."


class ChatResponse(BaseModel):
    response: str


# summarize request and response schemas
class SummarizeRequest(BaseModel):
    text: str


class SummarizeResponse(BaseModel):
    summary: str