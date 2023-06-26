import numpy as np

def dft(x):
    X=np.zeros(len(x),dtype=complex)
    for k in range(len(X)):
        for n in range(len(x)):
            X[k]+=x[n]*np.exp(-1j*2*np.pi*k*n/len(x))
    return X

x=np.array([1,0,0,0,0,0,0,0])
X=dft(x)
X_np=np.fft.fft(x) #numpy内のfft関数（高速フーリエ変換）
print(f"my dft: {X}\nnumpy fft: {X_np}")