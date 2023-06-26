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
x_ham=x*w_ham #npの要素積は*演算子でOK

plt.plot(t,x_ham)
plt.show()

##########確認コード##########

plt.plot(t,x) #元の正弦波
plt.xlim(0,1/f) #1周期分表示
plt.show()

plt.plot(t,w_ham) #窓関数を乗じた正弦波
plt.xlim(0,1/f) #1周期分表示
plt.show() #窓関数の端なので0に近い値をとるはず（Hamming窓だと0.08までしか抑えられない）