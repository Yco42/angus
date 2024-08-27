import openai
from character_module import response_character
from principles_module import principles_keywords
from action_suggestions_module import fetch_action_suggestion


engine_version = 'gpt-4'

# Use input() to get user_input from the console
user_input = input("What's bothering you?: ")

def identify_principles(user_input):
    identified_principles = []
    # Check if any keyword related to a principle is in the user input
    for principle, keywords in principles_keywords.items():
        if any(keyword in user_input for keyword in keywords):
            identified_principles.append(principle)
    return identified_principles

# Call identify_principles to get the list of principles based on user_input
principles = identify_principles(user_input)

# If multiple principles are identified, decide how to handle them. Here, taking the first identified principle.
principle = principles[0] if principles else "general kindness"  # Using "general kindness" as a fallback principle

# Fetch the action suggestion for the identified principle. Remember to adjust the engine version as needed.
action_suggestion = fetch_action_suggestion(principle, user_input)
print(action_suggestion)
