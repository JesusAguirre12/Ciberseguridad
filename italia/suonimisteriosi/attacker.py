import wave
import numpy as np

with wave.open("audio.wav", "rb") as wav_file:
    channels = wav_file.getnchannels()
    sample_width = wav_file.getsampwidth()
    sample_rate = wav_file.getframerate()
    n_frames = wav_file.getnframes()
    raw_bytes = wav_file.readframes(n_frames)
    audio_samples = np.frombuffer(raw_bytes, dtype=np.int16)
