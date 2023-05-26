import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

amp = 1
f = 440
fs = 16000
sec = 3

filepath = "monaural.wav"
_format = "WAV"
subtype = "PCM_16"


t = np.arange(sec * fs) / fs

y = amp * np.cos(2 * np.pi * f * t)

sf.write(filepath, y, fs, format=_format, subtype=subtype)
