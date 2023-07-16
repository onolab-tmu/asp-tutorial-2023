import numpy as np
import matplotlib.pyplot as plt


def calc_freq_resp(a, b, fs, N):
    f = np.arange(N) / N * fs
    omega = f * 2 * np.pi / fs
    H = np.zeros(len(omega), dtype=complex)
    for n in range(len(H)):
        sum_a, sum_b = 0.0 + 0.0j, 0.0 + 0.0j
        for k in range(len(b)):
            sum_b += b[k] * np.exp(-1j * omega[n] * k)
        for k in range(1, len(a)):
            sum_a += a[k] * np.exp(-1j * omega[n] * k)
        H[n] = sum_b / (1 + sum_a)
    return H, omega


a = np.array([1, -0.3])
b = np.array([0.4])
fs = 16000
N = 1000

H, omega = calc_freq_resp(a, b, fs, N)

plt.plot(omega, np.abs(H))
plt.xticks([0, np.pi / 2, np.pi, np.pi * 3 / 2, np.pi * 2], ["0", "π/2", "π", "3π/2", "2π"])
plt.show()
plt.plot(omega, np.angle(H))
plt.xticks([0, np.pi / 2, np.pi, np.pi * 3 / 2, np.pi * 2], ["0", "π/2", "π", "3π/2", "2π"])
plt.show()
