import numpy as np
import q02


def stft(x, w, L, S):
    x_split = q02.split_frame(x, L, S)  # フレーム分割
    T = x_split.shape[0]  # サイズ
    X = np.zeros((L // 2 + 1, T), dtype="complex")  # (L/2 + 1) * Tのサイズ

    for t in range(T):
        X[:, t] = np.fft.rfft(x_split[t] * w)  # XのTの要素ごとに計算

    return X


if __name__ == "__main__":
    x = np.array([0, 1, 1, 1, 0])
    L = 4
    S = 2
    w = np.hamming(L)

    print(stft(x, w, L, S))
