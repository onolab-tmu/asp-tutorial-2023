import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

save_filepath = "mix_downsample.wav"
_format = "WAV"
subtype = "PCM_16"
mix_filepath = "mix_snRatio.wav"
wave_mix, samplerate = sf.read(mix_filepath)
fs = 8000
sec = 3
fsRate = int(samplerate / fs)

t_mix = np.arange(sec * samplerate) / samplerate
t_down = np.arange(sec * fs) / fs
idx = fsRate * np.array([i for i in range(sec * fs)])

wave_down = wave_mix[idx]

plt.figure()
plt.plot(t_down, wave_down, label="downsample")
plt.plot(t_mix, wave_mix, label="mix_signal")
plt.xlim(0, 0.01)
plt.legend()
plt.show()

sf.write(save_filepath, wave_down, fs, format=_format, subtype=subtype)
