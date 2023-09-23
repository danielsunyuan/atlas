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

    def json_initiate(self, agent_tone: str = None):
        if agent_tone is None:
            messages = [
                {"role": "system", "content": "You are a helpful assistant"}
            ]
        else:
            messages = [
                {"role": "system", "content": agent_tone}
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


class FileManager:
    def __init__(self, directory_path):
        self.conversations_dir = get_conversations_path(directory_path)

    def rename_json(self, old_filename, new_filename):
        # Find and rename the selected conversation to new name
        old_filepath = os.path.join(self.conversations_dir, old_filename)
        new_filepath = os.path.join(self.conversations_dir, new_filename)

        if not old_filename.endswith('.json'):
            raise ValueError("The old filename must be a JSON file.")

        if not new_filename.endswith('.json'):
            raise ValueError("The new filename must have a .json extension.")

        if os.path.exists(new_filepath):
            raise FileExistsError("A file with the new filename already exists.")

        os.rename(old_filepath, new_filepath)
        print(f"File '{old_filename}' has been renamed to '{new_filename}' in the directory '{self.conversations_dir}'.")

    def list_conversations(self):
        # Find all JSON files in the conversations directory
        json_files = [file for file in os.listdir(self.conversations_dir) if file.endswith('.json')]

        if not json_files:
            print("No conversation files found.")
        else:
            print("Available conversation files:")
            for idx, json_file in enumerate(json_files, start=1):
                print(f"{idx}. {json_file}")

    def delete_conversation(self, conversation_name):
        conversation_path = os.path.join(self.conversations_dir, conversation_name)
        if conversation_path:
            try:
                os.remove(conversation_path)
                print(f"Conversation '{conversation_name}' deleted.")
            except OSError as e:
                print(f"Error deleting conversation '{conversation_name}': {str(e)}")
        else:
            print(f"Conversation '{conversation_name}' not found.")
    
    def delete_all_conversations(self):
        for filename in os.listdir(self.conversations_dir):
            file_path = os.path.join(self.conversations_dir, filename)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"Conversation '{filename}' deleted.")
            except OSError as e:
                print(f"Error deleting conversation '{filename}': {str(e)}")

    def select_conversation(self, conversation_name):
        conversation_path = os.path.join(self.conversations_dir, conversation_name)
        existing_messages = self.load_conversation(conversation_path)

        if conversation_path:
            print('.................................')
            self.print_chat(existing_messages)
            print(f"Conversation '{conversation_name}' selected.")
        else:
            print(f"Conversation '{conversation_name}' not found.")


    def load_conversation(self, conversation_path):
        existing_messages = []
        if os.path.exists(conversation_path):
            with open(conversation_path, 'r') as f:
                existing_messages = json.load(f)
                return existing_messages


    def print_chat(self, messages):
        for message in messages:
            role = message["role"]
            content = message["content"]

            if role == "system":
                print(f"SYSTEM: {content}")
            elif role == "user":
                print(f"USER: {content}")
            elif role == "assistant":
                print(f"ASSISTANT: {content}")
            print()

