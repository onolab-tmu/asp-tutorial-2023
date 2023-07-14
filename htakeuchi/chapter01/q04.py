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

plt.figure()
plt.plot(t,noise)
plt.xlabel("Time[s]")
plt.ylabel("Amplitude[-]")
plt.savefig("1_4.png")

# 確認用（解説）
white_noise_spec = np.fft.rfft(noise)
power = 10 * np.log10(np.abs(white_noise_spec) ** 2)
freq = np.arange(fs*sec // 2 + 1) / (fs*sec) * fs
plt.figure(9)
plt.title("White noise (Freqency domain)")
plt.plot(freq, power)
plt.ylabel("Power")
plt.xlabel("Freq. (Hz)")
plt.savefig("1_4_confirm.png")