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

    return a


def split_frame(L, S, x):
    x_zero = zero_padding(L, S, x)
    T = int((len(x_zero) - L + 1) / S)
    xt = np.zeros((T, L))
    for t in range(T):
        for l in range(L):
            xt[t][l] = x_zero[t * S + l]

    return xt


x = [1, 1, 1, 1, 1, 1, 1, 1]
L = 4
S = 3
y = zero_padding(L, S, x)
xt = split_frame(L, S, x)
print("x:", x)
print("x_pad:", y)
print("x_t:", xt)
