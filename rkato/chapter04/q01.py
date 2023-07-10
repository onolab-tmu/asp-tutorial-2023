import numpy as np


# L-Sこのゼロ詰め　Sの倍数になるようにゼロ詰め
def padding(x, L, S):
    x_pad = np.pad(x, [L - S, L - S])
    re = np.mod(len(x_pad), S)
    if re != 0:
        x_pad = np.pad(x_pad, [0, S - re])
    return x_pad


##### 確認コード #####
L = 4
S = 3
x = np.ones(8)
print(padding(x, L, S))
