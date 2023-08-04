import numpy as np


def calc_amv_linear(d, M, theta, f):
    c = 334
    u = np.array([np.sin(np.deg2rad(theta)), np.cos(np.deg2rad(theta)), 0])  # 平面派の到来方向を表すベクトル
    p = np.zeros((M, 3))  # マイクロフォンの配置を表すベクトル
    a = np.zeros(M, dtype="complex")  # 位相回転量を表す行列（遅延を表現）
    for m in range(M):
        p[m][0] = (m - (M - 1) / 2) * d  # m=1,2,3だが，Pythonのindexに合わせるためm=0,1,2となっている．そのため(m-1)をmと置き換えている
        a[m] = np.exp(2j * np.pi * f / c * np.dot(u, p[m]))
    return a


if __name__ == "__main__":
    d = 0.05
    M = 3
    theta = 45
    f = 1000

    a = calc_amv_linear(d, M, theta, f)
    print(a)

    ##########手計算で確認##########

    """
    u=[1/sqrt(2), 1/sqrt(2), 0]^T
    p1=[(0-(3-1)/2)*0.05, 0, 0]^T=[-0.05, 0, 0]^T
    p2=[0, 0, 0]^T
    p3=[0.05, 0, 0]^T
    以下，u^T･pm=pm[0]/sqrt(2)であることに注意
    a1=exp((2*pi*1000*(-0.05))j/(334*sqrt(2)))=exp(-25sqrt(2)pij/167)=0.79-0.62j
    a2=exp((2*pi*1000*0)j/334)=exp(0)=1
    a3=exp((2*pi*1000*0.05)j/(334*sqrt(2)))=exp(25sqrt(2)pij/167)=0.79+0.62j
    """
    print(np.exp(-25j * np.sqrt(2) * np.pi / 167), np.exp(25j * np.sqrt(2) * np.pi / 167))
