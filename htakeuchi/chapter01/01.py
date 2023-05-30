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
x = A * np.sin(2 * np.pi * f * t)

plt.figure()
plt.plot(t,x)
plt.xlim(0, 1/f)   #t=0からt=1/440までを表示．
plt.xlabel("Time[s]")
plt.ylabel("Amplitude[-]")
plt.savefig("1_1.png")


#2
filename = "1_2.wav"
_format = "WAV"
subtype = "PCM_16"
sf.write(filename, x, fs, format=_format, subtype=subtype)

wav = wave.open("1_2.wav", "rb")
print("\n1-2")
print("チャンネル数 : ", wav.getnchannels())
print("サンプルサイズ : ", wav.getsampwidth(),"バイト")
print("サンプリングレート : ", wav.getframerate())
print("フレーム数 : ", wav.getnframes())

print("\n", sf.info(filename))


#3
A = 1
f2 = 660
fs = 16000
sec = 3

t = np.array([i / fs for i in range(sec * fs)])
x2 = A * np.sin(2 * np.pi * f2 * t)

x3 = np.array([x,x2])
x3 = x3.T

# x3 = np.stack((sin_wave1, sin_wave2), axis=1)  # stereo

filename = "1_3.wav"
_format = "WAV"
subtype = "PCM_16"
sf.write(filename, x3, fs, format=_format, subtype=subtype)

wav = wave.open("1_3.wav", "rb")
print("\n1-3")
print("チャンネル数 : ", wav.getnchannels())
print("サンプルサイズ : ", wav.getsampwidth(),"バイト")
print("サンプリングレート : ", wav.getframerate())
print("フレーム数 : ", wav.getnframes())

print("\n", sf.info(filename))


#4
fs = 16000
sec = 3

t = np.array([i / fs for i in range(sec * fs)])
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



#5
y = x + noise
plt.figure()
plt.plot(t,y)
plt.xlabel("Time[s]")
plt.ylabel("Amplitude[-]")
plt.savefig("1_5.png")

# 確認用（解説）
plt.figure()
plt.title("Mixture")
plt.plot(t,y, label="Mixture")
plt.plot(t, x, marker=".", label="Sine wave")  # 確認用
plt.plot(t, noise, marker=".", label="White noise")  # 確認用
plt.xlabel("Time[s]")
plt.ylabel("Amplitude[-]")
plt.xlim(0,10 / fs)
plt.grid()
plt.legend()
plt.savefig("1_5_confirm.png")


#6
def SN(s, x):
    sum_s2 = 0
    sum_x2 = 0
    for i in range(len(x)):
        sum_s2 += s[i] ** 2
        sum_x2 += x[i] ** 2
    sn = 10 * np.log10(sum_s2 / sum_x2)
    return sn

# 確認用（解説）
print("\nSN(x,x) = ", SN(x,x), "dB")
print("SN(x, 10*x) = ", SN(x, 10*x), "dB")


#7
def add_noise(x, snr):
    size_x = len(x)
    noise = np.random.randn(size_x)
    noise = noise / np.sqrt(np.sum(noise ** 2))   # 正規化
    noise = noise * np.sqrt(np.sum(x ** 2))       # SN比は0になる．パワーがxと同じ．
    noise = noise * 10 ** (-snr/20)               # パワーを求める際に2乗することや，log10をとること，雑音noiseのパワーはlog10の中で分母であることから，10**(-snr/20)．
    print("\n1-7, 1-8 (6dB)")
    print("snr = ", SN(x,noise))   # 雑音を重畳する前の信号と雑音とのSN比．6になるはず．
    return x + noise


#8
snr = 6
y2 = add_noise(x,snr)
noise = y2 - x

filename = "1_8.wav"
_format = "WAV"
# subtype = "PCM_16"
subtype = "FLOAT"   #解説
sf.write(filename, y2, fs, format=_format, subtype=subtype)

# plt.figure()
# plt.plot(t,y2)
# plt.xlabel("Time[s]")
# plt.ylabel("Amplitude[-]")
# plt.savefig("1_8.png")


#9
data, samplerate = sf.read("1_8.wav")
print("\n1_8.wavのサンプリング周波数 : ", samplerate)

# 自分で作成．問題と意図が異なる．
# fs2 = 8000
# filename = "1_9.wav"
# _format = "WAV"
# subtype = "PCM_16"
# sf.write(filename, data, fs2, format=_format, subtype=subtype)

# data, samplerate = sf.read("1_9.wav")
# print("\n1_9.wavのサンプリング周波数 : ", samplerate)   # 確認用．samplerate=8となるはず．

# 解説
fs_down = 8000
step_down = int(fs // fs_down)
signal_down = (data-noise)[::step_down]
mixture_down = data[::step_down]
noise_down = mixture_down - signal_down
sf.write("1_9_2.wav", mixture_down, fs_down, format=_format, subtype=subtype)


#10
def MAF(x, M):
    y = np.zeros(len(x))
    for i in range(M, len(x)-M):
        y[i] = np.mean(x[i-M:i+M])
    return y

n = np.arange(len(mixture_down))
y3 = MAF(mixture_down, 2)        #mixture_downは元の信号．y3は5点移動平均フィルタを適用した信号．

plt.figure()
plt.subplot(1,2,1)
plt.plot(n[0:400],data[0:400])
plt.title("base")
plt.xlabel("Number[-]")
plt.ylabel("Amplitude[-]")
plt.subplot(1,2,2)
plt.plot(n[0:400],y3[0:400])
plt.title("5-MAF")
plt.xlabel("Number[-]")
plt.ylabel("Amplitude[-]")
plt.savefig("1_10.png")

print("\ninput SNR : ", SN(signal_down, noise_down))
print("output SNR : ", SN(signal_down, y3 - signal_down))

sf.write("1_10.wav", y3, fs_down, format=_format, subtype=subtype)