from openai import OpenAI

# It's critical to keep API keys secure and not hard-code them in scripts
client = OpenAI(api_key='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')

# Config
engine_version = 'gpt-4'  # Assuming the use of a ChatGPT model, "gpt-3.5-turbo" might be a correct identifier; verify with the latest documentation

def fetch_action_suggestion(principle, user_context):
    """
    Fetches an action suggestion based on a given principle and user context.
    
    :param principle: The principle to consider for the action suggestion.
    :param user_context: The user's specific situation or input.
    :return: A string containing the AI-generated action suggestion, prefixed with the principle.
    """
    prompt = f"Given the principle of {principle} and considering this context: '{user_context}', what is an appropriate action to take? Respond in one sentence"

    # match the expected parameters for chat-based completions
    response = client.chat.completions.create(
        model=engine_version,  # Use 'model' instead of 'engine' for specifying the model version
        messages=[{"role": "system", "content": prompt}],  # Wrap the prompt in 'messages' for chat-based models
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Extract the text suggestion from the response
    suggestion = response.choices[0].message.content.strip()

    # Prepend the principle to the suggestion text
    full_suggestion = f"The antidote is {principle}: {suggestion}"

    return full_suggestion