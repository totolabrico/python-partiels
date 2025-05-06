from pathlib import Path
from lxml import etree
import os
import shutil
import json
import subprocess
from .Version import Version
from .Document import Document
from .Exporters.ImageExporter import ImageExporter
from .Exporters.TextExporter import CsvExporter, JsonExporter, CueExporter
from .Exporters.SdifExporter import SdifExporter
from .Exporters.ReaperExporter import ReaperExporter
from .Exporters.LabExporter import LabExporter

PARTIELS_HANDLED_VERSION_MIN = "2.0.9"
PARTIELS_HANDLED_VERSION_MAX = "2.0.10"

class Partiels():

    def __init__(self):
        self.setExecPath(self.findExecPath())
        self.isHandledVersion = self.checkVersion()

    def getExecPath(self):
        return self.exec_path

    def setExecPath(self, path: str):
        self.exec_path = path

    def setVampPath(self, path: str):
        os.environ["VAMP_PATH"] = path

    def findExecPath(self):
        exec_name = "Partiels"
        exec_path = shutil.which(exec_name)
        if exec_path:
            return exec_path
        else:
            print(f"Executable '{exec_name}' non trouvé dans PATH.")
        return None

    def checkVersion(self):
        cmd = [self.exec_path, "--version"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        version = Version.from_string(res.stdout.split(" v")[1][:-1])
        min = Version.from_string(PARTIELS_HANDLED_VERSION_MIN)
        max = Version.from_string(PARTIELS_HANDLED_VERSION_MAX)

        if version is None:
            print("Error parsing Partiels version")
            return False
        if version.isMoreRecent(max):
            print("The Version of Partiel is too recent for the wrapper")
            return False
        if min.isMoreRecent(version):
            print("The Version of Partiel is too old for the wrapper")
            return False
        return True

    def createDocument(self, input:str = None, template:str):
        return Document(input, template)

    def createDefaultDocument(self, input:str = None, template:str):
        return Document(input, template, True)

    def createJpegExporter(self, format:str = "jpeg", width:int = 1000, height:int = 800, groups:bool = False):
        return ImageExporter(self.exec_path, format, width, height, groups)

    def createPngExporter(self, format:str = "png", width:int = 1000, height:int = 800, groups:bool = False):
        return ImageExporter(self.exec_path, format, width, height, groups)

    def createCsvExporter(self, nogrids:bool = False, header:bool = False, separator:str = ","):
        return CsvExporter(self.exec_path, nogrids, header, separator)

    def createJsonExporter(self, nogrids:bool = False, description:bool = False):
        return JsonExporter(self.exec_path, nogrids, description)

    def createCueExporter(self, nogrids:bool = False):
        return CueExporter(self.exec_path, nogrids)

    def createSdifExporter(self, frame:str = None, matrix:str = None, colname:str = None):
        return SdifExporter(self.exec_path, frame, matrix, colname)

    def createReaperExporter(self, reaperType:str = "region"):
        return ReaperExporter(self.exec_path, reaperType)

    def createLabExporter(self):
        return LabExporter(self.exec_path)

