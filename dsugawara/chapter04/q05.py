import numpy as np
import matplotlib.pyplot as plt


def optimal_win(S, win):
    """合成窓を作成
    Args:
        S(int): シフト幅
        win(ndarray): 窓
    Return:
        win_opt: 最適合成窓
    """

    L = win.size
    Q = L // S
    win_opt = np.empty(L)
    for l in range(0, L):
        sigma = 0
        for m in range(-(Q - 1), Q):
            if l - m * S >= 0 and l - m * S < L:
                sigma += win[l - m * S] ** 2
        win_opt[l] = win[l] / sigma

    return win_opt
