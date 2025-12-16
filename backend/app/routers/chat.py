from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.services.rag_service import generate_rag_response
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/query", response_model=ChatResponse)
async def query_chat(request: ChatRequest):
    try:
        logger.info(f"Received question: {request.question}")
        result = await generate_rag_response(request.question)
        return ChatResponse(**result)
    except Exception as e:
        logger.error(f"Error processing question: {e}")
        raise HTTPException(status_code=500, detail=str(e))
