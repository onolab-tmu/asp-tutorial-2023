import numpy as np


def zero_padding(L, S, x):
    L_S = L - S
    y_1 = []
    y_2 = []
    for i in range(L_S):
        y_1 += [0]
    a = y_1 + x + y_1
    for i in range(100):
        zero = i * S - len(a)
        if zero >= 0:
            for i in range(zero):
                y_2 += [0]
            break
    a += y_2

    return np.array(a)


x = [1, 1, 1, 1, 1, 1, 1, 1]
L = 4
S = 3
y = zero_padding(L, S, x)
print("x:", x)
print("x_pad:", y)
