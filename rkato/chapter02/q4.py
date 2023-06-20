import numpy as np
import q1
import matplotlib.pyplot as plt

#####q2の内容#####
delta = [1, 0, 0, 0, 0, 0, 0, 0]
delta_DFT = q1.calculate_dft(delta)

amplitude = np.abs(delta_DFT)
phase = np.angle(delta_DFT)
freq = np.linspace(0, 8000, len(delta))

# 振幅スペクトル・位相スペクトルを図示
plt.plot(freq[0 : int(len(delta))], amplitude[0 : int(len(delta))])
plt.xlabel("Frequency [Hz]", fontsize=20)
plt.ylabel("Amplitude", fontsize=20)
plt.show()

plt.plot(freq[0 : int(len(delta))], phase[0 : int(len(delta))])
plt.xlabel("Frequency [Hz]", fontsize=20)
plt.ylabel("Phase[rad]", fontsize=20)
plt.show()
