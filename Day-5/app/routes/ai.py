from fastapi import APIRouter

from app.schemas.ai import (
    ChatRequest,
    ChatResponse,
    SummarizeRequest,
    SummarizeResponse
)

from app.services.llm import (
    generate_chat_response,
    summarize_text,
)


router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
async def chat(request: ChatRequest):

    answer = await generate_chat_response(
        message=request.message,
        system_prompt=request.system_prompt
    )

    return ChatResponse(
        response=answer
    )


@router.post(
    "/summarize",
    response_model=SummarizeResponse
)
async def summarize(request: SummarizeRequest):

    summary = await summarize_text(
        request.text
    )

    return SummarizeResponse(
        summary=summary
    )