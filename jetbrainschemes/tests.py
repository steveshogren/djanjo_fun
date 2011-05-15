"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
import models


def data_provider(fn_data_provider):
    """Data provider decorator, allows another callable to provide the data for the test"""
    def test_decorator(fn):
        def repl(self, *args):
            for i in fn_data_provider():
                try:
                    fn(self, *i)
                except AssertionError:
                    print "Assertion error caught with data set ", i
                    raise
        return repl
    return test_decorator

class SimpleTest(TestCase):
    colors = lambda: (
        ( (0, 0, 0), '000' ),
        ( (0, 0, 0), '000000' ),
        ( (170, 187, 204), '#aabbcc' ),
        ( (255, 0, 0), 'ff0000' ),
    )

    @data_provider(colors)
    def test_ConvertingFromHexToRGB(self, color, hex):
        ReadXml = models.ReadXmlToPhpColors()
        self.assertEqual(color, ReadXml.ConvertHexToRGB(hex), "did not get the expected result")

