import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import librosa


def fivefilter(x):
    b = [0.2, 0.2, 0.2, 0.2, 0.2]
    a = np.convolve(x, b, mode="full")

    return a


y, sr = librosa.core.load("1_8.wav", sr=8000)

x = fivefilter(y)

plt.plot(y)
plt.title("Before")
plt.show()

plt.plot(x)
plt.title("After")
plt.show()

plt.plot(y)
plt.plot(x)
plt.show()
