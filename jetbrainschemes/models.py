from xml.dom import minidom

class ReadXmlToPhpColors():
    def parse(self):
        colors = {'text_back': 'ffffff', 'text_fore': 'ffffff', 'keyword_fore': 'ffffff'}
        colors['keyword_fore'] = self.Lookup("PHP_KEYWORD", "FOREGROUND")
        colors['text_back'] = self.Lookup("TEXT", "BACKGROUND")
        colors['text_fore'] = self.Lookup("TEXT", "FOREGROUND")
        return colors

    def Lookup(self, firstName, secondName):
        xmldoc = minidom.parse('jetbrainschemes/test.xml')
        for node in xmldoc.getElementsByTagName("option"):
            if node.getAttribute("name") == firstName:
                children = node.childNodes[1]
                for node in children.getElementsByTagName("option"):
                    if node.getAttribute("name") == secondName:
                        return node.getAttribute("value")

test = ReadXmlToPhpColors()
print test.parse()