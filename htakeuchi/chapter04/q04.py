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


"""4. STFTの確認"""
A = 1
f = 440
fs = 16000
sec = 0.1
x = np.sin([2 * np.pi * f * i / fs for i in range(int(fs * sec))])

# 信号xの確認用．
print("xのサイズ : ", len(x))
time = np.array([i / fs for i in range(int(fs * sec))])  # 横軸
plt.figure()
plt.plot(time, x)
plt.xlim(0, 1 / 440)  # 1周期分プロットされていれば正しい（可能性が高い）と判断できる．
plt.savefig("sin_440.png")

L = 1000
S = 500
w = np.hamming(L)  # 窓関数

y = zero_padding(L, S, x)  # q01と同じ．
print("\nyのサイズ : ", len(y))

x_t = frame_t(L, S, x)
print("\nx_tのサイズ : ", x_t.shape)

stft_x = stft(L, S, w, x)  # 要素数(L/2 + 1)の配列がT個．
print("\nstft_xのサイズ (L/2+1, T) : ", stft_x.shape)
# print("\n", stft_x)
# print("\n", np.abs(stft_x))
# print("\n", np.angle(stft_x))

T = (len(y) - L) // S + 1  # 「零詰め後の長さからLを引いた数」とSの商はシフトできる回数を表している．Tの定義より1を加えて調整している．
t_plot = np.arange(T)
f_plot = np.array([fs * i / L for i in range(int(L / 2) + 1)])

print(len(t_plot))
print(len(f_plot))
# pcolormeshの第3引数のサイズは，(len(f_plot), len(t_plot))になる必要がある．
# よって，転置をとる．ただし，関数stftに戻り値ですでに転置している場合は必要ない．
print(np.abs(stft_x).shape)

plt.figure()
plt.pcolormesh(t_plot, f_plot, np.abs(stft_x))
plt.xlabel("Frame Index")
plt.ylabel("Frequency [Hz]")
cbar = plt.colorbar()
cbar.ax.set_ylabel("Amplitude")
plt.savefig("4_4_amp.png")

plt.figure()
plt.pcolormesh(t_plot, f_plot, np.angle(stft_x))
plt.xlabel("Frame Index")
plt.ylabel("Frequency [Hz]")
# plt.ylim(430, 450)
cbar = plt.colorbar()
cbar.ax.set_ylabel("Phase [rad]")
plt.savefig("4_4_pha.png")


"""解説"""
plt.figure()
plt.pcolormesh(t_plot, f_plot, np.cos(np.angle(stft_x)))
plt.xlabel("Frame Index")
plt.ylabel("Frequency [Hz]")
cbar = plt.colorbar()
cbar.ax.set_ylabel("cos")
plt.savefig("4_4_cos_pha.png")

plt.figure()
plt.pcolormesh(t_plot, f_plot, np.sin(np.angle(stft_x)))
plt.xlabel("Frame Index")
plt.ylabel("Frequency [Hz]")
cbar = plt.colorbar()
cbar.ax.set_ylabel("sin")
plt.savefig("4_4_sin_pha.png")
