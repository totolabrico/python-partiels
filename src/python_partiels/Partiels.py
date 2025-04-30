import pkg_resources
from pathlib import Path
from lxml import etree
import subprocess
import os
import shutil
import json

class Partiels():

    def __init__(self):
        self.config = self.loadConfigFile()
        self.setExecPath(self.findExecPath())
        if self.exec_path:
            self.isMatchingVersion = not bool(self.compareVersions())
        else:
            self.isMatchingVersion = False

    def loadConfigFile(self):
        path = pkg_resources.resource_filename(
            __name__, 'config.json'
        )
        with open(path, 'r') as f:
            config = f.read()
        config = json.loads(config)
        return config

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

    def compareVersions(self):
        cmd = [self.exec_path, "--version"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        version = res.stdout.split(" v")[1][:-1].split(".")
        if len(version) != 3:
            print("Error: Did not get a correct version of Partiels throught CLI --version command")
        handled_versions = self.config["partiels_handled_versions"]
        if not handled_versions:
            print("Error in Config file: partiels_handled_versions does not exist")
        if "min" not in handled_versions or "max" not in handled_versions:
            print("Error in Config file: partiels_handled_versions: Missing field min or max")
        if len(handled_versions["min"]) != 3 or len(handled_versions["max"]) != 3:
            print("Error in Config file: partiels_handled_versions: Wrong format for min or max")
        for i in range(3):
            version[i] = int(version[i])
        def compareTab(a, b):
            for i in range(3):
                if a < b:
                    return 1
                if a > b:
                    break
            return 0
        if compareTab(version, handled_versions["min"]):
            print("The Version of Partiel is too old for the wrapper")
            return 1
        if compareTab(handled_versions["max"], version):
            print("The Version of Partiel is too recent for the wrapper")
            return 1
        return 0

    def export(self, template, audiofile, dest, format):
        template = pkg_resources.resource_filename(
            __name__, 'templates/' + template + '.ptldoc'
        )
        cmd = [self.exec_path, "--export", "-i", audiofile, "-t", template, "-o", dest, "-f", format]
        ret = subprocess.run(cmd, capture_output=True, text=True)
        if ret.stderr:
            print(ret.stderr)
        if ret.stdout:
            print(ret.stdout)
        return ret.returncode