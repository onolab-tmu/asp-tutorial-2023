import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

a = 1
f = 440
fs = 16000
s = 3

t = np.arange(0, s, 1 / fs)
y = a * np.sin(2 * np.pi * f * t)

a2 = 1
f2 = 660
fs2 = 16000
s2 = 3

t2 = np.arange(0, s2, 1 / fs2)
y2 = a2 * np.sin(2 * np.pi * f2 * t2)
y1 = y
wave = np.stack((y1, y2), axis=1)

sf.write("1_3.wav", wave, fs2)
sf.info("1_3.wav")
