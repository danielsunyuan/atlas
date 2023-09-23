import os
from scripts import audio, conversation, tts
from scripts.AI import OPENAI

if __name__ == "__main__":

    # initialise the application
    conversation.clear_conversation()
    conversation.json_initiate()
    user_input = input("Press ENTER to start recording: ")

    while True:

        if user_input.lower() == 'exit':
            break

        # Audio Module ------------------------------------------
        audio_file_path = audio.audio_processing()
        transcript = OPENAI.whisper(audio_file_path)
        os.remove(audio_file_path)

        # Storage Module ----------------------------------------
        print('transcript = ' + transcript)
        conversation.user_store(transcript)
        convo = conversation.read_conversation()

        # GPT 3.5 API -------------------------------------------
        print('sending to GPT')
        response = OPENAI.chatGPT(convo)
        conversation.ai_store(response)
        print(response)

        # Voice Response Module ---------------------------------
        tts.os_speech(response)

        user_input = input("Enter 'exit' to finish or press ENTER to continue: ")
        if user_input.lower() == 'exit':
            break