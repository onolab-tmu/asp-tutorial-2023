import numpy as np
import matplotlib.pyplot as plt

fs=16000
s=3

wn=np.random.normal(0,1,fs*s+1) #平均,標準偏差,サイズ（今回はサンプリング周波数*時間）
t=np.arange(0,s+1/fs,1/fs)
plt.plot(t,wn)
plt.show()

##########確認コード##########

plt.hist(wn,bins=500) #階級数500のヒストグラム
plt.show()
print(f"mean = {np.mean(wn)}, sd = {np.std(wn)}")

##########確認コード（解説）##########
#パワースペクトルがフラットであることを確認
sig_len_sample = fs * s  # signal length (sample)
white_noise_spec = np.fft.rfft(wn) # ホワイトノイズのスペクトル

power = 10 * np.log10(np.abs(white_noise_spec) ** 2)
freq = np.arange(sig_len_sample // 2 + 1) / sig_len_sample * fs
plt.title("White noise (Freqency domain)")
plt.plot(freq, power)
plt.ylabel("Power")
plt.xlabel("Freq. (Hz)")
plt.show()
