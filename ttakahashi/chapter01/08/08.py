from pathlib import Path
from typing import Optional, Union
import numpy as np
import soundfile as sf


def calc_snr(s, x):
    return 10 * np.log10(np.sum(s**2) / np.sum(x**2))


def adjust_snr(s, x, snr):
    return (x / np.sqrt(np.sum(x**2))) * np.sqrt(np.sum(s**2)) * 10 ** (-snr / 20)


def main(input_dir_02: Union[Path, str], input_dir_04: Union[Path, str], output_dir: Union[Path, str]):
    in_p_02 = Path(input_dir_02)
    in_p_04 = Path(input_dir_04)
    out_p = Path(output_dir)

    snr = 6

    y_02, sr = sf.read(in_p_02 / "02.wav")
    y_04, sr = sf.read(in_p_04 / "04.wav")
    mixture = adjust_snr(y_02, y_04, snr)

    print(f"SNR: {calc_snr(mixture, y_04)} (dB)")

    sf.write(out_p / "08.wav", mixture, sr, format="WAV", subtype="PCM_16")


if __name__ == "__main__":
    in_p_02 = Path.cwd() / "02/outputs"
    in_p_04 = Path.cwd() / "04/outputs"
    out_p = Path.cwd() / "08/outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(in_p_02, in_p_04, out_p)

    print("Finished")
