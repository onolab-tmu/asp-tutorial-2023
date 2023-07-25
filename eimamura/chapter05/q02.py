import numpy as np


def circular_array_manifold_vector(r, M, theta, f, c):
    """アレイマニフォールドベクトル（円状アレイ）
    Args:
        r(double): アレイ半径[m]
        M(int): マイク数
        theta(int): 音源方向
        f(int): 周波数[Hz]
        c(int): 音速[m/s]
    Return:
        a(ndarray): アレイマニフォールドベクトル（円状アレイ）
    """
    theta = np.deg2rad(theta)
    u = np.array([np.sin(theta), np.cos(theta), 0])
    a = np.zeros((M, 1), dtype=np.complex64)
    for m in range(M):
        pm = np.array(
            [
                r * np.sin(2 * np.pi * m / M),
                r * np.cos(2 * np.pi * m / M),
                0,
            ]
        )
        inp = np.dot(pm, u)
        a[m] = np.exp(1j * 2 * np.pi * f * inp / c)

    return a


r = 0.05
M = 3
theta = 45
f = 1000
c = 334
print(circular_array_manifold_vector(r, M, theta, f, c))
