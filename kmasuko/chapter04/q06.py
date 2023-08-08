import numpy as np
from q05 import syn_window


def istft(S, X):
    """
    逆短時間フーリエ変換を計算
    Args:
        S (int):シフト幅
        X (ndarray):複素スペクトル
    Return:
        output (ndarray):信号
    """

    F, T = X.shape  # F:周波数ビン, T:フレームインデックス
    N = 2 * (F - 1)  # 窓長
    M = S * (T - 1) + N  # 出力信号長
    hamm = np.hamming(N)
    win = syn_window(S, N, hamm)  # 合成窓
    output = np.zeros(M, dtype=float)  # 出力信号

    for t in range(T):
        z = np.fft.irfft(X[:, t])
        for i in range(N):
            output[t * S + i] = output[t * S + i] + win[i] * z[i]

    return output
