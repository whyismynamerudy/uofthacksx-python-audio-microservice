import wave
import numpy as np

# open wave file

def get_amplitdue(file):
    with wave.open(file, 'r') as f:
        # read frames
        frames = f.readframes(-1)
        # convert to numpy array
        audio = np.frombuffer(frames, dtype=np.int16)
        # calculate average amplitude
        average_amplitude = np.mean(np.abs(audio))
        # convert to dB
        average_amplitude_dB = 20 * np.log10(average_amplitude)
        print(average_amplitude_dB)