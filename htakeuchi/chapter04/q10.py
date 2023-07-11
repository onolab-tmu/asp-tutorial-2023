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


"""10. スペクトログラムの縦軸と横軸の単位をそれぞれ周波数と秒に変換する関数"""


def unit_conversion(spec, fs, S):
    F = spec.shape[0]  # L/2 + 1
    L = 2 * (F - 1)
    # f_plot : 周波数で表される縦軸
    f_plot = np.array([fs * i / L for i in range(F)])

    T = spec.shape[1]
    # specは先頭に L-S だけ零詰めした信号をSTFTしたものだから，対応する秒の初期値は以下のt0．
    # specの時間軸におけるインデクス [0, 1, ..., T] に対応する秒は [t0, t0 + S/fs, ... , t0 + (T-1)*S/fs]．
    # 詳しくは， t0 = ( L/2 + (S - L) ) / fs である．L/2はフレームの中心．
    t0 = (S - L / 2) / fs
    # t_plot : 秒で表される横軸．
    t_plot = np.array([t0 + i * S / fs for i in range(T)])

    return t_plot, f_plot


"""10. インデクスと物理量の対応関係の確認"""
A = 1
f = 440
fs = 16000
sec = 0.1
x = np.sin([2 * np.pi * f * i / fs for i in range(int(fs * sec))])


L = 1000
S = 500
w = np.hamming(L)  # 窓関数


stft_x = stft(L, S, w, x)  # 要素数(L/2 + 1)の配列がT個．


t_plot, f_plot = unit_conversion(stft_x, fs, S)

# 確認用
print("t_plot [s] : \n", t_plot)
print("\nf_plot [Hz] : \n", f_plot)


plt.figure()
plt.pcolormesh(t_plot, f_plot, np.abs(stft_x))
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
cbar = plt.colorbar()
cbar.ax.set_ylabel("Amplitude")
plt.savefig("4_10_amp.png")

plt.figure()
plt.pcolormesh(t_plot, f_plot, np.angle(stft_x))
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
cbar = plt.colorbar()
cbar.ax.set_ylabel("Phase [rad]")
plt.savefig("4_10_pha.png")
