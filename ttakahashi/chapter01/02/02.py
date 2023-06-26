from pathlib import Path
from typing import Optional, Union
import numpy as np
import soundfile as sf


def main(output_dir: Union[Path, str]):
    out_p = Path(output_dir)

    A = 1  # amplitude
    f = 440  # frequency (Hz)
    sec = 3  # time (sec)
    sr = 16000  # sampling rate (Hz)

    t = np.arange(sec * sr) / sr
    y = A * np.sin(2 * np.pi * f * t)

    sf.write(out_p / "02.wav", y, sr, format="WAV", subtype="PCM_16")

    print(sf.info(out_p / "02.wav"))


if __name__ == "__main__":
    out_p = Path.cwd() / "02/outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(out_p)

    print("Finished")
