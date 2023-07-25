import numpy as np


def linear_array_manifold_vector(d, M, theta, f, c):
    """アレイマニフォールドベクトル（直線状アレイ）
    Args:
        d(double): アレイ間隔
        M(int): マイク数
        thete(int): 音源方向
        f(int): 周波数[Hz]
        c(int): 音速[m/s]
    Return:
        a(ndarray): アレイマニフォールドベクトル（直線状アレイ）
    """
    theta = np.deg2rad(theta)
    u = np.array([np.sin(theta), np.cos(theta), 0])
    a = np.zeros((M, 1), dtype=np.complex64)
    for m in range(M):
        pm = np.array([(m - (M - 1) // 2) * d, 0, 0])
        inp = np.dot(pm, u)
        a[m] = np.exp(1j * 2 * np.pi * f * inp / c)

    return a


d = 0.05
M = 3
theta = 45
f = 1000
c = 334
print(linear_array_manifold_vector(d, M, theta, f, c))
