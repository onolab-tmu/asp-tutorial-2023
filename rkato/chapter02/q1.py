import numpy as np

###### DFTを行う関数の作成  ######
def calculate_dft(x):
    length = len(x)  # 信号の点数を取得
    X = np.zeros(length, dtype=complex)
    for n in range(length):
        weight = np.exp(-1j * ((2 * np.pi * n) / length))
        X_omega = 0
        for omega in range(length):
            X_omega += x[omega] * (weight**omega)
        X[n] = X_omega
    return X


######  IDFTを行う関数の作成  #####
def calculate_idft(Y):
    length = len(Y)  # 信号の点数を取得
    y = np.zeros(length, dtype=complex)
    for n in range(length):
        weight = np.exp(1j * ((2 * np.pi * n) / length))
        y_omega = 0
        for omega in range(length):
            y_omega += Y[omega] * (weight**omega) / length
        y[n] = y_omega
    return y


#上手くいかなかったパターン     
###### DFTを行う関数の作成  ######
# def calculate_dft(x):
#     N = len(x)  # 信号の点数を取得
#     DFT = []
#     for k in range(N):
#         weight = np.exp(-1j * ((2 * np.pi * k) / N))
#         sum = 0
#         for num in range(N):
#             sum += x[num] * (weight**num)
#     print(k)
#     DFT.append(sum)
#     return np.array(DFT)
