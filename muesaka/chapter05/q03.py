import numpy as np


# 一般のアレイを計算
def calculate_array(p, theta, f):
    c = 334  # 音速
    M = len(p)  # マイク数
    theta = np.radians(theta)  # ラジアンにする
    a = np.zeros((M, 1), dtype="complex")  # アレイマニフォールドベクトル
    u = np.array([np.sin(theta), np.cos(theta), 0])  # 音源方向ベクトル

    # アレイに合わせて計算
    for m in range(M):
        p_m = p[m]
        a[m] = np.exp(np.dot(1j * 2 * np.pi * f / c * u, p_m))  # a[m]を計算

    return a


if __name__ == "__main__":
    d = 0.05  # アレイ間隔[m]
    r = 0.05  # アレイ半径[m]
    M = 3  # マイク数[個]
    theta = 45  # 音源方向[°]
    f = 1000  # 周波数[Hz]

    p_linear = np.vstack([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])  # 直線状アレイ
    p_circular = np.vstack(  # 円状アレイ
        [
            [r * np.sin(0), r * np.cos(0), 0],
            [r * np.sin(2 * np.pi / M), r * np.cos(2 * np.pi / M), 0],
            [r * np.sin(4 * np.pi / M), r * np.cos(4 * np.pi / M), 0],
        ]
    )

    print(calculate_array(p_linear, theta, f))  # q01と同じになるはず
    print(calculate_array(p_circular, theta, f))  # q02と同じになるはず
