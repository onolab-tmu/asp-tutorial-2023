import numpy as np
import matplotlib.pyplot as plt

A=1
f=440
fs=16000
s=3

t=np.arange(0,s+1/fs,1/fs)
x=A*np.sin(2*np.pi*f*t)

X=np.fft.fft(x)
ks=np.arange(len(X))-len(X)//2 #負のインデックスに対応するための配列
k_list=ks*fs/len(X) #X[k]はk*fs/N(Hz)の正弦波に対するスペクトル

X_sliced=X[ks]

plt.plot(k_list,20*np.log10(np.abs(X_sliced)))
plt.show()
plt.plot(k_list,np.angle(X_sliced))
plt.show()
plt.stem(k_list,np.angle(X_sliced))
plt.xlim((430,450)) #440Hz付近を表示
plt.show()

##########確認コード##########

print(f"peak index: {np.argmax(np.abs(X))}, frequency: {np.argmax(np.abs(X))*fs/len(X)}")