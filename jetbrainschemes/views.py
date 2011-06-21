from django.http import HttpResponse
import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from jetbrainschemes.models import XmlToPersistence, CssSettings

def index(request):
<<<<<<< HEAD
    file_name = 'AllDefaultsSet.xml'
=======
    file_name = 'coolblue.xml'
>>>>>>> c4cf657d07edbf1094cabaf2833b0ef22d8de4ce

    xmlToPersistence = XmlToPersistence()
    xmlToPersistence.convert(file_name)

    c = CssSettings.objects.get(file_name=file_name)

    return render_to_response('colors/index.html',
                              {'colors': c.css, 'test': settings.MEDIA_ROOT},
                              context_instance=RequestContext(request))
