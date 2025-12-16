from qdrant_client import QdrantClient
print("Imported QdrantClient")
try:
    client = QdrantClient(location=":memory:")
    print(f"Client type: {type(client)}")
    print(f"Has search: {hasattr(client, 'search')}")
    print(f"Dir: {dir(client)}")
except Exception as e:
    print(f"Error: {e}")
