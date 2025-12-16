from app.core.ai_client import ai_client

async def generate_embedding(text: str) -> list[float]:
    return await ai_client.get_embedding(text)
