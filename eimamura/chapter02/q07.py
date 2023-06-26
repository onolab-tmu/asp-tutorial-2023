"""2_7"""

import numpy as np

def Hamming(w):
    N = len(w)
    w_hamming = np.zeros(N, dtype=complex)
    for n in range(N):
        w_hamming[n] = w[n] * (0.54 - 0.46 * np.cos(2 * np.pi * n / (N-1)))   
    return w_hamming