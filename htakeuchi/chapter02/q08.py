import numpy as np
import matplotlib.pyplot as plt

# 7
def Hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N-1))
    return w   


# 8
A = 1
f = 440
fs = 16000
sec = 3

t = np.array([i / fs for i in range(sec * fs)])
x = A * np.sin(2 * np.pi * f * t)

N = len(x)
w = Hamming(N)

x_w = x * w

plt.figure()
plt.plot(t, x_w)
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.savefig("2_8.png")
