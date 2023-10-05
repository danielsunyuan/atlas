import time

class ReadTranscription:

    def read_and_clear(self, transcription_file_path="transcript.txt"):
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

            print(transcription)

        time.sleep(3)