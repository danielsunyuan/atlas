import time

class ReadTranscription:

    def read_and_clear(self, transcription_file_path="transcription.txt"):
        try:
            with open(transcription_file_path, "r") as file:
                content = file.read()

            with open(transcription_file_path, "w") as file:
                file.write("")
                pass

            return content
        except FileNotFoundError:
            return None

if __name__ == "__main__":
    transcription_reader = ReadTranscription()

    while True:
        transcription = transcription_reader.read_and_clear()

        if transcription is not None and transcription.strip():
            # Process the transcription as needed
            # For example, you can send it to ChatGPT or perform other actions

            print(transcription)

        time.sleep(1)
