import numpy as np


def zero_pad(L, S, x):
    """
    ゼロ埋めを実行

    Args:
        L(int):窓幅
        S(int):シフト幅
        x(ndarray):入力信号
    Return:
        signal(ndarray):出力信号
    """

    # 例外処理
    if S >= L:
        print("Window length must be longer than shift length!")
        return None

    # 先頭末尾にゼロ埋め
    zeros = np.zeros(int(L - S))
    x = np.concatenate([zeros, x], axis=0)
    x = np.concatenate([x, zeros], axis=0)

    # 信号長がSの倍数になるようにゼロ埋め
    if len(x) % S != 0:
        zeros = np.zeros(S - len(x) % S)
        x = np.concatenate([x, zeros], axis=0)

    return x


if __name__ == "__main__":
    win_len = 5
    hop_len = 2
    x = np.array([1, 2, 3, 4, 5])
    x = zero_pad(win_len, hop_len, x)
    print(x)
