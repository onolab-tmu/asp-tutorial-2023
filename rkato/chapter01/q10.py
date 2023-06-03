import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

L=3.0
data,Fs=sf.read('sin_down.wav') #データの読み込み
t = np.arange(0,L,1/Fs)# 0からLまで1/Fs刻みで準備

#移動平均のサイズ
w_size = 5  
v = np.ones(w_size) / w_size

#フィルタ適用
sin_fil = np.convolve(data,v,mode='same')

#グラフで確認
fig,ax = plt.subplots()
ax.plot(t,data,label='noise+sin')
ax.plot(t,sin_fil,label='noise+sin(移動平均)')

plt.xlim(0,20 / Fs)
plt.show()

