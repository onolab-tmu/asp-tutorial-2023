import numpy as np
import q01


def flame_div(L, S, x):
    """N点の信号xをフレーム分割
    Args:
        L(int): 窓幅
        S(int): シフト幅
        x(ndarray): 入力信号
    Return
        x_div: フレーム分割したx
    """
    x_pad = q01.padding(L, S, x)
    print(x_pad)
    N = len(x_pad)
    T = ((N - L) // S) + 1
    x_div = np.empty([T, L])
    for t in range(0, T):
        x_div[t] = x_pad[t * S : t * S + L]

    return x_div
