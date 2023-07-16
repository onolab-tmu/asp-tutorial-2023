import numpy as np
import q7
import matplotlib.pyplot as plt
import soundfile as sf

sin, Fs = sf.read("sin.wav")
L = 3.0  # 信号は3秒

sin_hamming = q7.calculate_hamming(sin)


t = np.arange(0, L, 1 / Fs)  # 0からLまで1/Fs刻みで準備
plt.plot(t, sin, label="Sinwave")
plt.plot(t, sin_hamming, label="Hamming_Sinwave")
plt.xlabel("time [s]", fontsize=20)
plt.ylabel("Signal", fontsize=20)
# plt.xlim(0, 200 / Fs)  # 拡大して見る
plt.show()
