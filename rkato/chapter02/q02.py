import numpy as np
import q1
import matplotlib.pyplot as plt

# 8点の単位インパルス信号のDFT計算
delta = [1, 0, 0, 0, 0, 0, 0, 0]
t = np.arange(0, 7.0, 1.0)

delta_DFT = q1.calculate_dft(delta)
print("元波形")
print(delta)

print("DFT処理後")
print(delta_DFT)

delta_DFT_real = np.abs(delta_DFT)
delta_DFT_imag = np.imag(delta_DFT)
plt.plot(np.arange(0, delta_DFT_real.shape[0]), delta_DFT_real)
plt.title("Real")
plt.show()

plt.plot(np.arange(0, delta_DFT_imag.shape[0]), delta_DFT_imag)
plt.title("Image")
plt.show()
