import numpy as np


def padding(L, S, x):
    """N点の信号xにゼロ詰めを行う
    Args:
        L(int): 窓幅
        S(int): シフト幅
        x(ndarray): 入力信号
    Return
        x_pad: ゼロ詰め後の信号
    """

    x_pad = np.pad(x, (L - S, L - S))
    temp = S - len(x_pad) % S
    x_pad = np.pad(x_pad, (0, temp))
    return x_pad


def flame_div(L, S, x):
    """N点の信号xをフレーム分割
    Args:
        L(int): 窓幅
        S(int): シフト幅
        x(ndarray): 入力信号
    Return
        x_div: フレーム分割したx
    """
    x_pad = padding(L, S, x)
    N = len(x_pad)
    T = ((N - L) // S) + 1
    x_div = np.empty([T, L])
    for t in range(0, T):
        x_div[t] = x_pad[t * S : t * S + L]

    return x_div


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
    x_div = flame_div(L, S, x)
    T = x_div.shape[0]
    X = np.empty([L // 2 + 1, T], dtype="complex")
    for t in range(0, T):
        X[:, t] = np.fft.rfft(x_div[t, :] * win)

    return X


def scm(X):
    """空間相関行列（spatial correation matrix）を求める
    Args:
        X (ndarray): 複素数行列
    Return:
        R: 空間相関行列
    """
    M, F, T = X.shape

    R = np.empty([F, M, M], dtype="complex")
    x = np.empty([F, M, T], dtype="complex")
    for f in range(0, F):
        for m in range(0, M):
            x[f, m] = X[m, f]
    for f in range(0, F):
        R[f] = np.dot(x[f], np.conjugate(x[f].T)) / T
    return R


if __name__ == "__main__":
    X1 = np.array([[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]])
    X2 = np.array([[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]])
    X = np.array([X1, X2])

    print(scm(X))


if __name__ == "__main__":

    A = 1.0
    fs = 16000
    sec = 5

    nA = A * np.random.randn(round(fs * sec))
    nB = A * np.random.rand(round(fs * sec))

    L = 512  # 窓長
    S = 256  # シフト幅
    win = np.hanning(L)  # 窓関数

    nA_stft = my_stft(L, S, nA, win)
    nB_stft = my_stft(L, S, nB, win)

    R = scm(np.array([nA_stft, nB_stft]))

    print(R[100].real)
