import numpy as np


def conv_circular(x, h):
    N = len(x)
    z = np.zeros(N)
    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]  # 負の値のmodについては，例えば-1≡3(mod 4)（-1=4*(-1)+3であるため）
    #     X=np.fft.fft(x)
    #     H=np.fft.fft(h)
    #     z=np.fft.ifft(X*H).real #2つの信号をfftし，乗算したのちifftすることでも計算可能
    return z


##########確認コード##########

x = np.array([1, 3, 1])
h = np.array([0, 1, 2])
print(conv_circular(x, h))  # [0,0,0]+[1,1,3]+[6,2,2]=[7,3,5]となるはず
