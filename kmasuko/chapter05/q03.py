import numpy as np
from q01 import straight_manifold_vector
from q02 import circular_manifold_vector


def manifold_vector(coords: np.ndarray, theta: float, f: float, c: float = 334) -> np.ndarray:
    """アレイマニフォールドベクトルを計算

    Args:
        coods (ndarray):アレイの座標 (Mic, [x, y, 0])
        theta (float):音源方向
        f (float):周波数 [Hz]
        c (float):音速 [m/s] (defaulf = 334)
    Return:
        ndarray:アレイマニフォールドベクトル
    """

    theta = np.deg2rad(theta)
    direct_vec = np.array([np.sin(theta), np.cos(theta), 0])
    mani_vec = np.exp(1.0j * 2 * np.pi * f / c * direct_vec @ coords.T)

    return mani_vec


if __name__ == "__main__":
    d = 0.05
    r = 0.05
    M = 3
    theta = 45
    f = 1000

    coords_01 = []
    coords_02 = []

    for i in range(M):
        coords_01.append([(i - (M - 1) / 2) * d, 0, 0])
        coords_02.append([r * np.sin(2 * np.pi / M * i), r * np.cos(2 * np.pi / M * i), 0])

    coords_01 = np.array(coords_01)
    coords_02 = np.array(coords_02)

    print("q01")
    print(f"{straight_manifold_vector(d, M, theta, f)}")
    print("manifold")
    print(f"{manifold_vector(coords_01, theta, f)}")

    print("\nq02")
    print(f"{circular_manifold_vector(r, M, theta, f)}")
    print("manifold")
    print(f"{manifold_vector(coords_02, theta, f)}")
