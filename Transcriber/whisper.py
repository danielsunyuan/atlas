import subprocess
import re

additional_info = """
        whisper_init_state: loading Core ML model from 'models/ggml-base.en-encoder.mlmodelc'
        whisper_init_state: first run on a device may take a while ...
        whisper_init_state: Core ML model loaded

        system_info: n_threads = 4 / 10 | AVX = 0 | AVX2 = 0 | AVX512 = 0 | FMA = 0 | NEON = 1 | ARM_FMA = 1 | F16C = 0 | FP16_VA = 1 | WASM_SIMD = 0 | BLAS = 1 | SSE3 = 0 | VSX = 0 | COREML = 1 |
    """


def run_whisper():

    #command = "./stream", "-m ./models/ggml-base.en.bin", "-f transcription.txt", "-t 8", "--step 500", "--length 5000"
    #command =  f"./transcritption/stream -m ./trancription/models/ggml-base.en.bin -tdrz --vad-thold 0.50{additional_info}"
    command = "./stream -m ./models/ggml-base.en.bin -tdrz --vad-thold 0.50"

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    with open("transcript.txt", "w") as transcription_file:
        pass

    # Function to remove escape sequences
    def remove_escape_sequences(text):
        text = text.decode("utf-8")
        return re.sub(r'\x1b\[[0-9;]*[mK]', '', text)
    
    def write_transcription(cleaned_text, file_path="transcript.txt"):
        with open(file_path, "w") as file:
                file.write(cleaned_text)


    # Read and print live transcriptions
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            text = remove_escape_sequences(output) 
            cleaned_text = text.strip()
            if cleaned_text:
                # Live Transcription
                print(cleaned_text)
                write_transcription(cleaned_text)


if __name__ == "__main__":
    run_whisper()