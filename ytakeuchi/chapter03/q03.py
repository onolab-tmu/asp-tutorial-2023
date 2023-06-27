import numpy as np


def conv_circular(x, h):
    N = len(x)
    z = np.zeros(N)
    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]
    return z


def conv_circular_zero(x, y):
    N = len(x)
    z = np.zeros(2 * N - 1)
    return conv_circular(np.pad(x, (0, N - 1)), np.pad(y, (0, N - 1)))  # pad関数によって前に0個，後にN-1個定数をパディング


##########確認コード##########

x = np.array([1, 3, 1])
h = np.array([0, 1, 2])
print(conv_circular_zero(x, h))  # [0,0,0,0,0]+[0,1,3,1,0]+[0,0,2,6,2]=[0,1,5,7,2]となるはず
