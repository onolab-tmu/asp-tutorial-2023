import numpy as np
import soundfile as sf

# ノイズの振幅調整
def Add_noise(s, snr):
    noise = np.random.rand(len(s))
    # 正規化
    noise /= np.sqrt(np.sum(noise ** 2))
    # 元の雑音と求める雑音の比を乗算
    noise *= np.sqrt(np.sum(s ** 2)) / 10 ** (snr / 20)
    x = s + noise

    return x


x1, fs = sf.read("01.wav")

x = Add_noise(x1, snr=6)

sf.write("08.wav", x, fs, subtype="PCM_16")
