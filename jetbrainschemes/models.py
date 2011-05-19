import settings
import Image
import os.path
from xml.dom import minidom

class ReadXmlToPhpColors():
    def parse(self):
        
#        xmlOptions = ["PHP_DOC_TAG", "PHP_KEYWORD", "TEXT", "PHP_VAR", "PHP_OPERATION_SIGN", "PHP_DOC_COMMENT_ID",
#                      "PHP_COMMENT", "PHP_IDENTIFIER", "PHP_STRING", "PHP_EXEC_COMMAND_ID",
#                      "PHP_COMMA", "PHP_BRACKETS", "PHP_HEREDOC_ID", "PHP_NUMBER", "PHP_SEMICOLON", "PHP_PREDEFINED SYMBOL",
#                      "PHP_HEREDOC_CONTENT", "PHP_SCRIPTING_BACKGROUND", "PHP_TAG", "JS.KEYWORD"]

        xmlOptions = ["JS.KEYWORD", "JS.STRING"]
        xmlOverrides = {"PHP_SCRIPTING_BACKGROUND": "TEXT" }
        cssString = ""
        override = None
        for xmlOption in xmlOptions:
            if xmlOption in xmlOverrides:
                override = xmlOverrides[xmlOption]
            cssString += self.ConvertToCSS(xmlOption, override)
        return cssString

    def ConvertToCSS(self, value, override):
        className = value.replace (" ", "_")
        className = className.replace (".", "_")
        css = "." + className + " { "
        foreground = self.Lookup(value, "FOREGROUND", override)
        if foreground:
            paddedHexColor = foreground.zfill(6)
            css += "color: #" + paddedHexColor + ";"
        back = self.Lookup(value, "BACKGROUND", override)
        if back:
            paddedHexColor = back.zfill(6)
            css += "background: #" + paddedHexColor + ";"
        style = self.ConvertFontStyle(self.Lookup(value, "FONT_TYPE"))
        if style:
            css += style + "; "
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
                styleText = "font-weight: 700"
            if id == 2:
                styleText = "font-style: italic"
            if id == 3:
                styleText = "font-style: italic; font-weight: 700;"

        return styleText

    def ConvertTextDecoration(self, id, color):
        styleText = ""
        if id and color:
            id = int(id)
            if id == 0:
                colorString = color.encode('utf8')
                colorString = colorString.zfill(6)
                return "border: 1px solid #" + colorString + ";"
            elif id == 1:
                colorString = color.encode('utf8')
                colorString = colorString.zfill(6)
                return "border-bottom: 1px solid #" + colorString + ";"
            elif id == 2:
                colorString = color.encode('utf8')
                colorString = colorString.zfill(6)
                self.CreateWavyImage(colorString)
                return "background: url(" + settings.MEDIA_URL + colorString + ".png) bottom repeat-x;"
            elif id == 3:
                return "text-decoration: line-through;" # Not sure how to make this its own color...
            elif id == 4:
                colorString = color.encode('utf8')
                colorString = colorString.zfill(6)
                return "border-bottom: 2px solid #" + colorString + ";"
            elif id == 5:
                colorString = color.encode('utf8')
                colorString = colorString.zfill(6)
                return "border-bottom: 1px dotted #" + colorString + ";"

        return styleText

    def ConvertHexToRGB(self, value):
        value = value.lstrip('#').zfill(6)
        lv = len(value)
        return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

    def CreateWavyImage(self, hex_color):
        hex_color = hex_color.lstrip('#').zfill(6)
        if os.path.isfile(os.path.join(settings.MEDIA_ROOT, hex_color + ".png")):
            return True
        else:
            im = Image.open(os.path.join(settings.MEDIA_ROOT, "underline.gif"))
            im = im.convert("RGBA")
            pixels = im.load()
            rgb = self.ConvertHexToRGB(hex_color)
            color_value= rgb + (255, )
            invisible_value = (255, 255, 255, 0)
            pixels[0, 0] = invisible_value
            pixels[1, 0] = invisible_value
            pixels[2, 0] = invisible_value
            pixels[3, 0] = color_value

            pixels[0, 1] = color_value
            pixels[1, 1] = invisible_value
            pixels[2, 1] = color_value
            pixels[3, 1] = invisible_value

            pixels[0, 2] = invisible_value
            pixels[1, 2] = color_value
            pixels[2, 2] = invisible_value
            pixels[3, 2] = invisible_value

            im.save(os.path.join(settings.MEDIA_ROOT, hex_color + ".png"), "PNG")
        return True

    def Lookup(self, firstName, secondName, overrideName=None):
        xmldoc = minidom.parse('jetbrainschemes/coolblue.xml')
#        xmldoc = minidom.parse('jetbrainschemes/default3.xml')
#        xmldoc = minidom.parse('jetbrainschemes/emacs.xml')
        for node in xmldoc.getElementsByTagName("option"):
            if node.getAttribute("name") == firstName:
                children = node.childNodes[1]
                for node in children.getElementsByTagName("option"):
                    if node.getAttribute("name") == secondName:
                        if node.getAttribute("value"):
                            return node.getAttribute("value")
        if overrideName:
            return self.Lookup(overrideName, secondName)


#test = ReadXmlToPhpColors()
#print test.CreateWavyImage("FFFFFF")