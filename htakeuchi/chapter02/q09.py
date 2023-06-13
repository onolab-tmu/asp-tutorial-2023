import numpy as np
import matplotlib.pyplot as plt

# 7
def Hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N-1))
    return np.round(w, 5)

# 9
N = 48000
k = np.arange(N)
w = Hamming(N)

w_DFT = np.fft.fft(w)

w_DFT_db = 20 * np.log10(np.abs(w_DFT))

w_DFT_amp = np.abs(w_DFT)
w_DFT_pha = np.angle(w_DFT)

plt.figure()
plt.stem(k,w_DFT_amp)
plt.title("Amplitude Spectrum")
plt.xlabel("k [-]")
plt.ylabel("Amplitude [-]")
plt.savefig("2_9_amp.png")

plt.figure()
plt.stem(k,w_DFT_db)
plt.title("Amplitude Spectrum (db)")
plt.xlabel("k [-]")
plt.ylabel("Amplitude [db]")
plt.savefig("2_9_amp_db.png")

plt.figure()
plt.stem(k,w_DFT_pha)
plt.title("Phase Spectrum")
plt.xlabel("k [-]")
plt.ylabel("Amplitude [-]")
plt.savefig("2_9_pha.png")

