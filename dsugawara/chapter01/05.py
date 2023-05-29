import numpy as np
import matplotlib.pyplot as plt


def make_sine(A, f, sec, fs):
    """正弦波を生成
    Args:
        A(int):振幅
        f(int):周波数
        sec(int):信号長
        fs(int):サンプリング周波数
    Return:
        x(ndarray):正弦波
        t(ndarray):時間配列
    """
    t = np.arange(0, sec, 1 / fs)
    # 正弦波
    x = A * np.sin(2 * np.pi * f * t)

    return x, t


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
    fs = 16000
    sec = 3

    x, t = make_sine(A=1, f=440, sec=sec, fs=fs)
    n, _ = make_noise(sec=sec, fs=fs)

    y = x + n

    plt.figure(figsize=[6.0, 4.0])
    plt.title("440Hz + noise")
    plt.plot(t, y)
    plt.xlim(0, 0.03)
    plt.savefig("05.pdf")
