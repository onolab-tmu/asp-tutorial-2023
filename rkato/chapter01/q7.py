import numpy as np
import q6
import math 


def adj_snr(s,snr):

    #入力したSN比に応じたノイズを重畳

    n_white = np.random.rand(round(len(s)))

    a=q6.get_snr(s,n_white)
    n_adj=n_white*np.sqrt(a/10**(snr/10))

    
    return  s+n_adj
