import numpy as np
import matplotlib.pyplot as plt
import q06


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


def optimal_win(S, win):
    """合成窓を作成
    Args:
        S(int): シフト幅
        win(ndarray): 窓
    Return:
        win_opt: 最適合成窓
    """

    L = win.size
    Q = L // S
    win_opt = np.empty(L)
    for l in range(0, L):
        sigma = 0
        for m in range(-(Q - 1), Q):
            if l - m * S >= 0 and l - m * S < L:
                sigma += win[l - m * S] ** 2
        win_opt[l] = win[l] / sigma

    return win_opt


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


def delayed_sum_beamformer(L, S, win, X):
    _, F, T = X.shape
    tau = np.array([0, 10 / fs, 20 / fs])
    w = np.empty([F, 3], dtype="complex")
    Y = np.empty([F, T], dtype="complex")
    for Fn in range(0, F):
        f = (fs / 2) / (F - 1) * Fn
        w[Fn, :] = 1 / 3 * np.exp(-2j * np.pi * f * tau)
        Y[Fn, :] = np.dot(np.conjugate(w[Fn, :].T), X[:, Fn, :])

    y = my_istft(S, Y, win)

    return y


if __name__ == "__main__":
    # 信号の生成
    A = 1.0
    fs = 16000
    sec = 1
    f = 440
    t = np.arange(0, fs * sec) / fs

    s = A * np.sin(2 * np.pi * f * t)
    noise = q06.make_noise(s, 10)

    x1 = s + noise
    s2 = np.pad(s, [10, 0])
    x2 = s2[0 : len(s2) - 10] + noise
    s3 = np.pad(s, [20, 0])
    x3 = s3[0 : len(s3) - 20] + noise

    L = 1024
    S = 512
    win = np.hanning(L)
    X1 = my_stft(L, S, x1, win)
    X2 = my_stft(L, S, x2, win)
    X3 = my_stft(L, S, x3, win)
    X = np.stack([X1, X2, X3])

    y = delayed_sum_beamformer(L, S, win, X)
    x1_pad = padding(L, S, x1)

    plt.figure(figsize=[6.0, 4.0])
    plt.plot(np.arange(0, sec * y.shape[0]) / fs, y)
    plt.plot(np.arange(0, sec * y.shape[0]) / fs, x1_pad)
    plt.xlim(0.02, 0.04)
    plt.savefig("q07.pdf")
