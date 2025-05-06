import pkg_resources

class Document():
    def __init__(self, input: str, template: str, isDefault: bool = False):
        self.setInput(input)
        self.setTemplate(template, isDefault)

    def setInput(self, path: str):
        self.input = path

    def setTemplate(self, name: str, isDefault: bool = False):
        if isDefault:
            self.template = pkg_resources.resource_filename(__name__, 'templates/'+ name +'.ptldoc')
        else:
            self.template = name

    def getArgs(self):
        return [
            "--input=" + self.input,
            "--template=" + self.template,
        ]