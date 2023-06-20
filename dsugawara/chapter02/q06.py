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
        t(ndarray):時間配列
        x(ndarray):正弦波
    """
    t = np.arange(0, sec, 1 / fs)
    # 正弦波
    x = A * np.sin(2 * np.pi * f * t)

    return t, x


if __name__ == "__main__":
    fs = 16000
    _, x = make_sine(A=1, f=440, sec=3, fs=fs)

    X = np.fft.fft(x)
    n = np.arange(len(X)) / len(X) * fs

    fig = plt.figure(figsize=[6.0, 4.0], rasterized=True)
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.stem(n, 20 * np.log10(np.abs(X)))
    ax1.set_title("amplitude")
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.stem(n, np.angle(X))
    ax2.set_title("phase")
    fig.tight_layout()
    plt.savefig("q06.pdf")
