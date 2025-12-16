import google.generativeai as genai
from app.core.config import get_settings
import asyncio

settings = get_settings()

class AIClient:
    def __init__(self):
        self.provider = "gemini"
        
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            
    async def get_embedding(self, text: str) -> list[float]:
        # Run blocking call in thread
        try:
            result = await asyncio.to_thread(
                genai.embed_content,
                model="models/text-embedding-004",
                content=text,
                task_type="retrieval_query"
            )
            return result['embedding']
        except Exception as e:
            print(f"Error generating embedding: {e}")
            return []

    async def get_chat_completion(self, messages: list, model: str = "gemini-flash-latest") -> str:
        # Convert OpenAI-style messages to Gemini history if possible, 
        # but for simple one-off:
        try:
            last_msg = messages[-1]['content']
            system_instruction = next((m['content'] for m in messages if m['role'] == 'system'), None)
            
            model_instance = genai.GenerativeModel(
                model_name=model,
                system_instruction=system_instruction
            )
            
            # Simple prompt construction for now to handle context + question
            # (Assuming messages are [system, user_with_context])
            response = await asyncio.to_thread(
                model_instance.generate_content,
                last_msg
            )
            return response.text
        except Exception as e:
            print(f"Error generating chat completion: {e}")
            return f"I apologize, but I encountered an error generating the response. (Error: {str(e)})"

ai_client = AIClient()
