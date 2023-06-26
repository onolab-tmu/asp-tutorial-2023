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


#6
def SN(s, x):
    sum_s2 = 0
    sum_x2 = 0
    for i in range(len(x)):
        sum_s2 += s[i] ** 2
        sum_x2 += x[i] ** 2
    sn = 10 * np.log10(sum_s2 / sum_x2)
    return sn


#7
def add_noise(s, snr):
    size_s = len(s)
    noise = np.random.randn(size_s)
    noise = noise / np.sqrt(np.sum(noise ** 2))   # 正規化
    noise = noise * np.sqrt(np.sum(s ** 2))       # SN比は0になる．パワーがxと同じ．
    noise = noise * 10 ** (-snr/20)               # パワーを求める際に2乗することや，log10をとること，雑音noiseのパワーはlog10の中で分母であることから，10**(-snr/20)．
    return s + noise


#8
dB = 6
x = add_noise(s,dB)   #SN比が6dBになるようにホワイトノイズを付加した信号
n = x - s

#9
mixture, samplerate = sf.read("1_8.wav")   # mixtureは正弦波とホワイトノイズの混合信号
print("1_8.wavのサンプリング周波数 : ", samplerate)

# 解説
fs_down = 8000
step_down = int(fs // fs_down)
signal_down = (mixture - n)[::step_down]   # 雑音の分を除いて間引き
mixture_down = mixture[::step_down]   # 雑音含む信号の間引き
noise_down = mixture_down - signal_down   # 間引きした信号のうち，雑音の分

filename = "1_9.wav"
_format = "WAV"
subtype = "FLOAT"
sf.write("1_9.wav", mixture_down, fs_down, format=_format, subtype=subtype)

t_down = np.array([i / fs_down for i in range(sec * fs_down)])

plt.figure()
plt.title("Downsample")
plt.plot(t, mixture, marker=".", label="Raw")
plt.plot(t_down, mixture_down, marker="o", label="Downsampled")
plt.xlim(0, 10 / fs)
plt.legend()
plt.savefig("1_9.png")

print("1_9.wavのサンプリング周波数 : ", sf.read(filename)[1])
