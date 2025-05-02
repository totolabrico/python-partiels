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
    assert partiels.isHandledVersion == True, "Partiels Executable Version does not match the wrapper" 

def test_export():
    partiels = Partiels()
    partiels.exporter.setInput(pkg_resources.resource_filename(__name__, 'samples/patatine.wav'))
    partiels.exporter.setTemplate('beat_detection')
    partiels.exporter.setOutput(pkg_resources.resource_filename(__name__, 'exports/'))
    partiels.exporter.setFormat("jpeg")
    assert partiels.export() == 0, "Partiels JPEG Export Failed"
    partiels.exporter.setFormat("JPEG")
    assert partiels.export() == 0, "Partiels PNG Export Failed"
    partiels.exporter.setFormat("csv")
    assert partiels.export() == 0, "Partiels CSV Export Failed"
    partiels.exporter.setFormat("json")
    assert partiels.export() == 0, "Partiels JSON Export Failed"
