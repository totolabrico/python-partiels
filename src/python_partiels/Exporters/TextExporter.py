from .Exporter import Exporter

class TextExporter(Exporter):
    
    def __init__(self, exec_path, nogrids):
        super().__init__(exec_path)
        self.nogrids = False
        self.setNogrids(nogrids)

    def setNogrids(self, value):
        if super().checkBoolAttr("nogrids", value):
            return
        self.nogrids = value

    def getCmd(self, Document, output):
        res = super().getCmd(Document, output)
        if self.nogrids:
            res.append("--nogrids")
        return res

    def export(self, cmd):
        return super().export(cmd)


class CsvExporter(TextExporter):
    def __init__(self, exec_path, nogrids, header, separator):
        super().__init__(exec_path, nogrids)
        self.header = False
        self.separator = ","
        self.setHeader(header)
        self.setSeparator(separator)

    def setHeader(self, value):
        if super().checkBoolAttr("header", value):
            return
        self.header = value

    def setSeparator(self, value):
        if type(value) is not str and len(value) != 1:
            return self.error("character", "value is not valid")
        self.separator = value

    def getCmd(self, Document, output):
        res = super().getCmd(Document, output)
        res += [
            "--format=csv",
            "--separator=" + self.separator
            ]
        if self.header:
            res.append("--header")
        return res

    def export(self, Document, output):
        cmd = self.getCmd(Document, output)
        return super().export(cmd)

class JsonExporter(TextExporter):
    def __init__(self, exec_path, nogrids, description):
        super().__init__(exec_path, nogrids)
        self.description = False
        self.setDescription(description)

    def setDescription(self, value):
        if super().checkBoolAttr("description", value):
            return
        self.description = value

    def getCmd(self, Document, output):
        res = super().getCmd(Document, output)
        res.append("--format=json")
        if self.description:
            res.append("--description")
        return res

    def export(self, Document, output):
        cmd = self.getCmd(Document, output)
        return super().export(cmd)

class CueExporter(TextExporter):
    def __init__(self, exec_path, nogrids):
        super().__init__(exec_path, nogrids)

    def getCmd(self, Document, output):
        res = super().getCmd(Document, output)
        res.append("--format=cue")
        return res
    
    def export(self, Document, output):
        cmd = self.getCmd(Document, output)
        return super().export(cmd)