import numpy as np
import soundfile as sf

A =  1      #   振幅の設定
f1 =  440    #   周波数の設定[Hz]
f2 =  660    #   周波数の設定[Hz]
Fs = 16000       #  サンプリング周波数の設定[Hz]
L = 3.0     #   信号長さ[s]

t = np.arange(0,L,1/Fs)# 0からLまで1/Fs刻みで準備
sinwave1 = A*np.sin(2*np.pi*f1*t)   #正弦波生成
sinwave2 = A*np.sin(2*np.pi*f2*t)   #正弦波生成

#sin_st=np.array([sinwave1,sinwave2])
sin_st=np.stack((sinwave1,sinwave2),axis=1)


sf.write('sin_st.wav',sin_st,Fs,"PCM_16")


print(sf.info('sin_st.wav'))#wavフォーマットの確認