import numpy as np


def conv_linear(x, h):
    N = len(x)
    z = np.zeros(2 * N - 1)
    for n in range(2 * N - 1):
        for k in range(N):
            if n - k >= 0 and n - k <= N - 1:
                z[n] += x[k] * h[n - k]
    #     for k in range(N):
    #         z[k:k+N]+=x[k]*h #ひとつずつすらし，配列hにxの要素に対応した重みをつけて加算
    return z


##########確認コード##########

x = np.array([1, 3, 1])
h = np.array([0, 1, 2])
print(conv_linear(x, h))  # [0,0,0,0,0]+[0,1,3,1,0]+[0,0,2,6,2]=[0,1,5,7,2]となるはず
