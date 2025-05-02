import pkg_resources

class Exporter():
    def __init__(self):
        self.input = None
        self.template = "Factory"
        self.output = None
        self.format = "jpeg"
        self.width = 1000
        self.height = 800
        self.adapt = True
        self.groups = False
        self.nogrids = False
        self.header = False
        self.separator = ","
        self.reapertype = "region"
        self.description = False
    
        '''
        --input|-i <audiofile> Defines the path to the audio file to analyze (required).
        --template|-t <templatefile> Defines the path to the template file (required).
        --output|-o <outputdirectory> Defines the path of the output folder (required).
        --format|-f <formatname> Defines the export format (jpeg, png, csv, lab, json, cue, reaper or sdif) (required).
        --width|-w <width> Defines the width of the exported image in pixels (required with the jpeg and png formats).
        --height|-h <height> Defines the height of the exported image in pixels (required with the jpeg and png formats).
        --adapt Defines if the block size and the step size of the analyzes are adapted following the sample rate (optional).
        --groups Exports the images of group and not the image of the tracks (optional with the jpeg and png formats).
        --nogrids Ignores the export of the grid tracks (optional with the csv, json or cue formats).
        --header Includes header row before the data rows (optional with the csv format).
        --separator <character> Defines the separator character between columns (optional with the csv format, default is ',').
        --reapertype <type> Defines the type of the reaper format  (optional with the reaper format 'marker' or 'region', default is 'region').
        --description Includes the plugin description (optional with the json format).
            partiels.exporter.setFormat("json")
    assert partiels.export() == 0, "Partiels JSON Export Failed"
        --frame <framesignature> Defines the 4 characters frame signaturer (required with the sdif format).
        --matrix <matrixsignature> Defines the 4 characters matrix signaturer (required with the sdif format).
        --colname <string> Defines the name of the column (optional with the sdif format).
        '''

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
            return self.error("setFormat", format + " is not a valid format. Valid formats are" + valid_formats)
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

    def setBoolAttr(self, value):
        if type(value) is not bool:
            return self.error(f"set{name.capitalize()}", "value must be a boolean")
        self.adapt = value
        return 0

    def getArgs(self):

        res = [
            "--input=" + self.input,
            "--template=" + self.template,
            "--output=" + self.output,
            "--format=" + self.format
        ]

        if self.format == "jpeg" or self.format == "csv":
            res += [
                "--width=" + str(self. width),
                "--height=" + str(self.height)
            ]

        return res

    def error(self, functionName, msg):
        print("Exporter Error: ", functionName, ": ", msg)
        return 1