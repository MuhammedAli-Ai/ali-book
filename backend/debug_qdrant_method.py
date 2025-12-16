from qdrant_client import QdrantClient
import inspect

try:
    client = QdrantClient(location=":memory:")
    print("Function signature of query_points:")
    print(inspect.signature(client.query_points))
    
    print("\nFunction signature of query:")
    print(inspect.signature(client.query))

except Exception as e:
    print(f"Error: {e}")
