import time
import json

class ReadTranscription:

    def read_and_clear(self, transcription_file_path="Transcriber/transcript.txt"):
        try:
            with open(transcription_file_path, "r") as file:
                lines = file.readlines()

                # Read the 3rd line, because IDK why whisper.py writes 2 times?!
                if len(lines) >= 3:
                    content = ""
                    for line in lines[2:]:
                        print(line)
                        content += line

            return content
        except FileNotFoundError:
            raise FileNotFoundError
            
    def read_transcription_from_json(self, file_path="Transcriber/transcript.json"):
        transcriptions = []
        with open(file_path, "r") as file:
            for line in file:
                entry = json.loads(line)
                transcriptions.append(entry)
        return transcriptions


# Example Usage
if __name__ == "__main__":

    transcriptor = ReadTranscription()

    while True:

        # To read and extract elements from the JSON file "transcript.json"
        transcriptions = transcriptor.read_transcription_from_json()

        # You can now work with the transcriptions list
        for transcription in transcriptions:
            speech = transcription.get("speech")
            sfx = transcription.get("sfx")

        time.sleep(3)