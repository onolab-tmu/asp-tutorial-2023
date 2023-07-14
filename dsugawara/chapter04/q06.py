import numpy as np
import q05


def my_istft(S, X, win):
    """逆短時間フーリエ変換
    Args:
        S(int): シフト幅
        X(ndarray): 入力信号
        win(ndarray): 窓関数
    Return:
        x: 変換後の信号
    """
    F = X.shape[0]
    T = X.shape[1]
    N = 2 * (F - 1)
    M = S * (T - 1) + N

    x = np.zeros(M)
    z = np.empty([T, N])
    for t in range(0, T):
        z[t, :] = np.fft.irfft(X[:, t])
        x[t * S : t * S + N] = x[t * S : t * S + N] + win * z[t, :]

    return x
