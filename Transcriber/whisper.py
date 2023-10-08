import re
import subprocess

# Functions for Cleanup
def remove_escape_sequences(text):
        text = text.decode("utf-8")
        return re.sub(r'\x1b\[[0-9;]*[mK]', '', text).strip()

# Removes the soundfx
def remove_bracket_text(text):
            if not (re.search(r'\(.*\)|{.*}', text)):
                raise NotImplementedError

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
            print(text)
            write_transcription(text)


if __name__ == "__main__":
    run()