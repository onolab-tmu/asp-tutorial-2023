import numpy as np

def dft(x):
    X=np.zeros(len(x),dtype=complex) #複素数として0行列を定義
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

##########確認コード##########

x=np.array([2,3,5,9])
X=dft(x)
print(X)
x2=idft(X)
print(x2) #[2,3,5,9]となるはず