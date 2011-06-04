from django.db import models
from jetbrainschemes.XmlToCss import XmlToCss

class CssSettings(models.Model):
    file_name = models.CharField(max_length=250)
    css = models.CharField(max_length=50000)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.file_name

class XmlToPersistence():
    def convert(self, file_name='coolblue.xml'):
        c, created = CssSettings.objects.get_or_create(file_name=file_name)
        
        xmlToCss = XmlToCss()
        c.css = xmlToCss.convert(file_name)
        
        c.save()