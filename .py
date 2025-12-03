import soundfile as sf
from IPython.display import Audio
import numpy as np

# Lecture propre
sound, rate = sf.read("sonogramme/sound.wav", dtype="int16")

# Si tu veux un tableau numpy comme avec SciPy
sound = np.asarray(sound)

Audio(sound, rate=rate)
