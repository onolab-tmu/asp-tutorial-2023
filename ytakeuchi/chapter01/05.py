import numpy as np
import matplotlib.pyplot as plt

A=1
f=440
fs=16000
s=3

t=np.arange(0,s+1/fs,1/fs)
x=A*np.sin(2*np.pi*f*t)
wn=np.random.normal(0,1,fs*s+1)

x_wn=x+wn

plt.plot(t,x_wn)
plt.show()

##########確認コード##########

plt.subplot(211)
plt.plot(t[:400],x[:400])
plt.subplot(212)
plt.plot(t[:400],x_wn[:400])
plt.show()