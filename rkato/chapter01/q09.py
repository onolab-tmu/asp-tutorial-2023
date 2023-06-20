import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np


Fs2 = 8000
sin_noise_adj,Fs1 = sf.read('sin_noise_adj.wav')

sin_down = sin_noise_adj[::2]


sf.write('sin_down.wav',sin_down,Fs2)


#####作成したファイルを読み込みプロットしてみる#####

sin_down,Fs_down = sf.read('sin_down.wav')
sig_len_sample = len(sin_noise_adj)
sig_len_sample_down = len(sin_down)

t = np.arange(sig_len_sample) / Fs1
t_down = np.arange(sig_len_sample_down) / Fs2

#plot
plt.title("Downsample")
plt.plot(t, sin_noise_adj, marker='.', label="Raw")
plt.plot(t_down, sin_down, marker="o", label="Downsampled")
plt.xlim(0, 30 / Fs1)
plt.legend()
plt.show()



