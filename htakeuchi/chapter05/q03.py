import numpy as np

c = 334


def array_manifold_vector(coordinate, theta, f):
    """
    theta : 音源方向（度数法）
    theta_rad : 音源方向（弧度法）
    coodinate : 座標の配列．サイズはMであり，m=1に対応する値はcoordinate[0]に格納．
    f : 周波数[Hz]
    a : アレイマニフォールドベクトル．サイズはM+1であり，m=1に対応する値をa[1]に格納．
    """
    theta_rad = np.pi * theta / 180
    M = coordinate.shape[0]
    a = np.zeros(M + 1, dtype=complex)
    u = np.array([np.sin(theta_rad), np.cos(theta_rad), 0])
    for m in range(1, M + 1):
        p = np.array([coordinate[m - 1][0], coordinate[m - 1][1], 0])  # m=1に対応するのはcoordinate[0]．
        a[m] = np.exp(1j * 2 * np.pi * f / c * np.sum(u * p))
    return a


if __name__ == "__main__":
    theta = 45
    f = 1000

    # 問題1の座標
    d = 0.05
    coordinate_linear = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])

    # 問題2の座標
    r = 0.05
    coordinate_circular = np.array(
        [
            [0, r, 0],
            [r * np.sin(2 * np.pi / 3), r * np.cos(2 * np.pi / 3), 0],
            [r * np.sin(2 * np.pi / 3 * 2), r * np.cos(2 * np.pi / 3 * 2), 0],
        ]
    )

    a_linear = array_manifold_vector(coordinate_linear, theta, f)
    print("\na_linear = \n", a_linear[1:], "\n")  # 問題1と同じ結果になるはず

    a_circular = array_manifold_vector(coordinate_circular, theta, f)
    print("\na_circular = \n", a_circular[1:], "\n")  # 問題2と同じ結果になるはず
