
from cat.looking_glass.cheshire_cat import CheshireCat

ccat = CheshireCat()

def get_sentiment_memories():
    result = []
    
    try:
        collection = ccat.memory.vectors.collections.get("declarative")
        if not collection:
            print("\033[95mCollection 'declarative' not found.\033[0m")
            return result
        
        memories = collection.client.scroll(
            collection_name="declarative",
            with_vectors=True,
            limit=10000,
        )
        
        if not memories or len(memories) == 0:
            print("\033[95mNo memories found in the collection.\033[0m")
            return result
        
        # Appiattire se memories è una lista di liste
        if isinstance(memories, list) and isinstance(memories[0], list):
            memories = [item for sublist in memories for item in sublist]
        
        # Filtrare e processare
        result = [
            {"id": memory.id, "metadata": memory.payload.get("metadata", {})}
            for memory in memories
            if hasattr(memory, "payload") and memory.payload.get("metadata", {}).get("type") == "sentiment_memory"
        ]
    
    except Exception as e:
        print("\033[95mAn error occurred: " + str(e) + "\033[0m")
    
    return result


def clear_sentiment_memories():
    
    collections = list(ccat.memory.vectors.collections.keys())
    if ("declarative" in collections):
        ccat.memory.vectors.collections["declarative"].delete_points_by_metadata_filter({"type": "sentiment_memory"})
