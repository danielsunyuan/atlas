import pyaudio

class AudioCapture:
    def __init__(self, rate=44100, chunk_size=1024, channels=1):
        self.rate = rate
        self.chunk_size = chunk_size
        self.channels = channels

        # Initialize PyAudio
        self.p = pyaudio.PyAudio()

    def start_capture(self):
        # Open an audio stream for capture
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )

    def stop_capture(self):
        # Stop the audio stream and terminate PyAudio
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def read_audio_chunk(self):
        # Read and return an audio chunk
        return self.stream.read(self.chunk_size)
