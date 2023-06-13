import numpy as np
import matplotlib.pyplot as plt

A=1 #振幅
f=440 #周波数（1秒間に正弦波が440個）
fs=16000 #サンプリング周波数（1秒間に16000回サンプリング）
s=3 #信号の長さ

t=np.arange(0,s+1/fs,1/fs) #1秒にfsプロットなので1/fsずつ増える時間信号
x=A*np.sin(2*np.pi*f*t) #正弦波の生成（x=Asin(2πft)）
plt.plot(t,x)
plt.show()

##########確認コード##########

plt.plot(t[:400],x[:400]) #1秒に440回 => 0.025秒に11回
plt.show()

##########確認コード（解説）##########

plt.plot(t,x)
plt.xlim(0,1/f) #1周期のみをプロット
plt.show()