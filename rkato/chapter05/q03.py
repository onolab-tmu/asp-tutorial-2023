import numpy as np


def calc_amv(array, theta, f):
    n_mic = array[0].size
    amv = np.zeros((n_mic, 1), dtype=np.complex64)
    theta = np.radians(theta)  # deg→radに変換
    c = 334
    u = [np.sin(theta), np.cos(theta), 0]
    # アレイマニフォールドベクトルの計算
    for m in range(n_mic):
        inp = np.dot(array[m], u)
        amv[m] = np.exp(1j * 2 * np.pi * f * inp / c)
    return amv


def main():
    # 以下確認コード
    theta = 45
    f = 1000
    n_mic = 3
    d = 0.05
    # 直線状アレイ
    print("直線状アレイの計算結果")
    amv_line = np.zeros((n_mic, 1), dtype=np.complex64)
    pm_line = np.zeros((n_mic, 3), dtype=np.complex64)
    for num in range(n_mic):
        pm_line[num] = [d * (num - (n_mic - 1) / 2), 0, 0]
    amv_line = calc_amv(pm_line, theta, f)
    print(amv_line)
    # [[0.74137855-0.6710871j]
    # [1.        +0.j       ]
    # [0.74137855+0.6710871j]]

    # 円状アレイ
    r = 0.05
    print("円状アレイの計算結果")
    amv_circle = np.zeros((n_mic, 1), dtype=np.complex64)
    pm_circle = np.zeros((n_mic, 3), dtype=np.complex64)
    for num in range(n_mic):
        pm_circle[num] = [
            r * np.sin(2 * np.pi * num / n_mic),
            r * np.cos(2 * np.pi * num / n_mic),
            0,
        ]
    amv_circle = calc_amv(pm_circle, theta, f)
    print(amv_circle)


#  [[0.7868537 +0.6171396j]
#  [0.97051346+0.2410468j]
#  [0.6148926 -0.7886109j]]


if __name__ == "__main__":
    main()
