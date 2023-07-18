import numpy as np

c = 334


def circular_array_manifold_vector(r, M, theta, f):
    """
    theta : 音源方向（度数法）
    theta_rad : 音源方向（弧度法）
    r : アレイ半径[m]
    M : マイク数
    f : 周波数[Hz]
    a : アレイマニフォールドベクトル
    """
    theta_rad = np.pi * theta / 180
    a = np.zeros(M + 1, dtype=complex)
    u = np.array([np.sin(theta_rad), np.cos(theta_rad), 0])
    for m in range(1, M + 1):
        p = np.array([r * np.sin(2 * np.pi / M * (m - 1)), r * np.cos(2 * np.pi / M * (m - 1)), 0])
        a[m] = np.exp(1j * 2 * np.pi * f / c * np.sum(u * p))
    return a


if __name__ == "__main__":
    r = 0.05
    M = 3
    theta = 45
    f = 1000

    a = circular_array_manifold_vector(r, M, theta, f)
    print("\na = \n", a[1:], "\n")
