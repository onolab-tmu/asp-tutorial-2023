import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def add_SN(s,snr):
    v=np.sqrt(sum(s**2)/len(s)*10**(-snr/10))
    wn=np.random.normal(0,v,len(s))
    return s+wn

A=1
f=440
fs=16000
s=3

t=np.arange(0,s+1/fs,1/fs)
x=A*np.sin(2*np.pi*f*t)
x_wn=add_SN(x,6)

sf.write("ch01_8.wav",x_wn,fs,subtype="FLOAT") #subtype="FLOAT"にすると再現性が担保できる

##########確認コード##########

def calc_SN(s,x):
    return 10*np.log10(sum(s**2)/sum(x**2))

x2,fs2=sf.read("ch01_8.wav")
t2=np.arange(0,(len(x2)-1)/fs2+1/fs2,1/fs2)
plt.plot(t2,x2)
plt.show()
plt.plot(t2[:400],x2[:400])
plt.show()

##########確認コード（解説）##########

def calc_SN(s,x):
    return 10*np.log10(sum(s**2)/sum(x**2))

x2,fs2=sf.read("ch01_8.wav")
print(f"SNR should be 6, SNR is {calc_SN(x,x2-x)}")