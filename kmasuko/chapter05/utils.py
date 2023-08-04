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


def frame(L, S, x):
    """
    フレームを出力

    Args:
        L(int):窓長
        S(int):シフト長
        x(ndarray):入力信号
    Return:
        frames(ndarray):フレーム列
    """

    x = zero_pad(L, S, x)
    n_frame = int((len(x) - L) / S) + 1
    frames = []

    for t in range(n_frame):
        frames.append(x[t * S : t * S + L])

    frames = np.array(frames)

    return frames


def stft(L, S, win, x):
    """
    短時間フーリエ変換を実行

    Args:
        L(int):窓長
        S(int):シフト長
        win(ndarray):窓関数
        x(ndarray):入力信号
    Return:
        output(ndarray):複素数行列 (Freq, Time)
    """

    frames = frame(L, S, x)
    output = []

    for t in range(len(frames)):
        frames[t] = frames[t] * win
        output.append(np.fft.rfft(frames[t]))

    output = np.array(output, dtype="complex").T

    return output


def snRatio(signal, noise):
    """SN比を計算

    Args:
        signal (ndarray):信号
        noise (ndarray):ノイズ
    Return:
        float: SN比
    """

    signal_power = np.sum(signal**2)
    noise_power = np.sum(noise**2)

    sn = 10 * np.log10(signal_power / noise_power)

    return sn


def gene_noise(signal, sn):
    """目的のSN比になるようにホワイトノイズを作成

    Args:
        signal (ndarray):信号
        sn (float):目的SN比
    Return:
        ndarray:ホワイトノイズ
    """
    signal_power = np.sum(signal**2)
    noise = np.random.randn(len(signal))
    noise_power = np.sum(noise**2)
    noise_coef = np.sqrt(signal_power / noise_power / 10 ** (sn / 10))

    noise = noise_coef * noise
    print("snRatio: {}".format(snRatio(signal, noise)))

    return noise
