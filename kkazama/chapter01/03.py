import soundfile as sf
import numpy as np

# 3.WAVファイルの作成（ステレオ）
A = 1
f = 660
fs = 16000
sec = 3

t = np.arange(0, sec, 1 / fs)

x1, _ = sf.read("01.wav")
x2 = A * np.sin(2 * np.pi * f * t)

y = np.array([x1, x2])
y = y.T

sf.write("03.wav", y, fs, subtype="PCM_16")
