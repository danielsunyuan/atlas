import re
import json
import subprocess

# Functions for Cleanup
def remove_escape_sequences(text):
    text = text.decode("utf-8")
    return re.sub(r'\x1b\[[0-9;]*[mK]', '', text).strip()

def detect_brackets(text):
    # A function to detect whether text is an SFX or speech based on the presence of brackets
    if re.search(r'[\[\](){}]', text):
        return "sfx"
    else:
        return "speech"

def transcription_to_json(text):
    # Determine if it's speech or SFX and then write to JSON accordingly
    category = detect_brackets(text)

    # Split the text using '\r' and keep the last part
    parts = text.split('\r')
    high_confidence_transcription = parts[-1].strip()
    
    if high_confidence_transcription:
        transcription = {
            category: high_confidence_transcription
        }
        with open("transcript.json", "a") as file:
            json.dump(transcription, file, ensure_ascii=False)
            file.write("\n")


def run():
    # Execute C++ transcription code
    command = "bash stream.sh"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    while True:
        output = process.stdout.readline()

        # Remove empty outputs
        if output == b'' and process.poll() is not None:
            break

        elif output:
            all_text = remove_escape_sequences(output)
            transcription_to_json(all_text)

            # Live Transcription
            print(f"{all_text}")

if __name__ == "__main__":
    run()
