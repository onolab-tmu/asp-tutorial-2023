from pathlib import Path
from typing import Optional, Union
import numpy as np
import soundfile as sf


def calc_snr(s, x):
    return 10 * np.log10(np.sum(s**2) / np.sum(x**2))


def main(input_dir: Union[Path, str]):
    in_p = Path(input_dir)

    A = 10  # amplitude
    sr = 16000  # sampling rate (Hz)

    y, sr = sf.read(in_p / "02.wav")
    yxA = y * A

    print(f"SNR: {calc_snr(y, y)} (dB)")
    print(f"SNR: {calc_snr(y, yxA)} (dB)")


if __name__ == "__main__":
    in_p = Path.cwd() / "02/outputs"

    main(in_p)

    print("Finished")
