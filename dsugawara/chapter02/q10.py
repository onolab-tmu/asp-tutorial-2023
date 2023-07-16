import numpy as np
import matplotlib.pyplot as plt
import q07


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

    t, x = make_sine(A=1, f=440, sec=3, fs=16000)

    win = q07.my_hamming(len(x))

    X = np.fft.fft(x)
    Y = np.fft.fft(win)
    N = len(x)
    n = np.arange(N)
    Z = np.empty(0)
    for k in range(0, N):
        temp = np.sum(X[n] * Y[k - n])
        Z = np.append(Z, temp)
    z = np.fft.ifft(Z)

    plt.figure(figsize=[6.0, 4.0], rasterized=True)
    plt.stem(t, z)
    plt.savefig("q10.pdf")
