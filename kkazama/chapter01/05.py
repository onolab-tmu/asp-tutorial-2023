import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

x1, _ = sf.read("01.wav")
x2, _ = sf.read("04.wav")

x = x1 + x2

plt.plot(x)
plt.show()
