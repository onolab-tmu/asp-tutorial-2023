import numpy as np
import soundfile as sf


def calc_snr(x1, x2):
    """信号長の等しい 2 個の信号のSN比を計算
    Args:
        x1(ndarray):信号1
        x2(ndarray):信号2
    Return:
        snr(double):SN比
    """

    snr = 10 * np.log(np.sum(x1**2) / np.sum(x2**2))

    return snr


if __name__ == "__main__":
    x1, _ = sf.read("02.wav")
    x2, _ = sf.read("02.wav")
    snr = calc_snr(x1, x2)
    print(snr)
