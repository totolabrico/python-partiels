from .Exporter import Exporter

class LabExporter(Exporter):
    def __init__(self, exec_path):
        super().__init__(exec_path)

    def getCmd(self, Document, output):
        res = super().getCmd(Document, output)
        res.append("--format=lab")
        return res
    
    def export(self, Document, output):
        cmd = self.getCmd(Document, output)
        return super().export(cmd)