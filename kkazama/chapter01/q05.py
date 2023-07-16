import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

fs = 16000
sec = 3

t = np.arange(fs * sec) / fs

x1, _ = sf.read(file="01.wav")
x2, _ = sf.read(file="04.wav")

x = x1 + x2

plt.plot(t, x, label="Mixture")
plt.plot(t, x1, label="Sin wave") # 確認
plt.plot(t, x2, label="White noise") # 確認
plt.xlim(0, 10 / fs)
plt.legend()
plt.show()
