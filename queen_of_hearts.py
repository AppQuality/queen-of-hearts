from cat.mad_hatter.decorators import hook
from cat.mad_hatter.decorators import plugin

from .lib.sentiment_memory import get_sentiment_memories,clear_sentiment_memories
from .lib.activation import activation
from .lib.prefix import prompt_prefix
from .lib.save_memory import save_memory



@hook
def agent_prompt_prefix(prefix, cat):
    return prompt_prefix

@plugin
def activated(plugin):
    activation(plugin)

@hook
def before_cat_sends_message(message, cat):
    save_memory( message,cat)
    return message  


@hook(priority=0)
def agent_fast_reply(fast_reply, cat):
    if (cat.working_memory.user_message_json.text == "/empty_qoh"):
        memories = get_sentiment_memories()
        
        if len(memories) > 0:
            clear_sentiment_memories()
            return {
                "output": "Ok, la memoria di Queen of Hearts è stata svuotata."
            }
        
        
        return {"output":"Non c'è nulla da svuotare."}
    elif (cat.working_memory.user_message_json.text == "/show_qoh"):
        memories = get_sentiment_memories()
        
        return {"output":str(memories)}
