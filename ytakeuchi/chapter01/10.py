import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

x,fs=sf.read("ch01_9.wav")
y=np.zeros(len(x))
t=np.arange(0,(len(x)-1)/fs+1/fs,1/fs)

for i in range(5,len(y)-6):
    y[i]=np.mean(x[i-5:i+5])
    
plt.plot(t,x)
plt.show()

plt.plot(t,y)
plt.show()

##########確認コード？##########
    
plt.plot(t[:200],x[:200])
plt.show()

plt.plot(t[:200],y[:200])
plt.show()