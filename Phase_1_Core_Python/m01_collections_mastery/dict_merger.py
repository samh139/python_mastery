"""
Milestone: m01_collections_mastery
Task: Dict Merger
"""

# The Scenario
# You are building an AI application settings manager. You have a dictionary containing system defaults and 
# another containing user preferences. You need to merge them so that the user's 
# choices overwrite the defaults, and any new unique user settings are added.

##Inputs
default_config = {
    "model": "gpt-4o",
    "temperature": 0.7,
    "max_tokens": 1024,
    "stream": False
}

user_config = {
    "temperature": 0.2,
    "max_tokens": 2048,
    "presence_penalty": 0.5
}


# {
#     "model": "gpt-4o",
#     "temperature": 0.2,
#     "max_tokens": 2048,
#     "stream": False,
#     "presence_penalty": 0.5
# }

new_dict = default_config | user_config
print(new_dict)