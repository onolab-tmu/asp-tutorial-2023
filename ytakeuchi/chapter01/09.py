import numpy as np
import soundfile as sf

x,fs=sf.read("ch01_8.wav")

fs2=8000
x2=x[::fs//fs2] #fs//fs2(今回は2)ごとに要素を抽出(スライスと呼ばれる)

sf.write("ch01_9.wav",x2,fs2)

##########確認コード##########

def calc_SN(s,x):
    return 10*np.log10(sum(s**2)/sum(x**2))

x2,fs2=sf.read("ch01_9.wav")
t2=np.arange(0,(len(x2)-1)/fs2+1/fs2,1/fs2)
plt.plot(t2,x2)
plt.show()
plt.plot(t2[:200],x2[:200])
plt.show()
print(len(x2))