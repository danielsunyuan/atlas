import time
import json

class ReadTranscription:
            
    def read_transcription_from_json(self, file_path="Transcriber/transcript.json"):
        transcriptions = []
        try:
            with open(file_path, "r") as file:
                for line in file:
                    entry = json.loads(line)
                    transcriptions.append(entry)
            return transcriptions
        except FileNotFoundError:
            raise FileNotFoundError

    def clear_transcription_json(self, file_path="Transcriber/transcript.json"):
        with open(file_path, "w") as file:
            file.truncate(0)

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
            if speech is not None:
                print(speech)

        
        # After processing the data, you can clear the JSON file
        transcriptor.clear_transcription_json()

        time.sleep(3) # Temporary