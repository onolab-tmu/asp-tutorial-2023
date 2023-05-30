import numpy as np

def add_SN(s,snr):
    v=np.sqrt(sum(s**2)/len(s)*10**(-snr/10))
    wn=np.random.normal(0,v,len(s))
    return s+wn

##########確認コード##########

def calc_SN(s,x):
    return 10*np.log10(sum(s**2)/sum(x**2))

A=1
f=440
fs=16000
s=3

snr=6

t=np.arange(0,s+1/fs,1/fs)
x=A*np.sin(2*np.pi*f*t)
x_wn=add_SN(x,snr)

print(f"SNR should be {snr}, SNR is {calc_SN(x,x_wn-x)}")