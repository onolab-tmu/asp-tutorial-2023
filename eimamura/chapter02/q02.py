<<<<<<< HEAD
import numpy as np

=======
"""2_2"""

import numpy as np
>>>>>>> c3997293507c80cc63d552b80ed4562aec50b09f

def DFT(x):
    N = len(x)
    X = []
    for k in range(N):
        x1 = 0
        for n in range(N):
            a = 2 * np.pi * n * k / N
<<<<<<< HEAD
            x1 += x[n] * np.exp(-1j * a)
        X.append(x1)
    return X


x = [1, 0, 0, 0, 0, 0, 0, 0]
X = DFT(x)
print("元波形")
print(x)
print("DFT処理後")
print(X)
=======
            x1 += x[n]*np.exp(-1j * a)
        X.append(x1)    
    return X

x = [1,0,0,0,0,0,0,0]
X = DFT(x)
print(X)
>>>>>>> c3997293507c80cc63d552b80ed4562aec50b09f
