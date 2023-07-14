import numpy as np


###### ハン窓を作成する関数の作成  ######
def calculate_hamming(x):
    N = len(x)  # 信号の点数を取得
    x_hamming = np.zeros(N, dtype=complex)
    for k in range(0, N):
        x_hamming[k] = x[k] * (0.54 - 0.46 * np.cos(2 * np.pi * k / (N - 1)))

    return x_hamming
