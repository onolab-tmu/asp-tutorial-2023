import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def SN(s, x):
    pow_s = np.sum(s**2)
    pow_x = np.sum(x**2)
    
    return 10*np.log10(pow_s/pow_x)

a = np.array([3,4,5])
b = np.array([1,2,3])

print(SN(a, b))

def Wn(s, x, snr):
    pow_s = np.sum(s**2)
    pow_x = np.sum(x**2)
    
    x = np.sqrt(pow_s / pow_x / 10 ** (snr/10))
    return x

def add_white_noise_with_snr(s, snr):
    white_noise = np.random.rand(len(s))
    coef = Wn(s, white_noise, snr)
    
    return s + coef * white_noise

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

mix2, sr2 = sf.read('1_8.wav')
wn = mix2 - y
print(SN(y, wn))