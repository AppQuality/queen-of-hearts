from cat.mad_hatter.decorators import hook
from cat.mad_hatter.decorators import plugin
from cat.mad_hatter.decorators import tool
from cat.db.crud import get_setting_by_name,delete_setting_by_id

from .lib.const import QUEEN_OF_HEARTS_INJESTION_SETTING
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
        
        collections = list(cat.memory.vectors.collections.keys())
        if ("declarative" in collections):
            print(cat.memory.vectors.collections["declarative"].delete_points_by_metadata_filter({"type": "sentiment_memory"}))
        
        setting = get_setting_by_name(QUEEN_OF_HEARTS_INJESTION_SETTING)
        if setting is not None:
            delete_setting_by_id(setting["setting_id"])
            return {
                "output": "Ok, la memoria di Queen of Hearts è stata svuotata."
            }
        
        return {"output":"Non c'è nulla da svuotare."}
