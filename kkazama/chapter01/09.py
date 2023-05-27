import soundfile as sf

x, _ = sf.read("08.wav")

fs = 8000

sf.write("09.wav", x, 8000, subtype="PCM_16")
