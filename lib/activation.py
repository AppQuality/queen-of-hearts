import os
import json
from .memory import Memory
from cat.looking_glass.cheshire_cat import CheshireCat


ccat = CheshireCat()


default_memories = [
    {
        "id":1,
        "value": 1,
        "text": "Right now it's not clear to me how I can proceed, meaning, I don't understand what I have to do to reach the questions or anyway where", 
        "reason": "the user is confused about how to complete their task: \"not clear to me\""
    },
    {
        "id":2,
        "value": 1,
        "text": "Selecting the testers takes a lot of time, even though there's the new page that I know was released some time ago",
        "reason": "the interviewee is frustrated by the inefficiency of the functionality: \"takes a lot of time\""
    },
    {
        "id":3,
        "value": 2,
        "text": "I might have expected that there would already be options, that I could write the options directly below",
        "reason": "the interface does not meet the user's expectations"
    },
    {
        "id":4,
        "value": 2,
        "text": "I don't understand the other two icons, I find it a bit frustrating, a bit annoying",
        "reason": "the user expresses slight annoyance and frustration: \"a bit\""
    },
    {
        "id":5,
        "value": 3,
        "text": "Maybe it's not necessary but it could be useful to have an integration with an external tool",
        "reason": "the user suggests a feature but does not express a strong conviction"
    },
    {
        "id":6,
        "value": 3,
        "text": "I haven't had the chance to fully experience the new feature yet",
        "reason": "the interviewee reports an objective fact, not an evaluation of the tool"
    },
    {
        
        "id":7,
        "value": 4,
        "text": "I find the filter function very useful during selection",
        "reason": "the user believes the feature is useful for accomplishing their task"
    },
    {
        "id":8,
        "value": 4,
        "text": "Then there's a section for alerts and news: interesting to understand if there are already updates or problems",
        "reason": "the user shows interest in the section and believes it meets a potential need: \"interesting\""
    },
    {
        "id":9,
        "value": 5,
        "text": "The filter management is extremely convenient, essential!",
        "reason": "the user believes the feature is essential for accomplishing their task"
    },
    {
        "id":10,
        "value": 5,
        "text": "It seems to me that as a page, as a homepage, it is ideal from my point of view, because surely if I go to the Trenord site the first reason I would go is precisely to look for a ticket",
        "reason": "the user believes the interface fully meets their needs and expectations: \"ideal\""
    }
]

def load_injested_ids(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return []

def save_injested_ids(file_path, ids):
    with open(file_path, 'w') as f:
        json.dump(ids, f, indent=4)

def process(item):
    memory = Memory(ccat, item["value"], item["text"], item["reason"])
    memory.save()



def activation(plugin):
    
    # Percorso del file __injested.json
    injested_file = os.path.join(plugin.path, '__injested.json')
    
    # Carica gli ID già ingeriti dal file, se esiste
    injested_ids = load_injested_ids(injested_file)
    
    # Filtra gli ID che non sono nel dizionario
    valid_injested_ids = [id for id in injested_ids if any(item['id'] == id for item in default_memories)]
    
    # Per ogni memoria, se l'id non è stato ancora ingested, processa l'elemento e aggiungi l'id
    for item in default_memories:
        if item['id'] not in valid_injested_ids:
            process(item)
            valid_injested_ids.append(item['id'])

    # Salva la lista aggiornata degli ID nel file
    save_injested_ids(injested_file, valid_injested_ids)