import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


def ave_filter(x, n):
    """n点移動平均フィルタを適用
    Args:
        x(ndarray):信号
        n(int):移動平均
    Return:
        y(ndarray):
    """
    range = np.ones(n)
    y = np.convolve(x, range / n, mode="same")

    return y


if __name__ == "__main__":
    x, fs = sf.read("09.wav")
    n = 5
    y = ave_filter(x, n=n)
    t = np.arange(0, len(x) // fs, 1 / fs)

    plt.figure(figsize=[6.0, 4.0])
    plt.plot(t, x, label="original")
    plt.plot(t, y, label=f"{n}-point avarage")
    plt.xlim(0, 0.03)
    plt.legend(loc="lower right")
    plt.savefig("10.pdf")
