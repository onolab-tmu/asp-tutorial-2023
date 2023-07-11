import numpy as np


"""5. 合成窓を作成する関数"""


def synthesis_window(S, w):
    """
    S : シフト幅
    w : 分析窓
    w_s : 解析窓
    """
    L = len(w)
    l = np.arange(L)
    Q = int(L / S)

    # 窓関数におけるインデックス0未満とL以上を作成．ただし，末尾にのみpaddingする．
    w_ = np.pad(w, (0, S * (Q - 1)))
    deno = np.zeros(L)  # 分母の配列．長さはL．
    for m in range(1 - Q, Q):
        idx = l - m * S  # 負の値でもOK．w_の末尾に0をpaddingしてある．
        deno += w_[idx] ** 2
    w_s = w / deno
    return w_s


"""6. ISTFTの関数"""


def istft(S, X, w):
    """
    S : シフト幅
    X : 入力信号
    w : 合成幅
    """
    F = X.shape[0]
    T = X.shape[1]
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    x = np.zeros(M)  # 出力信号を初期化
    z = np.fft.irfft(X.T)  # 転置してT*F行列にしたX.Tを逆DFTする．
    w_s = synthesis_window(S, w)  # 最適合成窓
    n = np.arange(N)  # インデックスの配列
    for t in range(T):
        x[t * S + n] += w_s * z[t]  # overlap add の計算
    return x
