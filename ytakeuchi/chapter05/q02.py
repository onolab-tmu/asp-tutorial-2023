import numpy as np


def calc_amv_circular(r, M, theta, f):
    c = 334
    u = np.array([np.sin(np.deg2rad(theta)), np.cos(np.deg2rad(theta)), 0])
    p = np.zeros((M, 3))
    a = np.zeros(M, dtype="complex")
    for m in range(M):
        p[m] = np.array([r * np.sin(2 * np.pi * m / M), r * np.cos(2 * np.pi * m / M), 0])
        a[m] = np.exp(2j * np.pi * f / c * np.dot(u, p[m]))
    return a


if __name__ == "__main__":
    r = 0.05
    M = 3
    theta = 45
    f = 1000

    a = calc_amv_circular(r, M, theta, f)
    print(a)

    ##########手計算で確認##########

    """
    u=[1/sqrt(2), 1/sqrt(2), 0]^T
    p1=[0.05*sin(0), 0.05*cos(0), 0]^T=[0, 0.05, 0]^T
    p2=[0.05*sin(2pi/3), 0.05*cos(2pi/3), 0]^T=[sqrt(3)/40, -0.025, 0]^T
    p3=[0.05*sin(4pi/3), 0.05*cos(4pi/3), 0]^T=[-sqrt(3)/40, -0.025, 0]^T
    a1=exp((2*pi*1000*0.05)j/(334*sqrt(2)))=exp(25sqrt(2)pij/167)=0.79+0.62j
    a2=exp((2*pi*1000*(sqrt(6)-sqrt(2))j/(334*80))=exp(25(sqrt(6)-sqrt(2))pij/334)=0.97+0.24j
    a3=exp((2*pi*1000*(-sqrt(6)-sqrt(2))j/(334*80))=exp(-25(sqrt(6)+sqrt(2))pij/334)=0.61-0.79j
    """
    print(
        np.exp(25j * np.sqrt(2) * np.pi / 167),
        np.exp(25j * (np.sqrt(6) - np.sqrt(2)) * np.pi / 334),
        np.exp(25j * (-np.sqrt(6) - np.sqrt(2)) * np.pi / 334),
    )
