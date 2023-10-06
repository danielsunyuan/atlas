import os
import json

def get_conversations_path(directory_path):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        conversations_dir = os.path.join(script_dir, directory_path)

        return conversations_dir

class ConversationManager:
    def __init__(self, filename, directory_path):
        self.file_path = os.path.join(get_conversations_path(directory_path), filename)

    def save_conversation(self, messages):
        existing_messages = self._load_existing_messages()
        existing_messages += messages
        with open(self.file_path, 'w') as f:
            json.dump(existing_messages, f)
        
        return self.file_path

    def read_conversation(self):
        existing_messages = self._load_existing_messages()
        return existing_messages

    def clear_conversation(self):
        with open(self.file_path, 'w') as f:
            json.dump([], f)

    def _load_existing_messages(self):
        existing_messages = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                existing_messages = json.load(f)
        return existing_messages

    def json_initiate(self):

        # Default Setting
        messages = [
                {"role": "system", "content": "You are a helpful assistant"}
        ]

        file_path = self.save_conversation(messages)
        return file_path

    def user_store(self, message):
        message = [
            {"role": "user", "content": message}
        ]
        self.save_conversation(message)

    def ai_store(self, message):
        message = [
            {"role": "assistant", "content": message}
        ]
        self.save_conversation(message)