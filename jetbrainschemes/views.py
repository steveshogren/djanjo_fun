from django.http import HttpResponse
import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from jetbrainschemes.models import ReadXmlToPhpColors

def index(request):
    read = ReadXmlToPhpColors()
    colors = read.parse()
    return render_to_response('colors/index.html', {'colors': colors, 'test': settings.MEDIA_ROOT}, context_instance=RequestContext(request))