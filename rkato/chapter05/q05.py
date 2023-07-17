import numpy as np
from scipy import linalg
import librosa


def hermitian(arr):
    return np.conjugate(arr.T)


def calc_scm(X_ft):
    n_mic, F, T = np.shape(X_ft)
    # 空間相関行列の計算
    Rf = np.zeros((F, n_mic, n_mic), dtype=np.complex64)
    # xft = np.zeros((F, n_mic, T), dtype=np.complex64)
    for f in range(F):
        for t in range(T):
            xft = X_ft[:, f, t]
            Rf[f] += np.dot(xft.reshape(n_mic, 1), hermitian(xft.reshape(n_mic, 1)))
    return Rf / T


def main():
    # ==================================================================================
    # 設定変数
    variable = {
        "window_length": 512,  # STFT窓長
        "hop_length": 256,  # STFT窓遷移幅
    }
    # ==================================================================================
    # 白色雑音の作成
    A = 1.0  # 振幅
    sec = 5.0  # 信号の長さ s
    sf = 16000  # サンプリング周波数 Hz
    x = np.random.rand(round(sf * sec))  # ホワイトノイズの生成f
    white_noise = [x, x]
    white_noise2 = [np.random.rand(round(sf * sec)), np.random.rand(round(sf * sec))]
    n_mic = 2
    # スペクトログラムを計算
    X_ft = np.zeros((n_mic, 257, 311), dtype=np.complex64)
    X_ft2 = np.zeros((n_mic, 257, 311), dtype=np.complex64)
    for n in range(n_mic):
        X_ft[n] = librosa.stft(
            white_noise[n],
            n_fft=variable["window_length"],
            hop_length=variable["hop_length"],
            window="hann",
            center=False,
            dtype=None,
        )

    for n in range(n_mic):
        X_ft2[n] = librosa.stft(
            white_noise2[n],
            n_fft=variable["window_length"],
            hop_length=variable["hop_length"],
            window="hann",
            center=False,
            dtype=None,
        )

    print("元信号の配列構造:", np.shape(X_ft))
    Rf = calc_scm(X_ft)
    Rf2 = calc_scm(X_ft2)
    print("空間相関行列の配列構造:", np.shape(Rf))
    print()

    print("Rf100の実部:", Rf[101].real)
    print("Rf100の実部(左右違うノイズ):", Rf2[101].real)


if __name__ == "__main__":
    main()
