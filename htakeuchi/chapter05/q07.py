import numpy as np
import matplotlib.pyplot as plt
from q05 import stft
from q06 import x1, x2, x3, fs


"""合成窓を作成する関数"""


def synthesis_window(S, w):
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


"""ISTFTの関数"""


def istft(S, X, w):
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


if __name__ == "__main__":
    L = 1024
    S = 512
    w = np.hanning(L)

    X1 = stft(L, S, w, x1)
    X2 = stft(L, S, w, x2)
    X3 = stft(L, S, w, x3)

    F = X1.shape[0]
    T = X1.shape[1]

    f_list = np.array([i * fs / 2 / (F - 1) for i in range(F)])
    # print(f)

    tau1 = 0
    tau2 = 10 / fs
    tau3 = 20 / fs

    Y = np.zeros((F, T), dtype=complex)

    # f, tはインデクス．
    for f in range(F):
        w_f = np.array(
            [
                np.e ** (-2j * np.pi * f_list[f] * tau1),
                np.e ** (-2j * np.pi * f_list[f] * tau2),
                np.e ** (-2j * np.pi * f_list[f] * tau3),
            ]
        )
        w_f /= 3
        w_f_H = np.conj(w_f).reshape(1, 3)

        for t in range(T):
            x_ft = np.array([X1[f][t], X2[f][t], X3[f][t]]).reshape(3, 1)
            Y[f][t] = np.dot(w_f_H, x_ft)

    y = istft(S, Y, w)

    plt.figure()
    plt.plot(y)
    plt.xlabel("index")
    plt.ylabel("Amplitude")
    plt.savefig("5_7.png")

    plt.figure()
    plt.plot(y)
    plt.xlim(512, 672)  # 元信号の 0 ~ 0.01 秒に該当する箇所を表示
    plt.savefig("5_7_xlim.png")
