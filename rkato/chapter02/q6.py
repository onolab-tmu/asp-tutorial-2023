import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


# 1.正弦波の生成
A = 1
f = 440
Fs = 16000
sec = 3

N = Fs * sec
time = np.arange(Fs * sec) / Fs
sin=A*np.sin(2*np.pi*f*time)

sin_DFT = np.fft.fft(sin)
# sin_DFT = sin_DFT / (L / 2)  # 正規化処理
power = 10 * np.log10((np.abs(sin_DFT)) ** 2)  # パワースペクトル
phase = np.angle(sin_DFT) * 180 / np.pi  # 位相スペクトル
# freq = np.fft.fftfreq(sec, d=1 / Fs)
freq = np.arange(len(sin)) / len(sin) * Fs

#確認
plt.subplot(2,1,1)
plt.plot(freq, power, marker="o")
plt.xlabel("Frequency [Hz]", fontsize=20)
plt.ylabel("Power", fontsize=20)


plt.subplot(2,1,2)
plt.plot(freq, phase, marker="o")
plt.xlabel("Frequency [Hz]", fontsize=20)
plt.ylabel("Phase", fontsize=20)
plt.xlim(430, 450)
plt.show()

# plt.plot(freq, phase, marker="o")
# plt.xlabel("Frequency [Hz]", fontsize=20)
# plt.ylabel("Phase", fontsize=20)
# plt.xlim(430, 450)
# plt.show()

# #周波数軸を可視化
# plt.plot(np.arange(0, len(freq)), freq, marker="o")
# plt.show()
