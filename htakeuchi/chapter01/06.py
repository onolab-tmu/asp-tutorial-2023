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

# 確認用（解説）
print("\nSN(s,s) = ", SN(s,s), "dB")   # 0dB
print("SN(10*s, s) = ", SN(10*s, s), "dB")   # 20dB