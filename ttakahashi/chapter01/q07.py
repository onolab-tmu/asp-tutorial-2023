from pathlib import Path
from typing import Union
import numpy as np
import soundfile as sf

from q06 import calc_snr


def adjust_snr(s, x, snr):
    return (x / np.sqrt(np.sum(x**2))) * np.sqrt(np.sum(s**2)) * 10 ** (-snr / 20)


def main(input_dir_02: Union[Path, str], input_dir_04: Union[Path, str]):
    in_p_02 = Path(input_dir_02)
    in_p_04 = Path(input_dir_04)

    snr = 0

    y_02, sr = sf.read(in_p_02 / "02.wav")
    y_04, sr = sf.read(in_p_04 / "04.wav")
    mixture = adjust_snr(y_02, y_04, snr)

    print(f"SNR: {calc_snr(mixture, y_04)} (dB)")


if __name__ == "__main__":
    in_p_02 = Path.cwd() / "outputs"
    in_p_04 = Path.cwd() / "outputs"

    main(in_p_02, in_p_04)

    print("Finished")
