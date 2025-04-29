import pytest
from pathlib import Path
from python_partiels.xml import Partiels

def test_export():
    partiels = Partiels()
    partiels.setExecPath("/home/toto/Bureau/IRCAM/Partiels/build/Partiels/Partiels")
    partiels.setVampPath("/opt/Partiels/PlugIns")
    partiels.export("spectrogram", "/home/toto/Musique/patatine_mono.wav", "/home/toto/Bureau/IRCAM/Exports/json/", "json")
