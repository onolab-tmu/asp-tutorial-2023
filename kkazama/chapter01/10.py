import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

x, _ = sf.read("09.wav")

# 移動平均
y = np.convolve(x, np.ones(5), mode="valid") / 5

plt.subplot(2, 1, 1)
plt.plot(x)
# plt.xlim(0, 0.03)
plt.subplot(2, 1, 2)
plt.plot(y)
# plt.xlim(0, 0.03)
plt.show()
