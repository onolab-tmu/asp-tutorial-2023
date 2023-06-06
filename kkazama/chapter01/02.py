import soundfile as sf
import numpy as np

# 1.正弦波の生成
A = 1
f = 440
fs = 16000
sec = 3

t = np.arange(fs * sec) / fs

x1 = A * np.sin(2 * np.pi * f * t)

# 2.WAVファイルの作成
sf.write("01.wav", x1, fs, subtype="PCM_16")

# 確認コード
print(sf.info("01.wav"))
