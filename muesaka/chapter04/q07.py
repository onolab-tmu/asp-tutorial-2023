import numpy as np
import q01
import q03
import q06

if __name__ == "__main__":
    A = 1
    f = 440
    sr = 16000
    sec = 0.1
    L = 1000
    S = 500

    t = np.arange(sr * sec) / sr
    x = A * np.sin(f * 2 * np.pi * t)
    w = np.hamming(L)

    X = q03.stft(x, w, L, S)
    x_hat = q06.istft(X, S)

    print(len(q01.zero_padding(x, L, S)), len(x_hat))  # ゼロ埋めとistftの長さを比較
    print(np.sum(np.square(x_hat[L - S : L - S + len(x)] - x)))  # 再構成誤差
