import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft
import soundfile as sf

from q03 import manifold_vector
from q05 import spatial_corr


def calc_beam_former(a: np.ndarray) -> np.ndarray:
    """DSビームフォーマを計算

    Args:
        a (ndarray):アレイマニフォールドベクトル (n_mic, )
    Return:
        ndarray:ビームフォーマ
    """

    return a / (a.conj() @ a)


def calc_spatial_spectrum(X: np.ndarray, w: np.ndarray, f: int) -> np.ndarray:
    """空間スペクトルを計算

    Args:
        X (ndarray):空間相関行列 (n_mic, n_freq, n_frame)
        w (ndarray):ビームフォーマ (n_mic, )
        f (int):周波数ビンインデックス
    Return:
        ndarray:空間スペクトル
    """

    R = spatial_corr(X)
    P = w.conj() @ R[f, :, :] @ w

    return P


def conduct(coords: np.ndarray, theta: float, f: float, X: np.ndarray) -> np.ndarray:
    fs = 16000
    _, F, _ = X.shape
    F = np.arange(F) * fs / 2 / (F - 1)
    a = manifold_vector(coords, theta, F[f])
    w = calc_beam_former(a)

    return calc_spatial_spectrum(X, w, f)


if __name__ == "__main__":
    file = "signal.wav"
    x, fs = sf.read(file)

    n_mic = 3
    d = 0.05
    coord = []
    for m in range(n_mic):
        coord.append([(m - (n_mic - 1) / 2) * d, 0, 0])
    coord = np.array(coord)

    stft_args = {
        "fs": fs,
        "window": "hann",
        "nperseg": 1024,
        "noverlap": 512,
    }
    f, _, X = stft(x.T, **stft_args)

    thetas = np.arange(360)
    plt.figure(figsize=(12, 8))
    plt.subplots_adjust(hspace=0.6)
    for f in range(20, 30):
        P = [conduct(coord, theta, f, X) for theta in thetas]
        P = 20 * np.log10(np.abs(P))
        plt.subplot(3, 4, f - 19)
        plt.plot(thetas, P)
        plt.title(f"freq bin:{f}")
        plt.xlabel("theta [deg]")
    plt.subplots_adjust()
    plt.show()
