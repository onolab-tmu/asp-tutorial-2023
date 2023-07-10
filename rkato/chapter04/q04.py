from pathlib import Path
from typing import Union
import numpy as np
from matplotlib import pyplot as plt

config = {
    "figure.subplot.bottom": 0.15,
    "figure.subplot.left": 0.15,
    "figure.figsize": [10, 8],
    "font.size": 24,
    "mathtext.fontset": "cm",
    "pdf.fonttype": 42,
    "legend.borderaxespad": 1,
    "lines.linewidth": 2,
    "savefig.transparent": True,
}


LABELS = {
    0: ("viridis", "Power spectrogram"),
    1: ("viridis", "Phase spectrogram"),
    2: (plt.cm.Reds, "Cosine of phase spectrogram"),
    3: (plt.cm.Blues, "Sine of hase spectrogram"),
}


# L-Sこのゼロ詰め　Sの倍数になるようにゼロ詰めする関数
def pad(x, L, S):
    x_pad = np.pad(x, [L - S, L - S])
    re = np.mod(x_pad.size, S)
    if re != 0:
        x_pad = np.pad(x_pad, [0, S - re])
    return x_pad


# フレーム分割
def frame_div(x, L, S):
    x_pad = pad(x, L, S)
    T = int(np.floor((x_pad.size - L) / S)) + 1
    x_t = np.array([x_pad[t * S : t * S + L] for t in range(T)])
    return x_t


# 短時間フーリエ変換
def stft(x, L, S, w):
    x_div = frame_div(x, L, S)
    T = x_div.shape[0]
    X = np.empty([L // 2 + 1, T], dtype="complex")
    for t in range(0, T):
        X[:, t] = np.fft.rfft(x_div[t, :] * w)
    return X


def main(output_dir: Union[Path, str]):
    out_p = Path(output_dir)

    # 正弦波の生成　振幅:１　音高:440Hz 信号長:0.1秒　サンプリングレート:16kHz
    A = 1  # amplitude
    f = 440  # frequency (Hz)
    sec = 0.1  # time (sec)
    fs = 16000  # sampling rate (Hz)
    t = np.arange(0, sec, 1 / fs)
    y = A * np.sin(2 * np.pi * f * t)
    # 窓幅L,シフト幅S
    L = 1000
    S = L // 2

    w = np.hamming(L)
    y_stft = stft(y, L, S, w)
    print(f"y_stft.shape: {y_stft.shape}")
    spec = [
        np.abs(y_stft),
        np.angle(y_stft),
        np.cos(np.angle(y_stft)),
        np.sin(np.angle(y_stft)),
    ]

    # # ここからグラフ描画
    plt.rcParams.update(config)
    fig, ax = plt.subplots(4, 1)
    for i in range(len(spec)):
        # ax[i].pcolormesh(spec[i])
        ax[i].imshow(
            spec[i],
            cmap=LABELS[i][0],
            interpolation="nearest",
            aspect="auto",
            origin="lower",
            extent=[0, y_stft.shape[1], 0, y_stft.shape[0]],
        )
        ax[i].set_title(LABELS[i][1])
        ax[i].set_rasterized(True)
    fig.supxlabel("Frame")
    fig.supylabel("Frequency (Hz)")
    plt.tight_layout()
    fig.subplots_adjust(
        left=0.13, right=1 - 0.13, bottom=0.11, top=1 - 0.11, hspace=0.8
    )
    plt.savefig(out_p / "04.pdf", dpi=300)
    plt.clf()
    plt.close()


if __name__ == "__main__":
    out_p = Path.cwd() / "outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(out_p)

    print("Finished")
