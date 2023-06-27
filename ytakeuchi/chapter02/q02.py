import numpy as np

def dft(x):
    X=np.zeros(len(x),dtype=complex)
    for k in range(len(X)):
        for n in range(len(x)):
            X[k]+=x[n]*np.exp(-1j*2*np.pi*k*n/len(x))
    return X

x=np.array([1,0,0,0,0,0,0,0])
X=dft(x)
print(X)

##########確認コード##########

#手計算により確認可能．x[i]= 1(i=0), 0(i=1,2,...,7)よりX[j]=1(j=0,1,...,7)