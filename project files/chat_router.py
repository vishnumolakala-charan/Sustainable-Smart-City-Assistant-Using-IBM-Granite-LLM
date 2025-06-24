# chat_router.py

"""
Chat Assistant Router
---------------------
Provides a REST endpoint to accept user prompts and generate responses using
IBM Watsonx Granite LLM (via ask_granite function).

Skill Tags:
- FastAPI Endpoint
- Prompt Handling
- Granite LLM Integration
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.granite_llm import ask_granite

router = APIRouter(prefix="/chat", tags=["Chat Assistant"])

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str

@router.post("/ask", response_model=ChatResponse)
async def ask_chat(request: ChatRequest):
    """
    POST /chat/ask
    Accepts a prompt string and returns a response from the LLM.
    """
    try:
        result = ask_granite(request.prompt)
        return ChatResponse(response=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
