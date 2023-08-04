import numpy as np
import matplotlib.pyplot as plt


def make_wn(s, snr):
    v = np.sqrt(sum(s**2) / len(s) * 10 ** (-snr / 10))
    wn = np.random.normal(0, 1, len(s))
    return v * wn


if __name__ == "__main__":
    A = 1
    f = 440
    fs = 16000
    l = 1

    t = np.arange(0, l, 1 / fs)
    s = A * np.sin(2 * np.pi * f * t)
    wn = make_wn(s, 10)

    x = np.zeros((3, len(s)))
    for i in range(len(x)):
        x[i] = np.roll(s, i * 10) + wn  # np.roll(x,n)により配列xをnだけずらすことが可能（巡回シフト）

    plt.subplots_adjust(hspace=0.6)
    plot_range = 0.01
    for i in range(len(x)):
        plt.subplot(3, 1, i + 1)  # 正弦波の開始位置がずれるはず
        plt.plot(x[i])
        plt.title(f"x_{i+1}")
        plt.xlim([0, plot_range * 16000])
    plt.show()
