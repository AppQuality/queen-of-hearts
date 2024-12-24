
from cat.looking_glass.cheshire_cat import CheshireCat

ccat = CheshireCat()

def get_sentiment_memories():
    result = []

    collection = ccat.memory.vectors.collections["declarative"]
    memories = collection.client.scroll(
        collection_name="declarative",
        with_vectors=True,
        limit=10000,  # yeah, good for now dear :*
    )
    if len(memories) > 0:
        memories = memories[0]
        
        memories = [memory for memory in memories if memory.payload["metadata"]["type"] == "sentiment_memory"]
        
        # get metadata and id only
        result = [{"id": memory.id, "metadata": memory.payload["metadata"]} for memory in memories]
        
        
    return result

def clear_sentiment_memories():
    
    collections = list(ccat.memory.vectors.collections.keys())
    if ("declarative" in collections):
        ccat.memory.vectors.collections["declarative"].delete_points_by_metadata_filter({"type": "sentiment_memory"})
