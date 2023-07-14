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
    A = 1
    sec = 3
    fs = 16000

    x1, _ = make_sine(A=A, f=440, sec=sec, fs=fs)
    x2, _ = make_sine(A=A, f=660, sec=sec, fs=fs)
    x = np.array([x1, x2]).T

    sf.write(file="03.wav", data=x, samplerate=fs)
