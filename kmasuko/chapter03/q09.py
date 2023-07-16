import numpy as np
import matplotlib.pyplot as plt
from q08 import frf


if __name__ == "__main__":
    N = 10
    length = 5
    a = np.zeros(length)
    a[0] = 1
    b = np.zeros(length) + 0.2

    fs = 16000
    f = np.arange(N) / N * fs
    omega = 2 * np.pi * f / fs
    H = np.zeros(len(omega), dtype=complex)

    for i in range(len(omega)):
        H[i] = frf(a, b, omega[i])

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(omega, np.abs(H))

    plt.subplot(1, 2, 2)
    plt.plot(omega, np.angle(H))
    plt.show()
