
    '''
    def createReader(self, audiofile, channel):
        reader = etree.Element("reader")
        value = etree.Element("value")
        value.set("file", audiofile)
        value.set("channel", str(channel))
        reader.append(value)
        return reader
    
    def createXml(self, template, audiofile):
        #xml_path = 'templates/' + template + '.ptldoc'
        xml_path = pkg_resources.resource_filename(
            __name__, 'templates/' + template + '.ptldoc'
        )
        tree = etree.parse(xml_path)
        root = tree.getroot()
        #path = "templates/temp/" + template + ".ptldoc"
        path = pkg_resources.resource_filename(
            __name__, 'templates/temp/' + template + '.ptldoc'
        )
        with open(path, 'wb') as f:
            tree.write(f, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        return path
    '''