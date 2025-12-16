# Physical AI Textbook Backend

This is the FastAPI backend for the Physical AI Textbook RAG Chatbot.

## Setup

1. Install `uv`:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Sync dependencies:
   ```bash
   uv sync
   ```

3. Setup environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

## Running the Server

```bash
uv run uvicorn app.main:app --reload
```

## Indexing Content

```bash
uv run python scripts/index_content.py
```
