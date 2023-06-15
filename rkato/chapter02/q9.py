import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

sin, Fs = sf.read("sin.wav")
L = 3.0  # 信号は3秒
N = int(L * Fs)  # サンプル数の計算
num = np.arange(0, N, 1)
hamming = 0.54 - 0.46 * np.cos(2 * np.pi * num / (N - 1))

# #ハミング窓の波形を確認
# plt.plot(num, hamming)
# plt.xlabel("Sample_Number", fontsize=20)
# plt.ylabel("Signal", fontsize=20)
# plt.show()

hamming_DFT = np.fft.fft(hamming)
# ハミング窓のDFTを図示
 freq = np.fft.fftfreq(int(len(sin)), d=1 / Fs)
power = 10 * np.log10((np.abs(hamming_DFT)) ** 2)  # パワースペクトル
plt.plot(freqpower)
plt.xlabel("Sample_Number", fontsize=20)
plt.ylabel("Signal", fontsize=20)
plt.show()
