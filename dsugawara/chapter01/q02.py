import numpy as np
import soundfile as sf


def make_sine(A, f, sec, fs):
    """正弦波を生成
    Args:
        A(int):振幅
        f(int):周波数
        sec(int):信号長
        fs(int):サンプリング周波数
    Return:
        x(ndarray):正弦波
        t(ndarray):時間配列
    """
    t = np.arange(0, sec, 1 / fs)
    # 正弦波
    x = A * np.sin(2 * np.pi * f * t)

    return x, t


if __name__ == "__main__":
    fs = 16000
    x, _ = make_sine(A=1, f=440, sec=3, fs=fs)

    sf.write(file="02.wav", data=x, samplerate=fs, subtype="PCM_16")
