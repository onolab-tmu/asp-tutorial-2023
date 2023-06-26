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

    Win = np.fft.fft(win)
    print(Win)

    plt.figure(figsize=[6.0, 4.0])
    plt.plot(t, 20 * np.log10(np.abs(Win)))
    plt.savefig("q09.pdf")
