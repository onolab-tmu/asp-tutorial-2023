import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    X=np.zeros(len(x),dtype=complex)
    for k in range(len(X)):
        for n in range(len(x)):
            X[k]+=x[n]*np.exp(-1j*2*np.pi*k*n/len(x))
    return X

def idft(X):
    x=np.zeros(len(X),dtype=complex)
    for n in range(len(x)):
        for k in range(len(X)):
            x[n]+=X[k]*np.exp(1j*2*np.pi*k*n/len(X))
        x[n]/=len(X)
    return x

x=np.array([1,0,0,0,0,0,0,0])
X=dft(x)
x2=idft(X)
print(x2)

t=np.arange(8)
plt.stem(t,np.abs(x2))
plt.show()

##########確認コード##########

#手計算により確認可能．x[0]=1*exp(0)*8/8=1, x[i](i=1,2,...,7)は単位円を8分割した点の平均なので0