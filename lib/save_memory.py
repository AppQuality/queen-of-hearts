from cat.log import log
from .memory import Memory
import json

def is_valid_json(json_string):
    try:
        json.loads(json_string)
        return True
    except (ValueError, TypeError):
        return False

def save_memory(
    message,
    cat
):
    if (is_valid_json(message.content)):
        parsed_message = json.loads(message.content)

        value = parsed_message['value']
        log.info(parsed_message)
        memory = Memory(cat, value, message.why.input, parsed_message["why"])
        
        memory.save()