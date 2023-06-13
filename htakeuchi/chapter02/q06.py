import numpy as np
import matplotlib.pyplot as plt

A = 1
f = 440
fs = 16000
sec = 3

t = np.array([i / fs for i in range(sec * fs)])
x = A * np.sin(2 * np.pi * f * t)

N = len(x)
k = np.arange(N)
f = np.array([i * fs / N for i in range(N)])

x_DFT = np.fft.fft(x)

x_DFT_amp = np.abs(x_DFT)
x_DFT_pha = np.angle(x_DFT)

plt.figure()
plt.stem(k,x_DFT_amp)
plt.title("Amplitude Spectrum")
plt.xlabel("k [-]")
plt.ylabel("Amplitude [-]")
plt.savefig("2_6_amp.png")

# 横軸を周波数にする場合
# plt.figure()
# plt.stem(f,x_DFT_amp)
# plt.title("Amplitude Spectrum")
# plt.xlabel("Frequency [Hz]")
# plt.ylabel("Amplitude [-]")
# plt.savefig("2_6_amp.png")

x_DFT_amp_db = 20 * np.log10(np.abs(x_DFT))
plt.figure()
plt.stem(k,x_DFT_amp_db)
plt.title("Amplitude Spectrum (db)")
plt.xlabel("k [-]")
plt.ylabel("Amplitude [db]")
plt.savefig("2_6_amp_db.png")

plt.figure()
plt.stem(k,x_DFT_pha)
plt.title("Phase Spectrum")
plt.xlabel("k [-]")
plt.ylabel("Amplitude [-]")
plt.savefig("2_6_pha.png")

plt.figure()
plt.stem(f,x_DFT_pha)
plt.title("Phase Spectrum")
plt.xlim(435,445)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [-]")
plt.savefig("2_6_pha.png")
