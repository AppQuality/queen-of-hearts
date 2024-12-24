class Memory:
    def __init__(self, ccat, value, message, reason):
        self.ccat = ccat
        self.memory = {
            "value": value,
            "message": message,
            "reason": reason
        }
        self.memory["string_value"] = self.get_sentiment_string()
    
    def set_metadata(self, key, value):
        self.memory[key] = value
        
        
    def get_sentiment_string(self):
        if self.memory["value"] == 1:
            return "Very Negative"
        elif self.memory["value"] == 2:
            return "Negative"
        elif self.memory["value"] == 3:
            return "Neutral"
        elif self.memory["value"] == 4:
            return "Positive"
        elif self.memory["value"] == 5:
            return "Very Positive"
        else:
            return "Unknown"


    def save(self):
        new_memory = "Use the following example as guidelines for the sentiment classification: "
        new_memory += f"[{self.memory['value']} - {self.memory['string_value']}] "
        new_memory += f"{self.memory['message']}. "
        if self.memory["reason"]:
            new_memory += f"Reason: {self.memory['reason']}"
            
        with open('sentiment_memory.txt', 'w') as file:
            file.write(new_memory + '\n')
        metadata = {
            "type": "sentiment_memory",
        }
        if ("default_memory_id" in self.memory):
            metadata["default_memory_id"] = self.memory["default_memory_id"]
        self.ccat.rabbit_hole.ingest_file(self.ccat,'sentiment_memory.txt', metadata=metadata)
        
        
