import numpy as np
import matplotlib as plt


# 入力したSN比に応じたノイズを重畳する関数
def adj_snr(s, snr):
    wn = np.random.randn(len(s))
    wn = wn / np.sqrt(np.sum(wn**2))
    wn = wn * np.sqrt(np.sum(s**2))
    wn = wn * 10 ** (-snr / 20)

    return s + wn


#####確認コード#####
A = 1
f = 440
Fs = 16000
L = 3
snr = 6
t = np.array([i / Fs for i in range(L * Fs)])
sinwave = A * np.sin(2 * np.pi * f * t)
sin_white = adj_snr(sinwave, snr)


def calc_SN(s, x):
    return 10 * np.log10(sum(s**2) / sum(x**2))


wn = sin_white - sinwave
print("6dBになるように調整した結果、SNは", calc_SN(sinwave, wn), "[dB]になった")
