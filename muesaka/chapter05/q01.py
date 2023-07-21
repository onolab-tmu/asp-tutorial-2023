import numpy as np


# 直線状アレイを計算
def calculate_linear_array(d, M, theta, f):
    c = 334  # 音速
    theta = np.radians(theta)  # ラジアンにする
    a = np.zeros((M, 1), dtype="complex")  # アレイマニフォールドベクトル
    u = np.array([np.sin(theta), np.cos(theta), 0])  # 音源方向ベクトル

    # アレイに合わせて計算
    for m in range(M):
        p_m = np.array([(m - (M - 1) / 2) * d, 0, 0])  # p[m]を計算
        a[m] = np.exp(np.dot(1j * 2 * np.pi * f / c * u, p_m))  # a[m]を計算

    return a


if __name__ == "__main__":
    d = 0.05  # アレイ間隔[m]
    M = 3  # マイク数[個]
    theta = 45  # 音源方向[°]
    f = 1000  # 周波数[Hz]

    print(calculate_linear_array(d, M, theta, f))
