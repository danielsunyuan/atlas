class Transcription:
    def __init__(self):
        # Initialize any necessary setup for your chosen ASR service or library
        # e.g., establish a connection, configure settings, etc.
        raise NotImplementedError

    def send_for_transcription(self, audio_chunk):
        # Replace this with the actual code to send audio for transcription
        # You should implement this based on the chosen ASR service or library
        print("Sending audio chunk for transcription...")
        raise NotImplementedError

    def process_audio_stream(self, audio_stream):
        try:
            while True:
                audio_chunk = audio_stream.read_audio_chunk()
                self.send_for_transcription(audio_chunk)
        except KeyboardInterrupt:
            print("Transcription stopped.")
