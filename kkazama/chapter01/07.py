import numpy as np

# ノイズの振幅調整
def Add_noise(s, snr):
    noise = np.random.rand(len(s))
    noise /= np.sqrt(np.sum(noise * noise))
    noise *= np.sqrt(np.sum(s * s))
    noise = noise * 10 ** (snr / 20)

    x = s + noise

    return x
