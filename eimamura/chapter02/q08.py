"""2_8"""

import numpy as np
import matplotlib.pyplot as plt

def Hamming(w):
    N = len(w)
    w_hamming = np.zeros(N, dtype=complex)
    for n in range(N):
        w_hamming[n] = w[n] * (0.54 - 0.46 * np.cos(2 * np.pi * n / (N-1)))   
    return w_hamming

a = 1
f = 440
fs = 16000
s = 3

t = np.arange(0, s, 1/fs)
y = a * np.sin(2*np.pi*f*t)

hamming = Hamming(y)
print(hamming)
plt.plot(hamming)
plt.show()