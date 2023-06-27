import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

# 1.正弦波の生成
A = 1
f = 440
fs = 16000
sec = 3
N = fs * sec

t = np.arange(fs * sec) / fs

xt = A * np.sin(2 * np.pi * f * t)
X = np.fft.fft(xt)

freq = np.arange(len(X)) / len(X) * fs
X_abs = np.abs(X)
X_abs_db = 20 * np.log10(X_abs)


# 確認
plt.subplot(2, 1, 1)
plt.plot(freq, X_abs_db)
plt.subplot(2, 1, 2)
plt.plot(freq, np.angle(X))
plt.xlim(430, 450)
plt.show()
