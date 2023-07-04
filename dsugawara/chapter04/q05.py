import numpy as np
import matplotlib.pyplot as plt


def optimal_win(S, win):
    """合成窓を作成
    Args:
        S(int): シフト幅
        win(ndarray): 窓
    Return:
        win_s: 最適合成窓
    """
    L = win.size
    Q = L // S
    for l in range(0, L):
        sigma = 0
        for m in range(0, Q):
            sigma += win[l - m * S] ** 2
    win_s = win / sigma

    return win_s
