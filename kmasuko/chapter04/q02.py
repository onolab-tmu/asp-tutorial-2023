import numpy as np
from q01 import zero_pad


def frame(L, S, x):
    """
    フレームを出力

    Args:
        L(int):窓長
        S(int):シフト長
        x(ndarray):入力信号
    Return:
        frames(ndarray):フレーム列
    """

    x = zero_pad(L, S, x)
    n_frame = int((len(x) - L) / S) + 1
    frames = []

    for t in range(n_frame):
        frames.append(x[t * S : t * S + L])

    frames = np.array(frames)

    return frames


if __name__ == "__main__":
    win_len = 6
    hop_len = 2
    x = np.array([1, 2, 3, 4, 5, 6])

    frames = frame(win_len, hop_len, x)

    print(frames)
