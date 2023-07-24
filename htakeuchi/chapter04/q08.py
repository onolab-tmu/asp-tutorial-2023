import numpy as np
import matplotlib.pyplot as plt


"""1. 零詰めを行う関数"""


def zero_padding(L, S, x):
    y = np.pad(x, (L - S, L - S))  # 先頭と末尾にL-S個の零詰め．
    r = len(y) % S  # 信号yの長さをSで割った余り．
    y = np.pad(y, (0, S - r))  # 末尾にS-r個零詰めすることで最終的な信号の長さはSの倍数になる．
    return y


"""2. フレームを出力する関数"""


def frame_t(L, S, x):
    y = zero_padding(L, S, x)  # 零詰めしたx．

    # 以下Tを求める．「零詰め後の長さからLを引いた数」とSの商はシフトできる回数を表している．Tの定義より1を加えて調整している．
    T = (len(y) - L) // S + 1
    x_t = np.zeros((T, L))
    l = np.arange(L)
    for t in range(T):  # T*L の行列．要素数Lの配列がT個という意味．
        x_t[t] = y[t * S + l]
    return x_t


"""3. STFTを行う関数"""


def stft(L, S, w, x):
    x_t = frame_t(L, S, x)  # T*Lの行列．
    xw = x_t * w  # 各フレームに対して窓関数wをかける．
    # print(xw)
    stft_x = np.fft.rfft(xw)
    return stft_x.T  # 転置をとることで，(L/2+1)*Tの複素行列．


"""5. 合成窓を作成する関数"""


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


"""6. ISTFTの関数"""


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


"""8. 合成窓w_sのすべての要素を1にした際のISTFT関数"""

# w_sはすべてのnに対して1を持つから，6で作成したistftから窓の箇所を省略．


def istft_noWindow(S, X):
    F = X.shape[0]
    T = X.shape[1]
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    x = np.zeros(M)  # 出力信号を初期化
    z = np.fft.irfft(X.T)  # 転置してT*F行列にしたX.Tを逆DFTする．
    n = np.arange(N)  # インデックスの配列
    for t in range(T):
        x[t * S + n] += z[t]  # overlap add の計算
    return x


"""8. 合成窓の確認"""
A = 1
f = 440
fs = 16000
sec = 0.1
x = np.sin([2 * np.pi * f * i / fs for i in range(int(fs * sec))])

L = 1000
S = 500
w = np.hamming(L)  # 窓関数

stft_x = stft(L, S, w, x)  # 要素数(L/2 + 1)の配列がT個．

# 4の結果であるstft_xの逆短時間フーリエ変換を求める．
istft_stft_x = istft_noWindow(S, stft_x)

# 再構成誤差の和を求める
print("二乗誤差の和 : ", np.sum((zero_padding(L, S, x) - istft_stft_x) ** 2))

# サイズを確認．零詰めされた信号の長さである3000になるはず．
print("size of ISTFT(X) : ", len(istft_stft_x))

# すべての要素が1である矩形窓を用いてISTFTを求めたときの信号の最大値を表示．問題7と比較するため．
print("\nmax(ISTFT(X)) : ", max(istft_stft_x))


# 信号全体をプロット
plot_idx = np.arange(len(istft_stft_x))
plt.figure()
plt.plot(plot_idx, istft_stft_x)
# plt.xlim()
plt.savefig("4_8.png")

# 0でない箇所の1/440秒分をプロット．1周期分が表示されるはず．
plot_idx = np.arange(len(istft_stft_x))
plt.figure()
plt.plot(plot_idx, istft_stft_x)
# 横軸は時間ではなくインデックスであるから，1/440秒に対応するインデックス．L-Sだけ零詰めされているからその分を考慮．
plt.xlim(L - S, L - S + fs / f)
plt.savefig("4_8_xlim.png")


# 問題7で求めた逆短時間フーリエ変換
istft_stft_x_ = istft(S, stft_x, w)
# 7と8の差をプロット
plt.figure()
plt.plot(plot_idx, istft_stft_x - istft_stft_x_)
plt.ylim(0, 0.1)
plt.savefig("4_8_confirm.png")
