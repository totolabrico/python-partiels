import pytest
from pathlib import Path
import pkg_resources
import os

from python_partiels.Partiels import Partiels

def test_export():
    partiels = Partiels()
    exec_path = os.environ.get("PARTIELS_EXECUTABLE")
    assert exec_path is not None, "PARTIELS_EXECUTABLE environment variable is not set"
    partiels.setExecPath(exec_path)
    #partiels.setVampPath("/opt/Partiels/PlugIns")
    audiofile = pkg_resources.resource_filename(
            __name__, 'samples/patatine.wav'
        )
    dest = pkg_resources.resource_filename(
            __name__, 'exports/'
        )
    assert partiels.export("beat_detection", audiofile, dest, "json") == 0, "Partiels Export Failed"
