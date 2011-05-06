#from django.db import models
#
#class Scheme(models.Model):
##    def __unicode__(self):
##        return self.question
##
##    def was_published_today(self):
##        return self.pub_date.date() == datetime.date.today()
#
#
#    question = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')

from xml.dom import minidom

class ReadXmlToPhpColors():
    def parse(self):
        xmldoc = minidom.parse('jetbrainschemes/test.xml')
        option = xmldoc.getElementsByTagNameNS('option')
        for node in xmldoc.getElementsByTagName("option"):
            if node.hasAttribute == 'PHP_KEYWORD':
                test = node
#        option = xmldoc.getElementsByTagName('attributes')
#        foreground = option.getElementsByTagNameNS('option', 'FOREGROUND')
        return test

#    scheme/attributes/ option = PHP_KEYWORD/value/option = FOREGROUND
