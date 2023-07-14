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
print("チャンネル数 : ", wav.getnchannels())
print("サンプルサイズ : ", wav.getsampwidth(),"バイト")
print("サンプリングレート : ", wav.getframerate())
print("フレーム数 : ", wav.getnframes())

print("\n", sf.info(filename))
