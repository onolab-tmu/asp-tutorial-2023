import numpy as np
from matplotlib import pyplot as plt

# 1.正弦波の生成
A = 1
f = 440
fs = 16000
sec = 3

t = np.arange(fs * sec) / fs

x1 = A * np.sin(2 * np.pi * f * t)

# 確認コード
plt.xlim(0, 1 / f)
plt.plot(t, x1)
plt.show()
