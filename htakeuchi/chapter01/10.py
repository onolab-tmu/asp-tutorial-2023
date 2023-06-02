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

filename = "1_8.wav"
_format = "WAV"
subtype = "FLOAT"
sf.write(filename, x, fs, format=_format, subtype=subtype)

#9
mixture, samplerate = sf.read("1_8.wav")   # mixtureは正弦波とホワイトノイズの混合信号

fs_down = 8000
step_down = int(fs // fs_down)
signal_down = (mixture - n)[::step_down]   # 雑音の分を除いて間引き
mixture_down = mixture[::step_down]   # 雑音含む信号の間引き
noise_down = mixture_down - signal_down   # 間引きした信号のうち，雑音の分


#10
def MAF(x, M):   # M点移動平均．5点の場合はM=5．
    y = np.zeros(len(x))
    for i in range(int(M/2), len(x)-int(M/2)):
        y[i] = np.mean(x[i-int(M/2):i+int(M/2)+1])
    return y

t_down = np.arange(len(mixture_down))
mixture_down_5p_MA = MAF(mixture_down, 5)        #mixture_downは元の信号．y3は5点移動平均フィルタを適用した信号．

plt.figure()
plt.subplot(1,2,1)
plt.plot(t_down, mixture_down)
plt.title("base")
plt.xlabel("Number[-]")
plt.ylabel("Amplitude[-]")
plt.subplot(1,2,2)
plt.plot(t_down, mixture_down_5p_MA)
plt.title("5-MAF")
plt.xlabel("Number[-]")
plt.ylabel("Amplitude[-]")
plt.savefig("1_10.png")

print("input SNR : ", SN(signal_down, noise_down))
print("output SNR : ", SN(signal_down, mixture_down_5p_MA - signal_down))

filename = "1_10.wav"
_format = "WAV"
subtype = "FLOAT"
sf.write(filename, mixture_down_5p_MA, fs_down, format=_format, subtype=subtype)

plt.figure()
plt.title("5-point moving average")
plt.plot(t_down, mixture_down, label="Noisy")
plt.plot(t_down, mixture_down_5p_MA, label="Enhanced")
# plt.xlim(0, 100 / fs)  # 確認
plt.legend()
plt.savefig("1_10_confirm.png")
