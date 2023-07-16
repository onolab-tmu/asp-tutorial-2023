"""2_4"""

import numpy as np
import matplotlib.pyplot as plt

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
y = [0,1,2,3,4,5,6,7]
X = DFT(x)

amplitude = np.abs(X)
phase = np.angle(X)

plt.plot(amplitude)
plt.ylabel('amplitude')
plt.show()
plt.plot(phase)
plt.ylabel('phase')
plt.show()