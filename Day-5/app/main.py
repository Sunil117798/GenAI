from fastapi import FastAPI

from app.routes.ai import router as ai_router


app = FastAPI(
    title="AI Backend v1",
    description="GenAI backend built with FastAPI",
    version="1.0.0"
)


@app.get("/")
async def home():
    return {
        "message": "AI Backend is running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


app.include_router(ai_router)