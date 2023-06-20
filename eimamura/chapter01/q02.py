import numpy as np
import soundfile as sf

a = 1
f = 440
fs = 16000
s = 3

t = np.arange(0, s, 1 / fs)
y = a * np.sin(2 * np.pi * f * t)

sf.write("1_2.wav", y, fs)

sf.info("1_2.wav")
