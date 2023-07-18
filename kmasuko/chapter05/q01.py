import numpy as np


def straight_manifold_vector(d: float, M: int, theta: float, f: float, c: float = 334) -> np.ndarray:
    """直線状アレイマニフォールドベクトルを計算

    Args:
        d (float):アレイ間隔 [m]
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
    pos_vec = np.array([(m - (M - 1) / 2) * d, [0] * M, [0] * M])
    mani_vec = np.exp(1.0j * 2 * np.pi * f / c * direct_vec @ pos_vec)

    return mani_vec


if __name__ == "__main__":
    d = 0.05
    M = 3
    theta = 45
    f = 1000

    print(straight_manifold_vector(d, M, theta, f))
