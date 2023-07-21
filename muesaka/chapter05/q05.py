import numpy as np
import q04
import my_functions


if __name__ == "__main__":
    sr = 16000  # サンプリング周波数[Hz]
    sec = 5  # 信号長[s]
    L = 512  # 窓幅[点]
    S = 256  # シフト幅[点]

    np.random.seed(1024)  # 1つめのノイズのシード
    noise1 = np.random.randn(sr * sec)
    np.random.seed(512)  # 2つめのノイズのシード
    noise2 = np.random.randn(sr * sec)

    w = np.hanning(L)  # ハン窓

    X1 = my_functions.stft(noise1, w, L, S)  # 1ch目
    X2 = my_functions.stft(noise2, w, L, S)  # 2ch目
    X = np.array([X1, X2])

    R = q04.calculate_spatial_correlation(X)  # 空間相関行列を計算

    print(R[100].real)  # R100の実部
