"""2_3"""

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

def IDFT(X):
    N = len(X)
    x = []
    for n in range(N):
        X1 = 0
        for k in range(N):
            a = 2 * np.pi * k * n / N
            X1 += X[k]*np.exp(1j * a)
        X1 = 1/N*X1
        x.append(X1)    
    return x

x = [1,0,0,0,0,0,0,0]
y = [0,1,2,3,4,5,6,7]
X = DFT(x)
x = IDFT(X)
plt.bar(y,x)
plt.show()
print(x)