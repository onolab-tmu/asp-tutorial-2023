import numpy as np
import matplotlib.pyplot as plt


# 周波数応答
def frequency_responce(a, b, omega):
    a_sum = np.sum(a[1:] * np.exp(-1j * omega * np.arange(1, len(a))))
    b_sum = np.sum(b * np.exp(-1j * omega * np.arange(len(b))))

    H = b_sum / (1 + a_sum)

    return H


# 確認
N = 10
a = np.zeros(N)
a[0] = 1
b = np.zeros(N)
b[0] = 1

fs = 16000
f = np.arange(N * fs) / N
omega = 2 * np.pi * f / fs
H = np.zeros(N, dtype=complex)

for i in range(N):
    H[i] = frequency_responce(a, b, omega[i])

plt.subplot(2, 1, 1)
plt.plot(np.abs(H))
plt.subplot(2, 1, 2)
plt.plot(np.angle(H))
plt.show()
