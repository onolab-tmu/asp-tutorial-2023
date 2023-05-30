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


#2
filename = "1_2.wav"
_format = "WAV"
subtype = "PCM_16"
sf.write(filename, x, fs, format=_format, subtype=subtype)

wav = wave.open("1_2.wav", "rb")

print("チャンネル数 : ", wav.getnchannels())
print("サンプルサイズ : ", wav.getsampwidth(),"バイト")
print("サンプリングレート : ", wav.getframerate())
print("フレーム数 : ", wav.getnframes())

print("\n", sf.info(filename))