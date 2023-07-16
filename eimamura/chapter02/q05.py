"""2_5"""

import numpy as np

def DFT(x):
    N = len(x)
    X = []
    for k in range(N):
        x1 = 0
        for n in range(N):
            a = 2 * np.pi * n * k / N
            x1 += x[n]*np.exp(-1j * a)
        X.append(x1)    
    return X

x = [1,0,0,0,0,0,0,0]
X1 = DFT(x)
X2 = np.fft.fft(x)

print(X1)
print(X2)