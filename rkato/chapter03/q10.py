import numpy as np
import matplotlib.pyplot as plt


# 周波数応答
def frequency_responce(a, b, omega):
    a_sum = np.sum(a[1:] * np.exp(-1j * omega * np.arange(1, a.size)))
    b_sum = np.sum(b * np.exp(-1j * omega * np.arange(b.size)))

    H = b_sum / (1 + a_sum)

    return H


N = 10
a = np.zeros(10)
a[0] = 1
a[1] = -0.3
b = np.zeros(10)
b[0] = 0.4
fs = 16000
f = np.arange(N) / N * fs
omega = 2 * np.pi * f / fs
H = np.zeros(N, dtype=complex)
for i in range(N):
    H[i] = frequency_responce(a, b, omega[i])
plt.subplot(2, 1, 1)
plt.plot(omega, np.abs(H))
plt.subplot(2, 1, 2)
plt.plot(omega, np.angle(H))
plt.show()
