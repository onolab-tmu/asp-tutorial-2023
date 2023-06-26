import numpy as np
import q1
import matplotlib.pyplot as plt

#####q2の内容#####
delta = [1, 0, 0, 0, 0, 0, 0, 0]
delta_DFT = q1.calculate_dft(delta)  # DFT
delta_DFT_IDFT = q1.calculate_idft(delta_DFT)  # IDFT

# 元信号（単位インパルス応答）とDFT・IDFT後の信号を比較
print("元波形")
print(delta)
print("変換後波形")
print(delta_DFT_IDFT)

plt.plot(range(len(delta)), delta, marker="o", label="origin")
plt.plot(range(len(delta_DFT_IDFT)), delta_DFT_IDFT, marker="x", label="DFT-IDFT")

plt.legend()
plt.show()
