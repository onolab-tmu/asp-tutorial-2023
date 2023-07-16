import numpy as np
import matplotlib.pyplot as plt

def Hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N-1))
    return w   


#確認用
N = 8
w = Hamming(N)

n = np.arange(N)
plt.figure()
plt.stem(n,w)
plt.savefig("2_7.png")

