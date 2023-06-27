import numpy as np
import matplotlib.pyplot as plt


def defference_equation_recursion(x):
    N = x.size
    y = np.zeros(N)

    for n in range(N):
        y[n] = recursion(x, n)

    return y


def recursion(x, n):
    if n == 0:
        return 0.4 * x[n]
    else:
        return 0.3 * recursion(x, n - 1) + 0.4 * x[n]


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
b = defference_equation_recursion(a)

fs = 16000
f = np.arange(N) / N * fs
omega = 2 * np.pi * f / fs

H = np.zeros(N, dtype=complex)
for i in range(N):
    H[i] = frequency_response(a, b, omega[i])

plt.subplot(2, 1, 1)
plt.plot(np.abs(H))
plt.subplot(2, 1, 2)
plt.plot(np.angle(H))
plt.show()
