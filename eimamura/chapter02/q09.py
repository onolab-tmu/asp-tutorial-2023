"""2_9"""

import numpy as np
import matplotlib.pyplot as plt

def Hamming(w):
    N = len(w)
    for n in range(N):
        w[n] = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N-1))   
    return w

a = 1
f = 15000
fs = 16000
s = 3

t = np.arange(0, s, 1/fs)
y = a * np.sin(2*np.pi*f*t)

hamming = Hamming(y)
DFT_hamming = np.fft.fft(hamming)

print(DFT_hamming)

plt.plot(DFT_hamming)
plt.show()