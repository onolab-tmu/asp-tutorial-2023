import numpy as np
import matplotlib.pyplot as plt


def dft(x):
    """離散フーリエ変換
    Args:
        x(ndarray):信号
    Return:
        spec(ndarray):複素スペクトル
    """

    n = len(x)
    k = np.arange(n).reshape(1, -1)
    k_ = np.reshape(k, [-1, 1])

    exp = np.exp(-1j * 2 * np.pi * np.dot(k_, k) / n)
    spec = np.sum(x * exp, axis=1)

    return spec


def idft(spec):
    """逆離散フーリエ変換
    Args:
        spec(ndarray):複素スペクトル
    Return:
        x(ndarray):信号
    """

    n = len(spec)
    k = np.arange(n).reshape(1, -1)
    k_ = np.reshape(k, [-1, 1])

    exp = np.exp(1j * 2 * np.pi * np.dot(k_, k) / n)
    x = np.sum(spec * exp, axis=1) / n

    return x


if __name__ == "__main__":
    fs = 16000
    t = np.arange(fs) / fs
    f = 440
    x = np.cos(2 * np.pi * f * t)
    w = np.fft.fftfreq(len(x), 1/fs)
    x_dft = dft(x)

    plt.figure()
    plt.plot(np.abs(x_dft) / (fs / 2))
    plt.xlim(0, 500)
    plt.xlabel("k")
    plt.ylabel("|X[k]|")
    plt.show()

    plt.figure()
    plt.plot(np.angle(x_dft))
    plt.xlim(f-5, f+5)
    plt.xlabel("k")
    plt.ylabel("∠X[k]")
    plt.show()
