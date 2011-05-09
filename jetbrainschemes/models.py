class ReadXmlToPhpColors():
    def parse(self):
        
        xmlOptions = ["PHP_KEYWORD", "TEXT", "PHP_VAR", "PHP_OPERATION_SIGN", "PHP_DOC_COMMENT_ID",
                     "PHP_DOC_COMMENT_ID", "PHP_DOC_COMMENT_ID", "PHP_DOC_TAG", "PHP_COMMENT", "PHP_COMMENT",
                     "PHP_IDENTIFIER", "PHP_STRING"]

        cssString = ""
        for xmlOption in xmlOptions:
            cssString += self.ConvertToCSS(xmlOption)
        return cssString

    def ConvertToCSS(self, value):
        css = "." + value + " { "
        foreground = self.Lookup(value, "FOREGROUND")
        if foreground:
            if len (foreground) == 4:
                foreground = "00" + foreground
            css += "color: #" + foreground + ";"
        back = self.Lookup(value, "BACKGROUND")
        if back:
            css += "background: #" + back + ";"
        style = self.ConvertFontStyle(self.Lookup(value, "FONT_TYPE"))
        if style:
            css += "font-style: " + style + ";"
        decoration = self.ConvertTextDecoration(self.Lookup(value, "EFFECT_TYPE"))
        if decoration:
            css += "text-decoration: " + decoration + ";"
        css += " } \n"
        return css

    def ConvertFontStyle(self, id):
        styleText = ""
        if id:
            id = int(id)
            if id == 1:
                styleText = "bold"
            if id == 2:
                styleText = "italic"

        return styleText

    def ConvertTextDecoration(self, id):
        styleText = ""
        if id:
            id = int(id)
            if id == 1:
                styleText = "underline"

        return styleText

    def Lookup(self, firstName, secondName):
#        xmldoc = minidom.parse('jetbrainschemes/test.xml')
        xmldoc = minidom.parse('jetbrainschemes/emacs.xml')
        for node in xmldoc.getElementsByTagName("option"):
            if node.getAttribute("name") == firstName:
                children = node.childNodes[1]
                for node in children.getElementsByTagName("option"):
                    if node.getAttribute("name") == secondName:
                        return node.getAttribute("value")

from xml.dom import minidom

test = ReadXmlToPhpColors()
print test.parse()