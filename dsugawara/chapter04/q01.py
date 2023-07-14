import numpy as np


def padding(L, S, x):
    """N点の信号xにゼロ詰めを行う
    Args:
        L(int): 窓幅
        S(int): シフト幅
        x(ndarray): 入力信号
    Return
        x_pad: ゼロ詰め後の信号
    """

    x_pad = np.pad(x, (L - S, L - S))
    temp = S - len(x_pad) % S
    x_pad = np.pad(x_pad, (0, temp))
    return x_pad
