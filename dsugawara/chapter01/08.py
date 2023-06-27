import numpy as np
import soundfile as sf


def mixing_noise(x, snr):
    """SN 比を任意の値に設定できるようにホワイトノイズの振幅を調整
    Args:
        x(ndarray):元信号
        snr(double):任意のSN比
    Return:
        y(ndarray):ホワイトノイズを重畳した信号
    """

    noise = np.random.randn(len(x))
    noise = noise / np.sqrt(np.sum(noise**2))
    noise = noise * np.sqrt(np.sum(x**2))
    noise = noise * (10 ** (-snr / 20))

    y = x + noise

    return y


if __name__ == "__main__":
    x, fs = sf.read("02.wav")

    y = mixing_noise(x, snr=6)

    sf.write(file="08.wav", data=y, samplerate=fs)
