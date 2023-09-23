"""
Audio Module
For recording off the computer's microphone and to manipulate it into mp3
"""

import tempfile
import pyaudio
import wave
import os
from pydub import AudioSegment

# Choose your audio format, channels, rate, and chunk size
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 60

def audio_capture():

    # Initialize PyAudio and open a stream
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    # Record audio in chunks and append to frames
    print("Recording started. 'Ctrl C' to stop.")
    try:
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("\nRecording stopped.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    return audio, frames


def audio_file_create(audio, frames):

    # Create temporary files for WAV and MP3
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as wav_file:
        wav_file_path = wav_file.name

    # Save audio to a .wav file
    waveFile = wave.open(wav_file_path, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    # Convert WAV to MP3
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as mp3_file:
        mp3_file_path = mp3_file.name

        sound = AudioSegment.from_wav(wav_file_path)
        sound.export(mp3_file_path, format="mp3")

    return mp3_file_path

def audio_processing():

    audio, frames = audio_capture()

    return(audio_file_create(audio, frames))