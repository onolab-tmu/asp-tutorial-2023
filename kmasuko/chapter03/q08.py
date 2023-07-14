import numpy as np
import matplotlib.pyplot as plt


def frf(a, b, omega):
    """
    周波数応答を計算
    Args:
        a(ndarray):係数
        b(ndarray):係数
        omega(double):正規化角周波数
    Return:
        H(double):周波数応答
    """

    a_sum = np.sum(a[1:] * np.exp(-1j * omega * np.arange(1, len(a))))
    b_sum = np.sum(b * np.exp(-1j * omega * np.arange(len(b))))

    H = b_sum / (1 + a_sum)

    return H


if __name__ == "__main__":
    length = 10
    a = np.zeros(length)
    a[0] = 1
    b = np.zeros(length)
    b[0] = 1

    fs = 16000
    f = np.arange(length) / length * fs
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
