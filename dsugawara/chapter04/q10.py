import numpy as np
import matplotlib.pyplot as plt
import q03


def calc_axis(X, fs, S):
    """スペクトログラムの縦軸を周波数，横軸を時間に変換する
    Args:
        X(ndarray): スペクトログラム
        fs(int): サンプリング周波数
        S(int): シフト幅
    Returns:
        ax_f(ndarray): 縦軸（周波数）
        ax_t(ndarray): 横軸（時間）
    Memo:
        時間インデックスL-Sに対して0秒
        周波数インデックス0に対して0Hz
    """

    F = X.shape[0]
    T = X.shape[1]
    L = (F - 1) * 2

    axis_f = np.arange(0, F + 1) / F * (fs / 2)
    axis_t = (np.arange(0, T + 1) * S - (L - S)) / fs

    return axis_f, axis_t


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

    # plot
    freq, t = calc_axis(np.abs(X), fs, S)
    fig = plt.figure(figsize=[6.0, 6.0])
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax1.pcolormesh(t, freq, np.abs(X))
    ax2.pcolormesh(t, freq, np.angle(X))
    ax1.set_title("amp")
    ax2.set_title("phase")
    plt.tight_layout
    plt.savefig("q10.pdf")
