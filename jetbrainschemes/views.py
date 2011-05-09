from django.http import HttpResponse
from django.shortcuts import render_to_response
from jetbrainschemes.models import ReadXmlToPhpColors

def index(request):
    read = ReadXmlToPhpColors()
    colors = read.parse()
    return render_to_response('colors/index.html', {'colors': colors})