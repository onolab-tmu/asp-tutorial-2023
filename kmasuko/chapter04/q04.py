import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from q03 import stft


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

    tt = np.linspace(0, 0.1, X.shape[0])
    ff = np.linspace(0, fs / 2, X.shape[1])
    print(X.shape)
    print(tt.shape)
    print(ff.shape)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.pcolormesh(tt, ff, np.abs(X).T)

    plt.subplot(1, 2, 2)
    plt.pcolormesh(tt, ff, np.angle(X).T)
    plt.show()
