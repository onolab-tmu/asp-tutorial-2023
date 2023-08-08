import numpy as np


def zero_pad(L, S, x):
    y = np.pad(x, (L - S, L - S))
    len_modS = len(y) % S
    if len_modS > 0:
        y = np.pad(y, (0, S - len_modS))
    return y


def frame_split(L, S, x):
    x_tilde = zero_pad(L, S, x)
    L_array = np.arange(L)  # 長さLに切り出す配列
    y = x_tilde[L_array].reshape(1, L)  # yに配列を追加していくため，2次元配列にしておく
    # T=int(np.floor((len(x_tilde)-L)/S))+1 #予めyの大きさTがいくつになるか計算することもできる
    # y=np.array([x_tilde[t*S:t*S+L] for t in range(T)]) #yはこのように求めることが可能
    t = 1
    while t * S + L <= len(x_tilde):  # 条件を満たしている間配列を結合していく
        y = np.append(y, x_tilde[t * S + L_array].reshape(1, L), axis=0)
        t += 1
    return y


##########確認コード##########

L = 5
S = 3  # L-S=2なので先頭に0が2つ
x = np.array([1, 3, 5, 7, 9])  # x_tilde=[0,0,1,3,5,7,9,0,0]となる
print(zero_pad(L, S, x))  # x_tilde
print(frame_split(L, S, x))  # 上記のx_tildeを長さ5で3ずつシフトして分割する．
# xが全て含まれるところまでシフトしたら終了となるため，[[0,0,1,3,5],[3,5,7,9,0]]となるはず
# LがSの倍数でない場合，x_tildeの最後までシフトせず情報落ちしてしまう（L，Sは2のべき乗にすることが多い）
