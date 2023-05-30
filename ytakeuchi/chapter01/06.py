import numpy as np

# def calc_SN(s,x):
#     sum_s,sum_x=0,0
#     for i in range(len(s)):
#         sum_s+=s[i]**2
#         sum_x+=x[i]**2
#     return 10*np.log(sum_s/sum_x)

def calc_SN(s,x):
    return 10*np.log10(sum(s**2)/sum(x**2))

##########確認コード##########

A=1
f=440
fs=16000
s=3

t=np.arange(0,s+1/fs,1/fs)
x=A*np.sin(2*np.pi*f*t)
wn=np.random.normal(0,1,fs*s+1)

print(calc_SN(x,wn))