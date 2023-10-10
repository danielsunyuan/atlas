import sys
sys.path.append('GPT')
sys.path.append('Transcriber')
from Transcriber import reader as transcription
from Transcriber import whisper as whisper
from GPT import ChatGPT

import time


def main():

    # stream = whisper.run()

    # Create an instance of the ReadTranscription class
    reader = transcription.ReadTranscription()
    

    while True:
        # Call the read_and_clear method on the instance
        transcript = reader.read_and_clear()

        if transcript is not None:

            response = ChatGPT.ChatGPT(transcript)
            print(response)

        time.sleep(2) # Naive implementation of Automation

        """
            - Implement a way for sound effects to be part of the array of text (form context for AI)
            - Implement a VAD system to send only when detecting user
        """


if __name__ == "__main__":
    main()