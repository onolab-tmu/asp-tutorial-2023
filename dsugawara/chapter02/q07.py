import numpy as np


def my_hamming(in_n):
    """n点のハミング窓を作成
    Args:
        n(int):窓の長さを決める点の数（信号長）
    Return:
        win(ndarray):ハミング窓
    """
    n = np.arange(0, in_n)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (len(n) - 1))

    return win
