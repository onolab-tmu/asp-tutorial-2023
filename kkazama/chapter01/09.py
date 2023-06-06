import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

x, fs = sf.read("08.wav")

fs_down = 8000

step_down = int(fs // fs_down)
mix_down = x[::step_down]

sf.write("09.wav", mix_down, fs_down, subtype="FLOAT")

# 確認コード
t = np.arange(len(x)) / fs
t2 = np.arange(len(mix_down)) / fs_down

plt.title("Downsample")
plt.plot(t, x, marker=".", label="Raw")
plt.plot(t2, mix_down, marker="o", label="Downsampled")
plt.xlim(0, 10 / fs)
plt.legend()
plt.show()
