import numpy as np
import q02


def my_stft(L, S, x, win):
    """短時間フーリエ変換
    Args:
        L(int): 窓幅
        S(int): シフト幅
        x(ndarray): 入力信号
        w(ndarray): 窓関数
    Return
        X: 変換後の信号
    """
    x_div = q02.flame_div(L, S, x)
    T = x_div.shape[0]
    X = np.empty([L // 2 + 1, T], dtype="complex")
    for t in range(0, T):
        X[:, t] = np.fft.rfft(x_div[t, :] * win)

    return X
