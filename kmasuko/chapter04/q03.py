import numpy as np
from q02 import frame


def stft(L, S, win, x):
    """
    短時間フーリエ変換を実行

    Args:
        L(int):窓長
        S(int):シフト長
        win(ndarray):窓関数
        x(ndarray):入力信号
    Return:
        output(ndarray):複素数行列
    """

    frames = frame(L, S, x)
    output = []

    for t in range(len(frames)):
        frames[t] = frames[t] * win
        output.append(np.fft.rfft(frames[t]))

    output = np.array(output, dtype="complex")

    return output.T


if __name__ == "__main__":
    win_len = 4
    hop_len = 2
    win = np.hamming(win_len)
    x = np.array([1, 2, 3, 4, 5])

    X = stft(win_len, hop_len, win, x)

    print(X)
    print(X.shape)
    np.fft.fft
