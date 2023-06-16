import numpy as np
import matplotlib.pyplot as plt


def make_noise(sec, fs):
    """白色雑音を生成
    Args:
        sec(int):信号長
        fs(int):サンプリング周波数
    Return:
        n(ndarray):白色雑音
        t(ndarray):時間配列
    """
    t = np.arange(0, sec, 1 / fs)
    n = np.random.randn(round(sec * fs))

    return n, t


if __name__ == "__main__":
    n, t = make_noise(sec=3, fs=16000)

    plt.figure(figsize=[6.0, 4.0])
    plt.title("white noise")
    plt.plot(t, n)
    plt.xlim(0, 0.1)
    plt.savefig("04.pdf")
