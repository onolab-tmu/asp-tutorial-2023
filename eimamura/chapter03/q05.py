import numpy as np
import matplotlib.pyplot as plt


def difference_equation(x):
    N = x.size
    y = np.zeros(N)
    NUM_TERMS = 5

    for n in range(N):
        for i in range(NUM_TERMS):
            if n - i >= 0:
                y[n] += x[n - i] / NUM_TERMS
    return y


x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(difference_equation(x))
plt.stem(difference_equation(x))
plt.ylim(0, 1)
plt.show()
