import numpy as np
import matplotlib.pyplot as plt
import q03

if __name__ == "__main__":
    A = 1
    f = 440
    sec = 0.1
    fs = 16000
    t = np.arange(0, sec, 1 / fs)
    x = A * np.sin(2 * np.pi * f * t)

    L = 1000
    S = L // 2
    win = np.hamming(L)
    X = q03.my_stft(L, S, x, win)

    fig = plt.figure(figsize=[6.0, 6.0])
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax1.pcolormesh(np.abs(X))
    ax2.pcolormesh(np.angle(X))
    ax1.set_title("amp")
    ax2.set_title("phase")
    plt.tight_layout
    plt.savefig("q04.pdf")
