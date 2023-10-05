import os
import time
import json
import openai

MODEL = "gpt-3.5-turbo"
#MODEL = "gpt-4"

CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
TEMPERATURE = 0.5

class GPT:

    # Load configuration
    @staticmethod
    def load_config():
        with open(CONFIG_FILE_PATH) as config_file:
            return json.load(config_file)

    # Initialize OpenAI API
    @staticmethod
    def openai_init():
        config = GPT.load_config()
        openai.api_key = config['openai_api_key']

    # Call OpenAI Chat Completion API
    @staticmethod
    def chat_gpt(message_array):
        GPT.openai_init()

        start_time = time.time()

        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=message_array,
            temperature=TEMPERATURE,
        )

        # Measure Response Time
        print(f"{(time.time() - start_time):.2f} secs")

        return response['choices'][0]['message']['content']

# Test function
def test():

    OPENAI = GPT
    prompt = "What is the sun?"
    message_array = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    response = OPENAI.chat_gpt(message_array)
    print(response)


if __name__ == "__main__":
    test()