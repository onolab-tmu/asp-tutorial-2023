import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    X=np.zeros(len(x),dtype=complex)
    for k in range(len(X)):
        for n in range(len(x)):
            X[k]+=x[n]*np.exp(-1j*2*np.pi*k*n/len(x))
    return X

x=np.array([1,0,0,0,0,0,0,0])
X=dft(x)

k=np.arange(8)
plt.stem(k,np.abs(X))
plt.show()
plt.stem(k,np.angle(X))
plt.show()

##########確認コード##########

#X=[1+0j,1+0j,1+0j,1+0j,1+0j,1+0j,1+0j,1+0j]より，|X|=[1,1,1,1,1,1,1,1], angle(X)=[0,0,0,0,0,0,0,0]