import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import wave

# 1
A = 1
f = 440
fs = 16000
sec = 3

t = np.array([i / fs for i in range(sec * fs)])
s = A * np.sin(2 * np.pi * f * t)


#6
def SN(s, x):
    sum_s2 = 0
    sum_x2 = 0
    for i in range(len(x)):
        sum_s2 += s[i] ** 2
        sum_x2 += x[i] ** 2
    sn = 10 * np.log10(sum_s2 / sum_x2)
    return sn


#7
def add_noise(s, snr):
    size_s = len(s)
    noise = np.random.randn(size_s)
    noise = noise / np.sqrt(np.sum(noise ** 2))   # 正規化
    noise = noise * np.sqrt(np.sum(s ** 2))       # SN比は0になる．パワーがxと同じ．
    noise = noise * 10 ** (-snr/20)               # パワーを求める際に2乗することや，log10をとること，雑音noiseのパワーはlog10の中で分母であることから，10**(-snr/20)．
    return s + noise

#確認用
dB = 6
x = add_noise(s,dB)
n = x - s
print("SNR = ", SN(s,n))   # 雑音を重畳する前の信号と雑音とのSN比．6になるはず．