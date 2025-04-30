import pytest
from pathlib import Path
import pkg_resources
import os

from python_partiels.Partiels import Partiels

def test_create_instance():
    partiels = Partiels()
    print(partiels.getExecPath())
    assert partiels.getExecPath() is not None, "Partiels Executable not find"

def test_check_version():
    partiels = Partiels()
    print(partiels.isMatchingVersion)
    assert partiels.isMatchingVersion == True, "Partiels Executable Version does not match the wrapper" 

def test_export():
    partiels = Partiels()
    audiofile = pkg_resources.resource_filename(
            __name__, 'samples/patatine.wav'
        )
    dest = pkg_resources.resource_filename(
            __name__, 'exports/'
        )
    assert partiels.export("beat_detection", audiofile, dest, "json") == 0, "Partiels Export Failed"
