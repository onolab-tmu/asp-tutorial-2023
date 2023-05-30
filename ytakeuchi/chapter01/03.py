import numpy as np
import soundfile as sf

A1=1
f1=440
fs1=16000
s1=3

t1=np.arange(0,s1+1/fs1,1/fs1)
x1=A1*np.sin(2*np.pi*f1*t1)

A2=1
f2=660
fs2=16000
s2=3

t2=np.arange(0,s2+1/fs2,1/fs2)
x2=A2*np.sin(2*np.pi*f2*t2)

x=np.array([x1,x2]) #2つの信号を1つの配列にまとめる
x=x.T #ステレオの場合は[[x1,x2,...],[y1,y2,...]]ではなく[[x1,y1],[x2,y2],...]とする

sf.write("ch01_3.wav",x,fs,format="WAV",subtype="PCM_16")

##########確認コード##########

plt.plot(t2[:400],x2[:400]) #1秒に660回 => 0.025秒に16.5回
plt.show()