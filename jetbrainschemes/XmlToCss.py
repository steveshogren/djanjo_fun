import settings
import Image
import os.path
from xml.dom import minidom

class XmlToCss():
    def convert(self, file_name):
        xmlOptions = []
        xmlOverrides = {"PHP_SCRIPTING_BACKGROUND": "TEXT" }
        cssString = ""
        override = None
        xml_contents = minidom.parse('jetbrainschemes/' + file_name)

        optionsToSkip = ["EFFECT_TYPE", "FONT_TYPE", "BACKGROUND", "FOREGROUND", "EFFECT_COLOR", "ERROR_STRIPE_COLOR"]
        for node in xml_contents.getElementsByTagName("option"):
            if node.getAttribute("name") not in optionsToSkip:
                xmlOptions.append(node.getAttribute("name").encode('utf8'))

        print (xmlOptions)
        for xmlOption in xmlOptions:
            if xmlOption in xmlOverrides:
                override = xmlOverrides[xmlOption]
            cssString += self.__convertToCss(xmlOption, override, xml_contents)
        return cssString

    def __convertToCss(self, value, override, xml):
        className = value.replace (" ", "_")
        className = className.replace (".", "_")
        css = "." + className + " { \n"

        foreground = self.__lookupXmlOption(xml, value, "FOREGROUND", override)
        if foreground:
            paddedHexColor = foreground.zfill(6)
            css += "   /* Foreground */ color: #" + paddedHexColor + ";  \n"

        back = self.__lookupXmlOption(xml, value, "BACKGROUND", override)
        if back:
            paddedHexColor = back.zfill(6)
            css += "   /* BackGround */ background: #" + paddedHexColor + ";  \n"

        css += "   /* Font Type */ " + self.__convertFontStyle(self.__lookupXmlOption(xml, value, "FONT_TYPE")) + ";  \n"
        css += "   /* Effect */ " + self.__convertTextDecoration(self.__lookupXmlOption(xml, value, "EFFECT_TYPE"), self.__lookupXmlOption(xml, value, "EFFECT_COLOR")) + "; \n"
        css += "} \n"

        return css

    def __convertFontStyle(self, id):
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

    def __convertTextDecoration(self, id, color):
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
                self.__createWavyImage(colorString)
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

    def __convertHexToRGB(self, value):
        value = value.lstrip('#').zfill(6)
        lv = len(value)
        return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

    def __createWavyImage(self, hex_color):
        hex_color = hex_color.lstrip('#').zfill(6)
        if os.path.isfile(os.path.join(settings.MEDIA_ROOT, hex_color + ".png")):
            return True
        else:
            im = Image.open(os.path.join(settings.MEDIA_ROOT, "underline.gif"))
            im = im.convert("RGBA")
            pixels = im.load()
            rgb = self.__convertHexToRGB(hex_color)
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

    def __lookupXmlOption(self, xmldoc, firstName, secondName, overrideName=None):
        for node in xmldoc.getElementsByTagName("option"):
            if node.getAttribute("name") == firstName:
                if len(node.childNodes) > 1:
                    children = node.childNodes[1]
                    for node in children.getElementsByTagName("option"):
                        if node.getAttribute("name") == secondName:
                            if node.getAttribute("value"):
                                return node.getAttribute("value")
        if overrideName:
            return self.__lookupXmlOption(xmldoc, overrideName, secondName)