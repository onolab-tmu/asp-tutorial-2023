import numpy as np
import matplotlib.pyplot as plt

A =  1      #   振幅の設定
f =  440    #   周波数の設定[Hz]
Fs = 16000       #  サンプリング周波数の設定[Hz]
L = 3.0     #   信号長さ[s]

t = np.arange(0,L,1/Fs)# 0からLまで1/Fs刻みで準備
sinwave = A*np.sin(2*np.pi*f*t)   #正弦波生成
plt.plot(t,sinwave)
plt.show()



# 