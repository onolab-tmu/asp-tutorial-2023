import numpy as np
import q1
import matplotlib.pyplot as plt

delta = [1, 0, 0, 0, 0, 0, 0, 0]
#####q2のDFT#####
delta_DFT = q1.calculate_dft(delta)

#####numpyを使用してみる#####
delta_npDFT = np.fft.fft(delta)


print(delta_DFT)
print(delta_npDFT)

plt.plot(np.arange(0, len(delta_DFT)), delta_DFT, marker="o", label="q2DFT")
plt.plot(np.arange(0, len(delta_npDFT)), delta_npDFT, marker="x", label="numpyDFT")
plt.legend()
plt.show()
