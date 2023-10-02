import subprocess
import re

# ./stream -m ./models/ggml-base.en.bin -t 8 --step 500 --length 5000

def run_whisper():
    #command = "./stream", "-m ./models/ggml-base.en.bin", "-f transcription.txt", "-t 8", "--step 500", "--length 5000"
    command = "./stream -m ./models/ggml-base.en.bin -f transcription.txt -tdrz --vad-thold 0.40"

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    with open("transcription.txt", "w") as transcription_file:
        pass

    transcription = []

    # Function to remove escape sequences
    def remove_escape_sequences(text):
        text = text.decode("utf-8")
        return re.sub(r'\x1b\[[0-9;]*[mK]', '', text)

    # Read and print live transcriptions
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            text = remove_escape_sequences(output) 
            cleaned_text = text.strip()
            if cleaned_text:
                print("Live Transcription:", cleaned_text)

                # Append the transcription to the buffer
                transcription.append(cleaned_text)

if __name__ == "__main__":
    # Run the C++ code to capture the streaming transcription
    run_whisper()