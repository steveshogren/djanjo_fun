class ReadXmlToPhpColors():
    def parse(self):
        
        xmlOptions = ["PHP_DOC_TAG", "PHP_KEYWORD", "TEXT", "PHP_VAR", "PHP_OPERATION_SIGN", "PHP_DOC_COMMENT_ID",
                      "PHP_COMMENT", "PHP_COMMENT", "PHP_IDENTIFIER", "PHP_STRING",
                      "PHP_COMMA", "PHP_BRACKETS", "PHP_HEREDOC_ID", "PHP_NUMBER", "PHP_SEMICOLON"]

        cssString = ""
        for xmlOption in xmlOptions:
            cssString += self.ConvertToCSS(xmlOption)
        return cssString

    def ConvertToCSS(self, value):
        css = "." + value + " { "
        foreground = self.Lookup(value, "FOREGROUND")
        if foreground:
            paddedHexColor = foreground.zfill(6)
            css += "color: #" + paddedHexColor + ";"
        back = self.Lookup(value, "BACKGROUND")
        if back:
            paddedHexColor = back.zfill(6)
            css += "background: #" + paddedHexColor + ";"
        style = self.ConvertFontStyle(self.Lookup(value, "FONT_TYPE"))
        if style:
            css += "font-style: " + style + ";"
        decoration = self.ConvertTextDecoration(self.Lookup(value, "EFFECT_TYPE"), self.Lookup(value, "EFFECT_COLOR"))
        if decoration:
            css += decoration
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

    def ConvertTextDecoration(self, id, color):
        styleText = ""
        if id and color: #TODO make underlines/underwaves all support colors
            id = int(id)
            if id == 1:
                colorString = color.encode('utf8')
                colorString = colorString.zfill(6)
                return "border-bottom: 1px solid #" + colorString + ";"

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
#
#test = ReadXmlToPhpColors()
#print test.parse()