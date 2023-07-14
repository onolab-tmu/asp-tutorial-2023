import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm #for文の進捗を可視化できる

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

X=np.fft.fft(x)
Y=np.fft.fft(w_ham)

Z=np.zeros(len(X),dtype=complex)
# for k in tqdm(range(len(X))): #rangeをtqdmで括ると進捗を表示
#     for n in range(len(X)):
#         Z[k]+=X[n]*Y[k-n] #2重ループだと20分くらいかかる
        
k=np.arange(len(X)) #index行列を作成
for n in tqdm(range(len(X))):
    Z[k]+=X[n]*Y[k-n] #この書き方だと30秒くらい

z=np.fft.ifft(Z)

plt.plot(t,z)
plt.show()

#追記（for文を2重ループにしないことで計算を高速化）

# Z=np.zeros(len(X),dtype=complex)
# k=np.arange(len(X)) #index行列を作成
# for n in range(len(X)):
#     Z[k]+=X[n]*Y[k-n]