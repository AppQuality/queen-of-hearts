from cat.log import log
from .memory import Memory
import json


def save_memory(
    message,
    cat
):
    log.info(message.content)
    log.info(message.why.input)    
    parsed_message = json.loads(message.content)

    value = parsed_message['value']
    log.info(parsed_message)
    memory = Memory(cat, value, message.why.input, parsed_message["why"])
    
    memory.save()