import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import librosa

y, sr = librosa.core.load("1_8.wav", sr=8000)
sf.write("1_9.wav", y, sr, subtype="FLOAT")

plt.plot(y)
