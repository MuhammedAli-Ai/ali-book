import asyncio
import sys
import os
sys.path.append(os.getcwd())
from app.core.ai_client import ai_client

async def main():
    try:
        embedding = await ai_client.get_embedding("test")
        print(f"Embedding dimension: {len(embedding)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
