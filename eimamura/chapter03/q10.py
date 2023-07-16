import numpy as np
import matplotlib.pyplot as plt


def frequency_response(a, b, omega):
    N = a.size
    M = b.size
    bsum = 0
    asum = 0
    for m in range(M):
        bsum += b[m] * np.exp(-1j * omega * m)
    for n in range(1, N):
        asum += a[n] * np.exp(-1j * omega * n)
    h = bsum / (asum + 1)
    return h


N = 100
a = np.zeros(N)
a[0] = 1
a[1] = -0.3
b = np.zeros(10)
b[0] = 0.4

fs = 16000
f = np.arange(N) / N * fs
omega = 2 * np.pi * f / fs

H = np.zeros(N, dtype=complex)
for i in range(N):
    H[i] = frequency_response(a, b, omega[i])

plt.subplot(2, 1, 1)
plt.plot(omega, np.abs(H))
plt.subplot(2, 1, 2)
plt.plot(omega, np.angle(H))
plt.show()
