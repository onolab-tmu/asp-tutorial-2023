import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import q7

sin, Fs = sf.read("sin.wav")
L = 3.0  # 信号は3秒
N = int(L * Fs)
n = np.arange(0, N, 1)  # 0からLまで1/Fs刻みで準備
hamming = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))

#####正弦波信号のDFT、hamming窓のDFTを計算#####
sin_DFT = np.fft.fft(sin)
hamming_DFT = np.fft.fft(hamming)

# #信号長確認
# print(len(sin_DFT))
# print(len(hamming_DFT))

#####巡回畳み込みの計算 ######
conv = np.zeros(N, dtype=complex)
conv_ifft = np.zeros(N, dtype=complex)

k = np.arange(0, N, 1)  # 0からLまで1/Fs刻みで準備
for num in range(0, N):
    conv[k] += sin_DFT[num] * hamming_DFT[k - num]

conv_ifft = np.fft.ifft(conv)

sin_hamming = q7.calculate_hamming(sin)
t = np.arange(0, L, 1 / Fs)  # 0からLまで1/Fs刻みで準備
plt.plot(t, sin_hamming, label="Hamming_Sinwave")
plt.plot(t, conv_ifft, label="Hamming_convolution")
plt.xlabel("time", fontsize=20)
plt.ylabel("Signal", fontsize=20)
plt.show()
