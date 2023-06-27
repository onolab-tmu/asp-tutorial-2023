import numpy as np
import soundfile as sf
import IPython.display

A=1
f=440
fs=16000
s=3

t=np.arange(0,s+1/fs,1/fs)
x=A*np.sin(2*np.pi*f*t)

sf.write("ch01_2.wav",x,fs,format="WAV",subtype="PCM_16") #file名,data,サンプリング周波数,fileの種類,フォーマット

##########確認コード##########

x2,fs2=sf.read("ch01_2.wav")
t2=np.arange(0,(len(x2)-1)/fs2+1/fs2,1/fs2)
plt.plot(t2,x2)
plt.show()
plt.plot(t2[:400],x2[:400]) #1秒に440回 => 0.025秒に11回
plt.show()

##########確認コード（解説）##########

print(sf.info("ch01_2.wav")) #ファイル名を指定すると情報を取得できる
#IPython.display.Audio(x,rate=fs) #notebookのときは直接埋め込める
