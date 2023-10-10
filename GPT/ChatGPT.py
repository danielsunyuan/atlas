from Conversations.conversation import ConversationManager
from Conversations.file_manager import FileManager
from openai_api_call import GPT


DIRECTORY_PATH = ''
CONVERSATIONS = 'conversation.json'

def ChatGPT(text):
    conversation_manager = ConversationManager(CONVERSATIONS, DIRECTORY_PATH)

    conversation_manager.clear_conversation()
    current_conversation_file = conversation_manager.json_initiate()

    print(f"Conversation file created at: {current_conversation_file}")

    # While "Words detected for GPT" send the transcription through
    while True:
        user_input = text

        # Store User Messages
        conversation_manager.user_store(user_input)
        convo = conversation_manager.read_conversation()

        # GPT 3.5 API 
        response = GPT.chat_gpt(convo)
        conversation_manager.ai_store(response)
        print(f'\nAtlas: {response}\n')


if __name__ == "__main__":

    text = "hellow"
    ChatGPT(text)