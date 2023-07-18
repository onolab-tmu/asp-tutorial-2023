import numpy as np


def spatial_correlation_matrix(X):
    """
    X : M*F*Tの複素数行列
    X_tr : XをF*T*M行列に変換した行列．x_ftはM個の要素からなるベクトルであるから，計算しやすいように変形している．
    x_ft : ある(f,t)における各チャネルの値を要素に持つベクトル．要素数はチャネル数であるM．numpyのdot関数を使うためにreshapeしている．
    x_ft_H : x_ftの共役転置
    R : 空間相関行列
    """
    M = X.shape[0]
    F = X.shape[1]
    T = X.shape[2]
    R = np.zeros((F, M, M), dtype=complex)
    X_tr = X.transpose(1, 2, 0)  # F*T*M行列にする
    for f in range(F):
        for t in range(T):
            x_ft = X_tr[f][t].reshape(M, 1)  # M*1のベクトルにする
            x_ft_H = np.conj(X_tr[f][t]).reshape(1, M)  # 複素共役をとり，1*Mのベクトルにする
            # print("\n", np.dot( x_ft, x_ft_H ))
            R[f] += np.dot(x_ft, x_ft_H) / T  # 行列積をとり，Tで割る
    return R


if __name__ == "__main__":
    X = np.array(
        [[[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]], [[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]]]
    )

    R = spatial_correlation_matrix(X)
    print("\nR = \n", R)
