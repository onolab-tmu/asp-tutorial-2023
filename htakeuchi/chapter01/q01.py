import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import wave

# 1
A = 1
f = 440
fs = 16000
sec = 3

t = np.array([i / fs for i in range(sec * fs)])
x = A * np.sin(2 * np.pi * f * t)

plt.figure()
plt.plot(t,x)
plt.xlim(0, 1/f)   #t=0からt=1/440までを表示．
plt.xlabel("Time[s]")
plt.ylabel("Amplitude[-]")
plt.savefig("1_1.png")
