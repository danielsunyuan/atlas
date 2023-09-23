from audio_capture import AudioCapture
from transcription import Transcription  # Import the Transcription class

# Create instances of AudioCapture and Transcription classes
audio_capture = AudioCapture()
transcription = Transcription()

# Start capturing audio
audio_capture.start_capture()

# Start the transcription process
try:
    transcription.process_audio_stream(audio_capture)
except KeyboardInterrupt:
    print("Transcription stopped.")

# Stop audio capture when done
audio_capture.stop_capture()
