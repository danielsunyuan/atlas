import re
import json
import subprocess

# Functions for Cleanup
def remove_escape_sequences(text):
        text = text.decode("utf-8")
        return re.sub(r'\x1b\[[0-9;]*[mK]', '', text).strip()

# Removes the Soundfx 
"""
    TODO: Have the SFX within a JSON along with transcripted words to add context for AI
"""
def check_bracketed(text):
    # Use regular expressions to find and remove bracketed text
    text_without_brackets = re.sub(r'\[[^\]]*\]|\([^\)]*\)|\{[^\}]*\}', '', text)
    return True

# Write to Transcript.txt
def write_transcription(cleaned_text, file_path="transcript.txt"):
        with open(file_path, "w") as file:
                cleaned_text.strip()
                file.write(cleaned_text)


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
            text = remove_escape_sequences(output)

            # Live Transcription
            print(f"{text}")
            write_transcription(text)


if __name__ == "__main__":
    run()