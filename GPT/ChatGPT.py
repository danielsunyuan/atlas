from conversation import ConversationManager
from file_manager import FileManager
from openai_api_call import GPT


DIRECTORY_PATH = 'Conversations'
CONVERSATIONS = 'conversation.json'

def ChatGPT(text):

    #Initialise
    conversation_manager = ConversationManager(CONVERSATIONS, DIRECTORY_PATH)

    conversation_manager.clear_conversation()
    conversation_manager.json_initiate()

    # Store User Messages
    conversation_manager.user_store(text)
    convo = conversation_manager.read_conversation()

    # GPT 3.5 API 
    response = GPT.chat_gpt(convo)
    conversation_manager.ai_store(response)

    return response


if __name__ == "__main__":

    text = "Hello World"
    response = ChatGPT(text)
    print(f'\nAtlas: {response}\n')