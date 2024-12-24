from cat.mad_hatter.decorators import hook
from cat.mad_hatter.decorators import plugin
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