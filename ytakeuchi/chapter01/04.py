import numpy as np
import matplotlib.pyplot as plt

fs=16000
s=3

wn=np.random.normal(0,1,fs*s+1) #平均,標準偏差,サイズ（今回はサンプリング周波数*時間）
t=np.arange(0,s+1/fs,1/fs)
plt.plot(t,wn)
plt.show()

##########確認コード##########

plt.hist(wn,bins=500) #階級数500のヒストグラム
plt.show()
print(f"mean = {np.mean(wn)}, sd = {np.std(wn)}")