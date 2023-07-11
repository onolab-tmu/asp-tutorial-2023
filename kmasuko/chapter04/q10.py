import numpy as np
import matplotlib.pyplot as plt
from q01 import zero_pad
from q03 import stft


def stft_index(X, fs, S):
    """
    スペクトログラムの単位を変換
    Args:
        X(ndarray):スペクトログラム
        fs(int):サンプリング周波数
        S(int):シフト長
    Return:
        ff(ndarray):周波数ビン
        tt(ndarray):時間
    """

    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    ff = np.linspace(0, fs / 2, F)
    tt = (np.linspace(0, M, T) - (N - S)) / fs

    return ff, tt


if __name__ == "__main__":
    amp = 1
    f = 440
    fs = 16000
    sec = 0.1
    t = np.arange(int(fs * sec)) / fs
    x = np.cos(2 * np.pi * f * t)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(t, x)

    win_len = 1000
    hop_len = 500
    win = np.hamming(win_len)
    X = stft(win_len, hop_len, win, x)
    ff, tt = stft_index(X, fs, hop_len)
    x_pad = zero_pad(win_len, hop_len, x)
    t2 = (np.arange(len(x_pad)) - (win_len - hop_len)) / fs

    plt.subplot(1, 2, 2)
    plt.plot(t2, x_pad)
    plt.show()

    plt.figure()
    plt.pcolormesh(tt, ff, np.abs(X))
    plt.show()
