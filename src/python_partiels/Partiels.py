import pkg_resources
from pathlib import Path
from lxml import etree
import subprocess
import os
import shutil

class Partiels():

    def __init__(self):
        self.setExecPath(self.findExecPath())

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

    def export(self, template, audiofile, dest, format):
        template = pkg_resources.resource_filename(
            __name__, 'templates/' + template + '.ptldoc'
        )
        cmd = [self.exec_path, "--export", "-i", audiofile, "-t", template, "-o", dest, "-f", format]
        env = os.environ.copy()
        ret = subprocess.run(cmd, capture_output=True, text=True, env=env)
        if ret.stderr:
            print(ret.stderr)
        if ret.stdout:
            print(ret.stdout)
        return ret.returncode