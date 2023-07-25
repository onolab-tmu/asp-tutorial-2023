import numpy as np


# 円状アレイを計算
def calculate_circular_array(r, M, theta, f):
    c = 334  # 音速
    theta = np.radians(theta)  # ラジアンにする
    a = np.zeros((M, 1), dtype="complex")  # アレイマニフォールドベクトル
    u = np.array([np.sin(theta), np.cos(theta), 0])  # 音源方向ベクトル

    # アレイに合わせて計算
    for m in range(M):
        p_m = np.array([r * np.sin(2 * np.pi / M * m), r * np.cos(2 * np.pi / M * m), 0])  # p[m]を計算
        a[m] = np.exp(np.dot(1j * 2 * np.pi * f / c * u, p_m))  # a[m]を計算

    return a


if __name__ == "__main__":
    r = 0.05  # アレイ半径[m]
    M = 3  # マイク数[個]
    theta = 45  # 音源方向[°]
    f = 1000  # 周波数[Hz]

    print(calculate_circular_array(r, M, theta, f))
