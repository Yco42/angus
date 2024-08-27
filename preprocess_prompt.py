import openai
from character_module import response_character
from principles_module import principles_keywords
from action_suggestions_module import fetch_action_suggestion

# Assuming the OpenAI API key is set in your environment variables,
# or you can set it directly (ensure secure management of your API key)
openai.api_key = ''

def main():
    # Prompt the user for input
    user_input = input("What's bothering you? ")
    next_user_input = input("I have some suggestions... ")
    
    # Generate the preprocessed prompt
    preprocessed_prompt = generate_prompt(user_input)
    print(preprocessed_prompt)
    
    # Suggest an action based on the context of the previous user_input
    action_suggestion = suggest_action_based_on_context(user_input, next_user_input)
    print(action_suggestion)

def generate_prompt(user_input):
    identified_principles = []
    
    for principle, keywords in principles_keywords.items():
        if any(keyword in user_input for keyword in keywords):
            identified_principles.append(principle)
    
    principle_part = ", ".join(identified_principles)
    if principle_part:
        principle_part = f" and considering the principle(s) of {principle_part}"
    
    return f"Write a response in the style of {response_character} and their principle of {principle_part}, '{user_input}'?"

def suggest_action_based_on_context(previous_input, next_input):
    identified_principles = []
    
    for principle, keywords in principles_keywords.items():
        if any(keyword in previous_input for keyword in keywords):
            identified_principles.append(principle)
    
    # If principles are identified, fetch suggestions based on those principles
    suggestions = []
    if identified_principles:
        for principle in identified_principles:
            suggestion = fetch_action_suggestion(principle, next_input)
            suggestions.append(suggestion)
    else:
        # Default suggestion if no specific principle is identified
        suggestions.append("Hmm. Mind being more specific?")
    
    return " ".join(suggestions)

if __name__ == '__main__':
    main()




"""
import openai
from character_module import response_character
from principles_module import principles_keywords
from action_suggestions_module import fetch_action_suggestion


# Config
#openai.api_key = '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'
engine_version = "gpt-3.5"

# Prompt the user for input
user_input = input("What's bothering you? ")
next_user_input = input("I have some suggestions... ")

def generate_prompt(user_input):
    identified_principles = []
    
    for principle, keywords in principles_keywords.items():
        if any(keyword in user_input for keyword in keywords):
            identified_principles.append(principle)
    
    principle_part = ", ".join(identified_principles)
    if principle_part:
        principle_part = f" and considering the principle(s) of {principle_part}"
    
    return f"How should I, embodying {response_character}{principle_part}, respond to them in one short sentence? '{user_input}'?"

def suggest_action_based_on_context(previous_input, next_input):
    identified_principles = []
    
    for principle, keywords in principles_keywords.items():
        if any(keyword in previous_input for keyword in keywords):
            identified_principles.append(principle)
    
    # If principles are identified, fetch suggestions based on those principles
    suggestions = []
    if identified_principles:
        for principle in identified_principles:
            suggestion = fetch_action_suggestion(principle, next_input)
            suggestions.append(suggestion)
    else:
        # Default suggestion if no specific principle is identified
        suggestions.append("Hmm. I might need a few more specifics.")
    
    return " ".join(suggestions)

# Generate the preprocessed prompt
preprocessed_prompt = generate_prompt(user_input)

# Suggest an action based on the context of the previous user_input
action_suggestion = suggest_action_based_on_context(user_input, next_user_input)

# These would be printed to the app UI?
print(preprocessed_prompt)
print(action_suggestion)

"""