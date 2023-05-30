#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""1_1"""

import numpy as np
import matplotlib.pyplot as plt

a = 1
f = 440
fs = 16000
s = 3

t = np.arange(0, s, 1/fs)
y = a * np.sin(2*np.pi*f*t)

plt.plot(t,y)

plt.xlim(0, 1 / f)


# In[2]:


"""1_2"""

import soundfile as sf
sf.write('1_2.wav', y, fs)

sf.info('1_2.wav')


# In[3]:


"""1_3"""

a2 = 1
f2 = 660
fs2 = 16000
s2 = 3

t2 = np.arange(0, s2, 1/fs2)
y2 = a2 * np.sin(2*np.pi*f2*t2)
y1 = y
wave = np.stack((y1, y2), axis = 1)

sf.write('1_3.wav', wave, fs2)
sf.info('1_3.wav')


# In[4]:


"""1_4"""

A = 1.0
sec = 3.0
fs = 16000

x = np.random.rand(round(fs*sec))

plt.plot(x)
plt.show()


# In[5]:


x_spec = np.fft.rfft(x)

power = 10 * np.log10(np.abs(x_spec)**2)
freq = np.arange((fs*sec) // 2 + 1) / (fs*sec) * fs

plt.plot(freq,power)


# In[6]:


"""1_5"""

fy = y + x

sf.write('1_5.wav', fy, fs)
plt.plot(fy)
plt.show


# In[7]:


plt.plot(t, fy, label="Mix")
plt.plot(t, y, label="Sin wave")
plt.plot(t, x, label="White noise")
plt.xlim(0,10 / fs)
plt.legend()
plt.show()


# In[8]:


"""1_6"""

def SN(s, x):
    pow_s = np.sum(s**2)
    pow_x = np.sum(x**2)
    
    return 10*np.log10(pow_s/pow_x)

a = np.array([3,4,5])
b = np.array([1,2,3])

print(SN(a, b))


# In[9]:


"""1_7"""

# def Wn(s, a, sec, f):
#     x = a*np.random.rand(round(f*sec))
#     wn = SN(s, x, f*sec)
#     print(wn)
#     return s


# In[10]:


"""1_7"""

def Wn(s, x, snr):
    pow_s = np.sum(s**2)
    pow_x = np.sum(x**2)
    
    x = np.sqrt(pow_s / pow_x / 10 ** (snr/10))
    return x

def add_white_noise_with_snr(s, snr):
    white_noise = np.random.rand(len(s))
    coef = Wn(s, white_noise, snr)
    
    return s + coef * white_noise


# In[11]:


snr = 0
s = 3
fs = 16000
a = 1
f = 440

t = np.arange(0, s, 1/fs)
y = a * np.sin(2*np.pi*f*t)
mix = add_white_noise_with_snr(y, snr)

wn = mix - y
print(SN(y, wn))


# In[12]:


"""1_8"""

# a = 1
# f = 440
# fs = 16000
# s = 3

# t = np.arange(0, s, 1/fs)
# y = a * np.sin(2*np.pi*f*t) + 0.33
# x = Wn(y, a, s, fs)
# print(x)

# sf.write('1_8.wav', x, fs)
# plt.plot(x)


# In[13]:


"""1_8"""

f = 440
fs = 16000
s = 3
snr = 6

t = np.arange(fs * 3)/fs
y = np.sin(2*np.pi*f*t)
# x = np.random.rand(round(fs*s))
# b = Wn(y, x, snr)
# print(b)
mix = add_white_noise_with_snr(y, snr)

sf.write('1_8.wav', mix, fs, subtype="FLOAT")
plt.plot(mix)


# In[14]:


mix2, sr2 = sf.read('1_8.wav')
wn = mix2 - y
print(SN(y, wn))


# In[15]:


"""1_9"""

import librosa

y, sr = librosa.core.load('1_8.wav', sr=8000)
sf.write('1_9.wav', y, sr, subtype="FLOAT")

plt.plot(y)


# In[16]:


"""1_10"""

def fivefilter(x):
    b = [0.2, 0.2, 0.2, 0.2, 0.2]
    a = np.convolve(x, b, mode="full") 

    return a

y, sr = librosa.core.load('1_8.wav', sr=8000)

x = fivefilter(y)

plt.plot(y)
plt.title("Before")
plt.show()

plt.plot(x)
plt.title('After')
plt.show()

plt.plot(y)
plt.plot(x)
plt.show()


# In[ ]:




