from .Exporter import Exporter

class SdifExporter(Exporter):
    def __init__(self, exec_path, frame, matrix, colname):
        super().__init__(exec_path)
        self.frame = ""
        self.matrix = ""
        self.colname = ""
        self.setFrame(frame)
        self.setMatrix(matrix)
        self.setColname(colname)

    def checkSignature(self, name, value):
        if type(value) is not str or len(value) != 4:
            return super().error(name, "should be a 4 characters signaturer")
        return 0

    def setFrame(self, value):
        if self.checkSignature("frame", value):
            return
        self.frame = value

    def setMatrix(self, value):
        if self.checkSignature("matrix", value):
            return
        self.matrix = value

    def setColname(self, value):
        if type(value) is not str:
            return super().error("colname", "should be a string")
        self.colname = value

    def getCmd(self, Document, output):
        res = super().getCmd(Document, output)
        res += [
            "--format=sdif",
            "--frame=" + self.frame,
            "--matrix=" + self.matrix,
            "--colname=" + self.colname
        ]
        return res

    def export(self, Document, output):
        cmd = self.getCmd(Document, output)
        return super().export(cmd)
