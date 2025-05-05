from .Exporter import Exporter

class ReaperExporter(Exporter):
    def __init__(self, exec_path, reaperType):
        super().__init__(exec_path)
        if self.setReaperType(reaperType):
            self.reaper_type = "region"

    def setReaperType(self, value):
        if value != "region" and value != "marker":
            return super().error("reapertype", "should be region or marker")
        self.reaper_type = value

    def getCmd(self, Document, output):
        res = super().getCmd(Document, output)
        res += [
            "--format=reaper",
            "--reapertype=" + self.reaper_type,
        ]
        return res

    def export(self, Document, output):
        cmd = self.getCmd(Document, output)
        return super().export(cmd)