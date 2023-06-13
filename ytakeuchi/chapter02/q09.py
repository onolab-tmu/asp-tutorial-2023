import numpy as np
import matplotlib.pyplot as plt

A=1
f=440
fs=16000
s=3

t=np.arange(0,s+1/fs,1/fs)
x=A*np.sin(2*np.pi*f*t)

def make_ham(N):
    w=np.zeros(N)
    for n in range(N):
        w[n]=0.54-0.46*np.cos(2*np.pi*n/(N-1))
    return w

w_ham=make_ham(len(x))

W_HAM=np.fft.fft(w_ham)
ks=np.arange(len(W_HAM))-fs*s//2 #0中心
k_list=ks*fs/len(W_HAM)

plt.plot(k_list,20*np.log10(np.abs(W_HAM[ks])))
plt.show()
plt.plot(k_list,np.angle(W_HAM[ks]))
plt.show()
plt.plot(k_list,np.angle(W_HAM[ks]))
plt.xlim((-5,5)) #0付近を表示
plt.show()