from .Exporter import Exporter
from ..Document import Document

class LabExporter(Exporter):
    def __init__(self, exec_path: str):
        super().__init__(exec_path)

    def getCmd(self, Document: Document, output: str):
        res = super().getCmd(Document, output)
        res.append("--format=lab")
        return res
    
    def export(self, Document: Document, output: str):
        cmd = self.getCmd(Document, output)
        return super().export(cmd)