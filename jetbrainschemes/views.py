from django.http import HttpResponse
from django.shortcuts import render_to_response
from jetbrainschemes.models import ReadXmlToPhpColors

def index(request):
#    game_list = Game.objects.all()[:5]
#    read = ReadXmlToPhpColors()
#    xml = read.parse()
#    return render_to_response("colors/index.html", {'xml': xml})
    read = ReadXmlToPhpColors()
    xml = read.parse()
    return render_to_response('colors/index.html', {'php_keyword': xml})