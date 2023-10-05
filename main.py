from Transcriber import reader as transcription
from Transcriber import whisper as whisper
from GPT import openai
from GPT import conversation
import time

# CONSTANTS
DIRECTORY_PATH = 'conversations'
CONVERSATIONS = 'conversation.json'


def chatGPT(text):
    conversation_manager = conversation.ConversationManager(CONVERSATIONS, DIRECTORY_PATH)

    conversation_manager.clear_conversation()
    current_conversation_file = conversation_manager.json_initiate()

    print(f"Conversation file created at: {current_conversation_file}")

    while True:
        user_input = text

        # Store User Messages
        conversation_manager.user_store(user_input)
        convo = conversation_manager.read_conversation()

        # GPT 3.5 API 
        response = openai.chat_gpt(convo)
        conversation_manager.ai_store(response)
        print(f'\nAtlas: {response}\n')



if __name__ == "__main__":

    # stream = whisper.run_whisper()

    # Create an instance of the ReadTranscription class
    reader = transcription.ReadTranscription()

    while True:
        # Call the read_and_clear method on the instance
        transcript = reader.read_and_clear()

        if transcript is not None and transcript.strip():

            print("sending to GPT")
            chatGPT(transcript)

        time.sleep(2)
        print("----")