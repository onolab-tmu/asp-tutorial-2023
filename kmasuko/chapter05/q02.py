import numpy as np


def circular_manifold_vector(r: float, M: int, theta: float, f: float, c: float = 334) -> np.ndarray:
    """円状アレイマニフォールドベクトルを計算

    Args:
        r (float):アレイ半径 [m]
        M (int):マイク数
        theta (float):音源方向
        f (float):周波数 [Hz]
        c (float):音速 [m/s] (default = 334)
    Returns:
        ndarray:アレイマニフォールドベクトル
    """

    theta = np.deg2rad(theta)
    m = np.arange(M)
    direct_vec = np.array([np.sin(theta), np.cos(theta), 0])
    pos_vec = np.array([r * np.sin(2 * np.pi * m / M), r * np.cos(2 * np.pi * m / M), [0] * M])
    mani_vec = np.exp(1.0j * 2 * np.pi * f / c * direct_vec @ pos_vec)

    return mani_vec


if __name__ == "__main__":
    r = 0.05
    M = 3
    theta = 45
    f = 1000

    print(circular_manifold_vector(r, M, theta, f))
