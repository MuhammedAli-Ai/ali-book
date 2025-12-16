import os
import asyncio
import glob
from uuid import uuid4
from qdrant_client import QdrantClient
from qdrant_client.http import models
from app.core.config import get_settings
from app.core.ai_client import ai_client
import re

settings = get_settings()

# We need to set the environment variable for the script to load .env correctly if run directly
# But usually the app runs with .env loaded.

qdrant = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY,
)

COLLECTION_NAME = settings.QDRANT_COLLECTION_NAME

def extract_text_and_metadata(filepath):
    """
    Simple markdown parser.
    Assumes frontmatter is between --- and ---
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract frontmatter title
    title_match = re.search(r'title:\s*(.*)', content)
    title = title_match.group(1).strip() if title_match else os.path.basename(filepath)

    # Remove frontmatter
    content = re.sub(r'^---[\s\S]*?---', '', content)
    
    return title, content

def chunk_text(text, chunk_size=1000, overlap=100):
    """
    Simple chunking by character count.
    A better approach would be semantic split by headers.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - overlap)
    return chunks

async def index_docs():
    
    # 1. Create Collection if not exists
    try:
        qdrant.get_collection(COLLECTION_NAME)
        print(f"Collection {COLLECTION_NAME} exists.")
    except:
        print(f"Creating collection {COLLECTION_NAME}...")
        qdrant.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
        )

    # 2. Find all MD files
    root_dir = "../docs"
    files = glob.glob(f"{root_dir}/**/*.md", recursive=True)
    
    print(f"Found {len(files)} markdown files.")
    
    total_chunks = 0
    
    for filepath in files:
        if "node_modules" in filepath:
            continue
            
        print(f"Processing {filepath}...")
        title, content = extract_text_and_metadata(filepath)
        chunks = chunk_text(content)
        
        for i, chunk in enumerate(chunks):
            if not chunk.strip():
                continue
                
            # Generate Embedding
            embedding = await ai_client.get_embedding(chunk)
            
            # Upsert
            qdrant.upsert(
                collection_name=COLLECTION_NAME,
                points=[
                    models.PointStruct(
                        id=str(uuid4()),
                        vector=embedding,
                        payload={
                            "title": title,
                            "text": chunk,
                            "url": filepath, # In production, convert to real URL
                            "chunk_id": i
                        }
                    )
                ]
            )
            total_chunks += 1
            print(f"  Indexed chunk {i+1}/{len(chunks)}")
            
    print(f"Indexing complete. Total chunks: {total_chunks}")

if __name__ == "__main__":
    import sys
    # Add parent dir to path so imports work
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    asyncio.run(index_docs())
