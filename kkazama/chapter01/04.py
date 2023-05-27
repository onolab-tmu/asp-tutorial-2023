import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# 4.ホワイトノイズの生成
A = 1
sec = 3
fs = 16000

x = 2 * A * (np.random.rand(round(fs * sec)) - 0.5)

sf.write("04.wav", x, fs, subtype="PCM_16")
plt.plot(x)
plt.show()
