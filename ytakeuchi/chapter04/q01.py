import numpy as np


def zero_pad(L, S, x):
    y = np.pad(x, (L - S, L - S))  # xの前後にL-Sだけ0をパディング
    len_modS = len(y) % S
    if len_modS > 0:
        y = np.pad(y, (0, S - len_modS))  # Sの倍数になるようパディング
    return y  # （LとSの最小公倍数の倍数になるようにパディングすると一般化可能）


##########確認コード##########

L = 10
S = 5  # L-S=5なので先頭に0が5つ
x = np.array([1, 3, 5])
print(zero_pad(L, S, x))  # [0,0,0,0,0,1,3,5,0,0,0,0,0,0,0]となるはず
