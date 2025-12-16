from qdrant_client import QdrantClient
from app.core.config import get_settings
from app.core.ai_client import ai_client
from app.models.schemas import Source
from app.services.embedding_service import generate_embedding

settings = get_settings()

try:
    qdrant = QdrantClient(
        url=settings.QDRANT_URL,
        api_key=settings.QDRANT_API_KEY,
    )
except Exception as e:
    print(f"Failed to connect to Qdrant: {e}")
    qdrant = None

async def search_similar(question: str, top_k: int = 3) -> list:
    if not qdrant:
        return []
    
    embedding = await generate_embedding(question)
    
    results = qdrant.query_points(
        collection_name=settings.QDRANT_COLLECTION_NAME,
        query=embedding,
        limit=top_k
    ).points
    return results

async def generate_rag_response(question: str) -> dict:
    # 1. Retrieve
    search_results = await search_similar(question)
    
    context_text = ""
    sources = []
    
    for hit in search_results:
        payload = hit.payload
        context_text += f"---\nTitle: {payload.get('title', 'Unknown')}\nContent: {payload.get('text', '')}\n"
        sources.append(Source(
            title=payload.get('title', 'Unknown'),
            url=payload.get('url', '#'),
            snippet=payload.get('text', '')[:150] + "...",
            score=hit.score
        ))

    # 2. Augment
    system_prompt = """You are an AI teaching assistant for the Physical AI & Humanoid Robotics course. 
    Answer the user's question based ONLY on the following context. 
    If the answer is not in the context, say "I don't have enough information in the textbook to answer that."
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {question}"}
    ]

    # 3. Generate
    answer = await ai_client.get_chat_completion(messages)
    
    return {
        "answer": answer,
        "sources": sources
    }
