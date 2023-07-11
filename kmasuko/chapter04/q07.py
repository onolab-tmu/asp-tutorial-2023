import numpy as np
import matplotlib.pyplot as plt
from q01 import zero_pad
from q03 import stft
from q06 import istft


if __name__ == "__main__":
    amp = 1
    f = 440
    fs = 16000
    sec = 0.1
    t = np.arange(int(fs * sec)) / fs
    x = np.cos(2 * np.pi * f * t)

    plt.figure()
    plt.plot(t, x)
    plt.show()

    win_len = 1000
    hop_len = 500
    win = np.hamming(win_len)
    X = stft(win_len, hop_len, win, x)
    x_istft = istft(hop_len, X)
    x_origin = zero_pad(win_len, hop_len, x)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.title("est")
    plt.plot(x_istft)

    plt.subplot(1, 2, 2)
    plt.title("origin")
    plt.plot(x_origin)
    plt.show()

    print(np.sum((x_istft - x_origin) ** 2))  # 誤差の確認
