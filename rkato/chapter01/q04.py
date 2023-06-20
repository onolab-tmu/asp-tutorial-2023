import numpy as np
import matplotlib.pyplot as plt

Fs = 16000       #  サンプリング周波数の設定[Hz]
L = 3.0     #   信号長さ[s]

t = np.arange(0,L,1/Fs)# 0からLまで1/Fs刻みで準備
n_white = np.random.rand(round(Fs*L))


#####ノイズのスペクトルを確認#####
sig_len_sample = Fs * L
n_white_spec = np.fft.rfft(n_white)

power = 10* np.log10(np.abs(n_white_spec)**2)
freq = np.arange(sig_len_sample // 2 + 1)/ sig_len_sample * Fs
plt.title("White noise (Frequency domain)")
plt.plot(freq , power)
plt.ylabel("Power")
plt.xlabel("Freq.(Hz)")

plt.show()
