from pathlib import Path
from lxml import etree
import os
import shutil
import json
import subprocess
from .Version import Version
from .Exporter import Exporter

PARTIELS_HANDLED_VERSION_MIN = "2.0.9"
PARTIELS_HANDLED_VERSION_MAX = "2.0.10"

class Partiels():

    def __init__(self):
        self.setExecPath(self.findExecPath())
        self.isHandledVersion = self.checkVersion()
        self.exporter = Exporter(self.exec_path)

    def getExecPath(self):
        return self.exec_path

    def setExecPath(self, path):
        self.exec_path = path

    def setVampPath(self, path):
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
