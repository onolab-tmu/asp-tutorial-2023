import numpy as np


def SNR(s, x):
    snr = 10 * np.log10(np.sum(s * s) / np.sum(x * x))
    return snr


# 確認コード
A1 = 1
A2 = 10
f = 440
fs = 16000
sig_len = 3
t = np.arange(fs * sig_len) / fs
s = A1 * np.sin(2 * np.pi * f * t)
x = A2 * np.sin(2 * np.pi * f * t)

print(f"SNR: {SNR(s, s)} (dB)")
print(f"SNR: {SNR(s, x)} (dB)")
