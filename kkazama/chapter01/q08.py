import numpy as np
import soundfile as sf


# SNRの計算
def SNR(s, x):
    snr = 10 * np.log10(np.sum(s * s) / np.sum(x * x))
    return snr

# ノイズの振幅調整
def Add_noise(s, snr):
    noise = np.random.rand(len(s))
    noise /= np.sqrt(np.sum(noise * noise))
    noise *= np.sqrt(np.sum(s * s))
    noise = noise / 10 ** (snr / 20)

    x = s + noise

    return x


x1, fs = sf.read("01.wav")

x = Add_noise(x1, snr=6)

sf.write("08.wav", x, fs, subtype="PCM_16")

# 確認コード
white_noise = x - x1
print(f"SNR: {SNR(x1, white_noise)} (dB)")
