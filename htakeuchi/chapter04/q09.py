import numpy as np
import matplotlib.pyplot as plt
import scipy
import soundfile as sf


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


"""9. 不確定性原理の確認"""
f0 = 100
f1 = 16000
fs = 16000
sec = 1

t = np.linspace(0, sec, fs)
# t = np.arange(sec*fs) / fs

x = scipy.signal.chirp(t, f0, sec, f1, method="linear")  # チャープ信号を生成

# チャープ信号をプロット
plt.figure()
plt.plot(t, x)
plt.savefig("4_9_chirp.png")

# チャープ信号をプロット(xlim)
plt.figure()
plt.plot(t, x)
plt.xlim(0.45, 0.55)
plt.savefig("4_9_chirp_xlim.png")

# チャープ信号をwavで保存
sf.write("4_9_chirp.wav", x, fs)

LandS = np.array([[100, 50], [200, 100], [400, 200], [800, 400]])

for i in range(len(LandS)):
    L = LandS[i][0]
    S = LandS[i][1]
    w = np.hamming(L)
    stft_x = stft(L, S, w, x)
    # print(stft_x.shape)
    plot_x = np.arange(stft_x.shape[1] + 1)  # 横軸はフレームインデクス
    plot_y = np.arange(stft_x.shape[0] + 1)  # 縦軸は周波数成分のインデクス

    plt.figure()
    # dB表記にしている
    plt.pcolormesh(plot_x, plot_y, 20 * np.log10(np.abs(stft_x)))
    # plt.pcolormesh(plot_x, plot_y, np.abs(stft_x))
    plt.colorbar()
    plt.savefig("4_9_spec_L" + str(L) + ".png")
