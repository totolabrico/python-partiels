import pkg_resources

class Document():
    def __init__(self, input, template):
        self.setInput(input)
        self.setTemplate(template)

    def setInput(self, path):
        self.input = path

    def setTemplate(self, name):
        self.template = pkg_resources.resource_filename(__name__, 'templates/'+ name +'.ptldoc')

    def getArgs(self):
        return [
            "--input=" + self.input,
            "--template=" + self.template,
        ]