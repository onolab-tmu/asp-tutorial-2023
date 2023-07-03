import numpy as np
import matplotlib.pyplot as plt


def frequency_response(a, b, omega):
    H = np.zeros(omega.size, dtype=complex)
    for i in range(H.size):
        a_sum = np.sum(a[1:] * np.exp(-1j * omega[i] * np.arange(1, a.size)))  # aのsumを保存

        b_sum = np.sum(b * np.exp(-1j * omega[i] * np.arange(b.size)))  # bのsumを保存
        H[i] = b_sum / (1 + a_sum)  # 周波数応答

    return H


if __name__ == "__main__":
    N = 10
    a = np.zeros(N)
    a[0] = 1
    b = np.zeros(N)
    b[0] = 1

    fs = 16000
    f = np.arange(N) * fs / N
    omega = 2 * np.pi * f / fs
    H = frequency_response(a, b, omega)

    print("abs H:{}".format(np.abs(H)))
    print("angle H:{}".format(np.angle(H)))

    fix, ax = plt.subplots(2, 1, tight_layout=True)
    ax[0].plot(omega, np.abs(H))
    ax[0].set_title("abs H")
    ax[1].plot(omega, np.angle(H))
    ax[1].set_title("angle H")
    plt.show()


"""
abs H:[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
angle H:[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

"""
