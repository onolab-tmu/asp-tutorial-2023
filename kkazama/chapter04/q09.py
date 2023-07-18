from scipy.signal import chirp
import numpy as np
import matplotlib.pyplot as plt
from q04 import stft

# チャープ信号
fs = 16000
sec = 1
t = np.linspace(0, 1, fs)
y = chirp(t, f0=100, f1=16000, t1=sec, method='linear')

L0 = 100
S0 = 50
Y_amp = []

for i in range(1, 5):
    L = i * L0
    S = i * S0
    w = np.hamming(L)
    Y = stft(y, L, S, w)
    Y_amp.append(np.abs(Y))

# プロット
fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(6, 10))

for i in range(4):
    p = ax[i].pcolormesh(Y_amp[i])
    ax[i].set_title("Amplitude spectrum")

plt.tight_layout()

plt.show()
