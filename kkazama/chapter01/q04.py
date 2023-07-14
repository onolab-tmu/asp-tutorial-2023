import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal

# 4.ホワイトノイズの生成
A = 1
sec = 3
fs = 16000

x = 2 * A * (np.random.rand(round(fs * sec)) - 0.5)

sf.write("04.wav", x, fs, subtype="PCM_16")
plt.plot(x)
plt.show()

sig_len_sample = fs * sec
t = (np.arange(sig_len_sample * 2 - 1) - sig_len_sample) / fs
col = signal.fftconvolve(x, x[::-1]) / sig_len_sample
plt.title("auto correlation")
plt.plot(t, col)
plt.show()
