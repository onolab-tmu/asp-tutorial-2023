import numpy as np
from q04 import spatial_correlation_matrix
import matplotlib.pyplot as plt


"""零詰めを行う関数"""


def zero_padding(L, S, x):
    y = np.pad(x, (L - S, L - S))  # 先頭と末尾にL-S個の零詰め．
    r = len(y) % S  # 信号yの長さをSで割った余り．
    y = np.pad(y, (0, S - r))  # 末尾にS-r個零詰めすることで最終的な信号の長さはSの倍数になる．
    return y


"""フレームを出力する関数"""


def frame_t(L, S, x):
    y = zero_padding(L, S, x)  # 零詰めしたx．

    # 以下Tを求める．「零詰め後の長さからLを引いた数」とSの商はシフトできる回数を表している．Tの定義より1を加えて調整している．
    T = (len(y) - L) // S + 1
    x_t = np.zeros((T, L))
    l = np.arange(L)
    for t in range(T):  # T*L の行列．要素数Lの配列がT個という意味．
        x_t[t] = y[t * S + l]
    return x_t


"""STFTを行う関数"""


def stft(L, S, w, x):
    x_t = frame_t(L, S, x)  # T*Lの行列．
    xw = x_t * w  # 各フレームに対して窓関数wをかける．
    # print(xw)
    stft_x = np.fft.rfft(xw)
    return stft_x.T  # 転置をとることで，(L/2+1)*Tの複素行列．


if __name__ == "__main__":
    fs = 16000
    sec = 5
    np.random.seed(0)
    n1 = np.random.randn(fs * sec)
    n2 = np.random.randn(fs * sec)

    L = 512  # 窓幅
    S = 256  # シフト幅
    w = np.hanning(L)  # ハニング窓

    # ハニング窓の確認
    t = np.arange(len(w))
    plt.figure()
    plt.plot(t, w)
    plt.savefig("hanning.png")

    N1 = stft(L, S, w, n1)
    N2 = stft(L, S, w, n2)
    # print(N1.shape, N2.shape)

    N = np.stack([N1, N2])  # 2*512*314 にする．空間相関行列を求める関数の引数におけるM*F*Tにあたる．
    print("\nN.shape : ", N.shape)

    R = spatial_correlation_matrix(N)
    print("\nR.shape : ", R.shape)
    print("\nR[100] : \n", R[100].real)
