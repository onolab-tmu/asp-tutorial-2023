import numpy as np


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


# 確認コード
amp = 1
fs = 16000
sig_len = 3
freq = 440

snr = 2
t = np.arange(fs * sig_len) / fs
sin_wave = amp * np.sin(2 * np.pi * freq * t)
mixture = Add_noise(sin_wave, snr)

white_noise = mixture - sin_wave
print(f"SNR: {SNR(sin_wave, white_noise)} (dB)")
