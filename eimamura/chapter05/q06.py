import numpy as np
import matplotlib.pyplot as plt


def calculate_amplitude_from_snr(s, snr):
    a = np.linalg.norm(s)
    x = np.random.randn(round(len(s)))
    x = a * x / (10 ** (snr / 20) * np.linalg.norm(x))
    return x


if __name__ == "__main__":
    snr = 10
    s = 1
    fs = 16000
    a = 1
    f = 440

    t = np.arange(0, s, 1 / fs)
    y = a * np.sin(2 * np.pi * f * t)

    s1 = a * np.sin(2 * np.pi * f * t)
    s2 = np.hstack((np.zeros(10), s1[:-10]))
    s3 = np.hstack((np.zeros(20), s1[:-20]))

    white_noise = calculate_amplitude_from_snr(y, snr)

    x1 = s1 + white_noise
    x2 = s2 + white_noise
    x3 = s3 + white_noise

    plt.plot(x1, label="x1")
    plt.plot(x2, label="x2")
    plt.plot(x3, label="x3")
    plt.xlim(0, 0.01 * fs)
    plt.legend(["x1[n]", "x2[n]", "x3[n]"])
    plt.show()
