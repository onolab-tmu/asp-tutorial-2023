import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


sin, Fs = sf.read("sin.wav")
L = int(len(sin))

sin_DFT = np.fft.fft(sin)
sin_DFT = sin_DFT / (L / 2)  # 正規化処理
power = 10 * np.log10((np.abs(sin_DFT)) ** 2)  # パワースペクトル
phase = np.angle(sin_DFT) * 180 / np.pi  # 位相スペクトル
freq = np.fft.fftfreq(L, d=1 / Fs)

# plt.plot(freq[0 : int(Fs / 2)], power[0 : int(Fs / 2)], marker="o")
fig, ax = plt.subplots()
ax.plot(freq, power, marker="o")
ax.set_xlabel("Frequency [Hz]", fontsize=20)
ax.set_ylabel("Power", fontsize=20)
ax.grid()
plt.show()

plt.plot(freq, phase, marker="o")
plt.xlabel("Frequency [Hz]", fontsize=20)
plt.ylabel("Phase", fontsize=20)
plt.show()


plt.plot(np.arange(0, len(freq)), freq, marker="o")
plt.show()
