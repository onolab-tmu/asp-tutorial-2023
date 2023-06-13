import numpy as np
import matplotlib.pyplot as plt

def make_ham(N):
    w=np.zeros(N)
    for n in range(N):
        w[n]=0.54-0.46*np.cos(2*np.pi*n/(N-1))
    return w

##########確認コード##########

'''N=7のとき
w[0]=0.54-0.46cos(0)=0.08
w[1]=0.54-0.46cos(pi/3)=0.31
w[2]=0.54-0.46cos(2pi/3)=0.77
w[3]=0.54-0.46cos(pi)=1.00
w[4]=0.54-0.46cos(4pi/3)=0.77
w[5]=0.54-0.46cos(5pi/3)=0.31
w[6]=0.54-0.46cos(2pi)=0.08
'''

w=make_ham(7)
plt.plot(w)
plt.show()
print(w)