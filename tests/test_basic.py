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


def export(partiels):
    partiels.exporter.setFormat("JPEG")
    assert partiels.exporter.export() == 0, "Partiels JPEG Export Failed"
    partiels.exporter.setFormat("Png")
    assert partiels.exporter.export() == 0, "Partiels PNG Export Failed"
    partiels.exporter.setFormat("csv")
    assert partiels.exporter.export() == 0, "Partiels CSV Export Failed"
    partiels.exporter.setFormat("json")
    assert partiels.exporter.export() == 0, "Partiels JSON Export Failed"

def test_export():
    partiels = Partiels()
    partiels.exporter.setInput(pkg_resources.resource_filename(__name__, 'samples/patatine.wav'))
    partiels.exporter.setTemplate('beat_detection')
    partiels.exporter.setOutput(pkg_resources.resource_filename(__name__, 'exports/'))
    export(partiels)
    partiels.exporter.setWidth(500)
    partiels.exporter.setHeight(200)
    partiels.exporter.setAdapt(True)
    partiels.exporter.setDescription(True)
    partiels.exporter.setGroups(True)
    partiels.exporter.setHeader(True)
    partiels.exporter.setNogrids(True)
    partiels.exporter.setCharacter(":")
    partiels.exporter.setReaperType("marker")
    export(partiels)

