import pkg_resources
import subprocess

class Exporter():
    def __init__(self, exec_path):
        self.exec_path = exec_path
        self.input = None
        self.template = "Factory"
        self.output = None
        self.format = "jpeg"
        self.width = 1000
        self.height = 800
        self.adapt = False
        self.groups = False
        self.nogrids = False
        self.header = False
        self.separator = ","
        self.reapertype = "region"
        self.description = False
    
    def setInput(self, path):
        self.input = path

    def setTemplate(self, name):
        self.template = pkg_resources.resource_filename(__name__, 'templates/'+ name +'.ptldoc')

    def setOutput(self, path):
        self.output = path

    def setFormat(self, format):
        valid_formats = ["jpeg", "png", "csv", "json"]
        format = format.lower()
        if format not in valid_formats:
            return self.error("format", format + " is not a valid format. Valid formats are" + valid_formats)
        self.format = format
        return 0

    def setDimension(self, name, value):
        if value < 1:
            return self.error(f"set{name.capitalize()}", "value must be greater than 0")
        setattr(self, name.lower(), value)
        return 0

    def setWidth(self, width):
        return self.setDimension("width", width)

    def setHeight(self, height):
        return self.setDimension("height", height)

    def setBoolAttr(self, name, value):
        if type(value) is not bool:
            return self.error(f"set{name.capitalize()}", "value must be a boolean")
        self.adapt = value
        return 0

    def setAdapt(self, value):
        return self.setBoolAttr("adapt", value)

    def setGroups(self, value):
        return self.setBoolAttr("groups", value)

    def setNogrids(self, value):
        return self.setBoolAttr("nogrids", value)

    def setHeader(self, value):
        return self.setBoolAttr("header", value)

    def setDescription(self, value):
        return self.setBoolAttr("description", value)

    def setCharacter(self, value):
        if type(value) is not str and len(value) != 1:
            return self.error("character", "value is not valid")

    def setReaperType(self, value):
        if value != "marker" or value != "region":
            return self.error("reaper type", "must be marker or region")

    def getArgs(self):

        res = [
            "--input=" + self.input,
            "--template=" + self.template,
            "--output=" + self.output,
            "--format=" + self.format
        ]

        if self.adapt:
            res += "--adapt"

        if self.format == "jpeg" or self.format == "csv":
            res += [
                "--width=" + str(self. width),
                "--height=" + str(self.height),
            ]
            if self.groups:
                res += "--groups"

        if self.format == "csv" or self.format == "json":
            if self.nogrids:
                res += "--nogrids"

        if self.format == "csv":
            res += "--separator=" + self.separator 
            if self.header:
                res += "--header"
        
        if self.format == "json":
            if self.description:
                res += "--description"

        return res

    def export(self):
        cmd = [self.exec_path, "--export"] + self.getArgs()
        print(cmd)
        ret = subprocess.run(cmd, capture_output=True, text=True)
        if ret.stderr:
            print("Err:\n", ret.stderr)
        if ret.stdout:
            print("Out:\n", ret.stdout)
        return ret.returncode

    def error(self, functionName, msg):
        print("Exporter Error: ", functionName, ": ", msg)
        return 1