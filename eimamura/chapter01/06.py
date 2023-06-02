import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def SN(s, x):
    pow_s = np.sum(s**2)
    pow_x = np.sum(x**2)
    
    return 10*np.log10(pow_s/pow_x)

a = np.array([3,4,5])
b = np.array([1,2,3])

print(SN(a, b))