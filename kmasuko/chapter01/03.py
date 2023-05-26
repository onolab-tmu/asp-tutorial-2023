import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

amp1 = 1
f1 = 440
amp2 = 1
f2 = 660
fs = 16000
sec = 3

filepath = "stereo.wav"
_format = "WAV"
subtype = "PCM_16"


t = np.arange(sec * fs) / fs

y1 = amp1 * np.cos(2 * np.pi * f1 * t)
y2 = amp2 * np.cos(2 * np.pi * f2 * t)

wave = np.array([y1, y2])
wave = wave.T

sf.write(filepath, wave, fs, format=_format, subtype=subtype)
