#二つの信号のSN比を計算

import numpy as np


def get_snr(s,n):

 sn = (np.sum(s**2))/(np.sum(n**2))

 return  10*np.log10(sn)
    

