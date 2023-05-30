import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

x,fs=sf.read("ch01_9.wav")
y=np.zeros(len(x))
t=np.arange(0,(len(x)-1)/fs+1/fs,1/fs)

A=1
f=440
fs=8000
s=3
sin_wave=A*np.sin(2*np.pi*f*t)

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

##########確認コード（解説）##########

def calc_SN(s,x):
    return 10*np.log10(sum(s**2)/sum(x**2))
    
print(f"input SNR: {calc_SN(sin_wave,x-sin_wave)}\noutput SNR: {calc_SN(sin_wave,y-sin_wave)}")