import time

class ReadTranscription:

    def read_and_clear(self, transcription_file_path="Transcriber/transcript.txt"):
        try:
            with open(transcription_file_path, "r") as file:
                lines = file.readlines()

                if len(lines) >=3:
                    content = ""
                    for line in lines[2:]:
                        print(line)
                        content += line

            return content
        except FileNotFoundError:
            raise FileNotFoundError

# Example Usage
if __name__ == "__main__":

    transcription_reader = ReadTranscription()

    while True:
        transcription = transcription_reader.read_and_clear()

        if transcription is not None and transcription.strip():
            print(transcription)

        time.sleep(3)