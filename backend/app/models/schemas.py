from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    question: str
    history: Optional[List[dict]] = None # List of {"role": "user", "content": "..."}

class Source(BaseModel):
    title: str
    url: str
    snippet: str
    score: float

class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]
