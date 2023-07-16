import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import wave

# 1
A = 1
f = 440
fs = 16000
sec = 3

t = np.array([i / fs for i in range(sec * fs)])
s = A * np.sin(2 * np.pi * f * t)


#4
noise = np.random.randn(len(t))   # 標準正規分布のほうで作成する．
# noise = np.random.rand(len(t))   # こっちは一様分布．ホワイトノイズは正規分布（上）のほうがよさそう．


#5
x = s + noise
plt.figure()
plt.plot(t,x)
plt.xlabel("Time[s]")
plt.ylabel("Amplitude[-]")
plt.savefig("1_5.png")

# 確認用（解説）
plt.figure()
plt.title("Mixture")
plt.plot(t, x, label="Mixture")
plt.plot(t, s, marker=".", label="Sine wave")  # 確認用
plt.plot(t, noise, marker=".", label="White noise")  # 確認用
plt.xlabel("Time[s]")
plt.ylabel("Amplitude[-]")
plt.xlim(0,10 / fs)
plt.grid()
plt.legend()
plt.savefig("1_5_confirm.png")