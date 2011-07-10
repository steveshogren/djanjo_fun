from django.http import HttpResponse
import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from jetbrainschemes.models import XmlToPersistence, CssSettings

def index(request):
    file_name = 'twilightest.xml'

#    xmlToPersistence = XmlToPersistence()
#    xmlToPersistence.convert(file_name)

    c = CssSettings.objects.get(file_name=file_name)

    return render_to_response('colors/index.html',
                              {'colors': c.css, 'test': settings.MEDIA_ROOT, 'mediaurl': settings.MEDIA_URL},
                              context_instance=RequestContext(request))
