from .Exporter import Exporter
from ..Document import Document

class SdifExporter(Exporter):
    def __init__(self, exec_path: str, frame: str, matrix: str, colname: str):
        super().__init__(exec_path)
        self.frame = "aaaa"
        self.matrix = "aaaa"
        self.colname = "default"
        self.setFrame(frame)
        self.setMatrix(matrix)
        self.setColname(colname)

    def checkSignature(self, name: str, value: str):
        if type(value) is not str or len(value) != 4:
            return super().error(name, "should be a 4 characters signaturer")
        return 0

    def setFrame(self, value: str):
        if self.checkSignature("frame", value):
            return
        self.frame = value

    def setMatrix(self, value: str):
        if self.checkSignature("matrix", value):
            return
        self.matrix = value

    def setColname(self, value: str):
        if type(value) is not str:
            return super().error("colname", "should be a string")
        self.colname = value

    def getCmd(self, Document: Document, output: str):
        res = super().getCmd(Document, output)
        res += [
            "--format=sdif",
            "--frame=" + self.frame,
            "--matrix=" + self.matrix,
            "--colname=" + self.colname
        ]
        return res

    def export(self, Document: Document, output: str):
        cmd = self.getCmd(Document, output)
        return super().export(cmd)
