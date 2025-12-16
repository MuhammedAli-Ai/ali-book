import asyncio
import sys
import os

# Add backend to path
sys.path.append(os.getcwd())

from app.services.rag_service import generate_rag_response

async def main():
    print("Testing RAG extraction...")
    try:
        response = await generate_rag_response("What is Physical AI?")
        print("\n--- Response ---")
        print(response['answer'])
        print("\n--- Sources ---")
        for source in response['sources']:
            print(f"- {source.title}: {source.url}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
