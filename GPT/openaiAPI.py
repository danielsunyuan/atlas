import os
import time
import json
import openai

# Constants
MODEL = "gpt-3.5-turbo"
#MODEL = "gpt-4"

CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

# Load configuration
def load_config():
    with open(CONFIG_FILE_PATH) as config_file:
        return json.load(config_file)

# Initialize OpenAI API
def initialize_openai():
    config = load_config()
    openai.api_key = config['openai_api_key']

# Call OpenAI Chat Completion API
def chat_gpt(message_array, temperature=0.5):
    initialize_openai()
    start_time = time.time()

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=message_array,
        temperature=temperature,
    )

    # Check for errors in the response
    if response['object'] == 'error':
        print("API call failed with error:")
        print(response['error'])

    response_time = time.time() - start_time
    formatted_response_time = f"{response_time:.2f} secs"
    print(formatted_response_time)

    return response['choices'][0]['message']['content']

# Test function
def test():

    initialize_openai()
    message_array = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you help me with a question?"},
        {"role": "assistant", "content": "Of course! What do you need assistance with?"},
        {"role": "user", "content": "I have a problem with my computer."},
        {"role": "assistant", "content": "Please provide more details about the issue."},
        {"role": "user", "content": "It keeps crashing whenever I open a specific program."},
    ]
    response = chat_gpt(message_array)
    print(response)


if __name__ == "__main__":
    test()
