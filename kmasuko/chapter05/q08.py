import matplotlib.pyplot as plt
import numpy as np

from q03 import manifold_vector


def calc_beam_pattern(wf: np.ndarray, coords: np.ndarray, fs: float) -> np.ndarray:
    """ビームパターンを計算

    Args:
        wf (ndarray):ビームフォーマフィルタ (n_freq, n_channel)
        coords (ndarray):マイクアレイ座標 (n_mic, coord)
        fs (float):サンプリング周波数
    Return:
        ndarray:ビームパターン
    """

    thetas = np.arange(360)
    F = wf.shape[0]
    F_array = np.arange(F)
    F_array = F_array * fs / 2 / (F - 1)

    beam_pattern = []
    for i in range(F):
        temp = []
        for theta in thetas:
            temp.append(manifold_vector(coords, theta, F_array[i]))  # (n_theta, n_channel)
        psi = np.sum(wf.conj().T[:, i, None] * np.array(temp).T, axis=0)
        beam_pattern.append(psi)
    beam_pattern = np.array(beam_pattern)  # (n_freq, n_theta)

    return beam_pattern


def plot_beam_pattern(angle: np.ndarray, f_array: np.ndarray, beam_pattern: np.ndarray) -> None:
    """ビームパターンを描画

    Args:
        angle (ndarray):位相軸
        f_array (ndarray):周波数軸
        beam_pattern (ndarray):ビームパターン
    Return:
        None
    """

    X, Y = np.meshgrid(angle, f_array)
    plt.figure()
    plt.pcolormesh(X, Y, beam_pattern, cmap="gray")
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    n_mic = 3
    d = 0.05
    theta = 0
    coords = []
    for m in range(n_mic):
        coords.append([(m - (n_mic - 1) / 2) * d, 0, 0])
    coords = np.array(coords)

    F = 1000
    fs = 16000
    f_array = np.arange(F) * fs / 2 / (F - 1)
    w = []
    for f in f_array:
        w.append(manifold_vector(coords, theta, f))
    w = np.array(w) / n_mic

    beam_pattern = calc_beam_pattern(w, coords, fs)
    beam_pattern = 20 * np.log10(np.abs(beam_pattern))

    angle = np.arange(360)
    plot_beam_pattern(angle, f_array, beam_pattern)
