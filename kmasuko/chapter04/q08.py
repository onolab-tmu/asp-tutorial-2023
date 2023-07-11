import numpy as np
import matplotlib.pyplot as plt
from q03 import stft
from q06 import istft


def istft2(S, X):
    """
    逆短時間フーリエ変換を計算
    Args:
        S(int):シフト幅
        X(ndarray):複素スペクトル
    Return:
        output(ndarray):信号
    """

    F, T = X.shape  # F:周波数ビン, T:フレームインデックス
    N = 2 * (F - 1)  # 窓長
    M = S * (T - 1) + N  # 出力信号長
    win = np.ones(N)
    output = np.zeros(M, dtype=float)  # 出力信号

    for t in range(T):
        z = np.fft.irfft(X[:, t])
        for i in range(N):
            output[t * S + i] = output[t * S + i] + win[i] * z[i]

    return output


if __name__ == "__main__":
    amp = 1
    f = 440
    fs = 16000
    sec = 0.1
    t = np.arange(int(fs * sec)) / fs
    x = np.cos(2 * np.pi * f * t)

    plt.figure()
    plt.plot(t, x)
    plt.show()

    win_len = 1000
    hop_len = 500
    win = np.hamming(win_len)
    X = stft(win_len, hop_len, win, x)
    x_istft = istft(hop_len, X)
    x_istft2 = istft2(hop_len, X)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(x_istft)

    plt.subplot(1, 2, 2)
    plt.plot(x_istft2)
    plt.show()

    plt.figure()
    plt.plot(x_istft2 - x_istft)
    plt.show()

    print(np.sum((x_istft - x_istft2) ** 2))
